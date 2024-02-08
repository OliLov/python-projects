"""Webcam hand draw."""

# pylint: disable=no-member
from typing import Any

import cv2
import mediapipe as mp
import numpy as np
from cv2.typing import MatLike

# Initialize MediaPipe Hands module for hand tracking
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1)

# Drawing configuration
PEN_SIZE = 5
COLORS = {"RED": (0, 0, 255)}
COLOR = COLORS["RED"]


def draw_on_image(image: MatLike, result: Any, finger_index: int = 8) -> None:
    """Draw on image based on hand landmarks at finger index.

    :param image: The image to draw on.
    :param result: The detected hand landmarks from MediaPipe.
    :param finger_index: The index of the finger tip to use for drawing.
    """
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            height, width, _ = image.shape

            # Get the finger position
            finger_pos = hand_landmarks.landmark[finger_index]
            finger_x, finger_y = int(finger_pos.x * width), int(
                finger_pos.y * height
            )

            # Add the point
            drawing_points.append((finger_x, finger_y))

    # Draw lines between points
    if len(drawing_points) > 1:
        for i in range(1, len(drawing_points)):
            cv2.line(
                image,
                drawing_points[i - 1],
                drawing_points[i],
                COLOR,
                PEN_SIZE,
            )


# Initialize the list to store points for drawing
drawing_points = []

# Setup video capture from webcam
video_capture = cv2.VideoCapture(0)

# Create a persistent image to draw on
success, frame = video_capture.read()
persistent_image = np.zeros_like(frame) if success else None

while True:
    success, frame = video_capture.read()
    if not success:
        break  # Exit loop if video capture failed

    # Flip frame for a mirror effect and convert color to RGB
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the RGB image
    results = hands.process(rgb_frame)

    # Work on a copy of the persistent image
    image_for_drawing = persistent_image.copy()
    if results.multi_hand_landmarks:
        draw_on_image(image_for_drawing, results)

    # Overlay the drawing image on the current frame
    combined_image = cv2.addWeighted(frame, 0.5, image_for_drawing, 0.5, 0)

    # Display the combined image
    cv2.imshow("Drawing", combined_image)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break  # Exit loop if 'q' is pressed

    # Update the persistent image with the new drawing
    persistent_image = image_for_drawing.copy()

# Release video capture and destroy all OpenCV windows
video_capture.release()
cv2.destroyAllWindows()
