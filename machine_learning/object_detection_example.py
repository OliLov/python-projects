"""Object detection example."""

import cv2
import cvlib
from cvlib.object_detection import draw_bbox

# Load and display the image in a window
image = cv2.imread("images/pedestrian_crossing.jpg")
cv2.imshow("Image", image)

# Wait for a key press
cv2.waitKey(0)

# Perform object detection
bbox, labels, counts = cvlib.detect_common_objects(image)

# Draw boxes object and display the object detection image in a window
output = draw_bbox(image, bbox, labels, counts)
cv2.imshow("Output", output)

# Wait for a key press
cv2.waitKey(0)

# Combine the original image and the object detection image
image = cv2.imread("images/pedestrian_crossing.jpg")
combined_image = cv2.hconcat([image, output])

# Display the combined image
cv2.imshow("Combined Image", combined_image)
cv2.imwrite("images/pedestrian_crossing_output.jpg", combined_image)

# Wait for a key press and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
