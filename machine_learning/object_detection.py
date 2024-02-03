"""Object detection."""

import argparse
from typing import Optional

import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox


def main(image_path: str, output_path: Optional[str] = None) -> None:
    """Object detection main function.

    :param image_path: Path to the input image.
    :param output_path: Path to save the output image.
    """
    image = cv2.imread(image_path)

    if image is None:
        print("Could not read the image.")
        exit(1)

    box, label, count = cv.detect_common_objects(image)

    output = draw_bbox(image, box, label, count)
    cv2.imshow("Object Detection", output)

    if output_path:
        cv2.imwrite(output_path, output)
        print(f"Output image saved as {output_path}")

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Display object detection on image"
    )

    parser.add_argument("image_path", type=str, help="Path to the input image")
    parser.add_argument(
        "-o", "--output", type=str, help="Path to save the output"
    )

    args = parser.parse_args()
    main(args.image_path, args.output)
