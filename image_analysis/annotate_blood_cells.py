"""Annotate blood cells."""

import argparse
import xml.etree.ElementTree as ET

import cv2
import matplotlib.pyplot as plt
from numpy import ndarray


def parse_xml(xml_file: str) -> list[dict[str, dict[str, int]]]:
    """Parse an XML file to extract annotations for blood cells.

    :param xml_file: The path to the XML annotation file.
    :return: A list of dictionaries containing the name and bounding box
        coordinates for each annotated object.
    """
    tree = ET.parse(xml_file)
    root = tree.getroot()

    annotations = []
    for obj in root.iter("object"):
        annotations.append(
            {
                "name": obj.find("name").text,
                "bndbox": {
                    "xmin": int(obj.find("bndbox/xmin").text),
                    "ymin": int(obj.find("bndbox/ymin").text),
                    "xmax": int(obj.find("bndbox/xmax").text),
                    "ymax": int(obj.find("bndbox/ymax").text),
                },
            }
        )
    return annotations


def draw_bounding_boxes(
    image: ndarray, annotations: list[dict[str, dict[str, int]]]
) -> ndarray:
    """Draw bounding boxes on an image according to provided annotations.

    :param image: The image on which to draw, as a numpy array.
    :param annotations: A list of dictionaries with annotation details.
    :return: The image with bounding boxes.
    """
    for ann in annotations:
        xmin, ymin, xmax, ymax = ann["bndbox"].values()
        # Update color coding to include platelets
        if ann["name"] == "RBC":
            color = (255, 0, 0)  # Red for RBC
        elif ann["name"] == "WBC":
            color = (0, 0, 255)  # Blue for WBC
        else:
            color = (0, 255, 0)  # Green for Platelets
        cv2.rectangle(image, (xmin, ymin), (xmax, ymax), color, 2)
        cv2.putText(
            image,
            ann["name"],
            (xmin, ymin - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            color,
            2,
        )
    return image


def main(image_file: str, xml_file: str) -> None:
    """Main function for annotating blood cells in an image.

    :param image_file: A path to the image file.
    :param xml_file: A path to the XML annotation file.
    """
    annotations = parse_xml(xml_file)
    image = cv2.imread(image_file)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_with_boxes = draw_bounding_boxes(image, annotations)

    plt.figure(figsize=(8, 6))
    plt.imshow(image_with_boxes)
    plt.axis("off")
    plt.show()

    cell_counts = {}
    for ann in annotations:
        cell_type = ann["name"]
        cell_counts[cell_type] = cell_counts.get(cell_type, 0) + 1

    print(cell_counts)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Annotate blood cells in an image given XML annotations"
    )
    parser.add_argument("image", type=str, help="Path to the image file")
    parser.add_argument(
        "xml", type=str, help="Path to the XML annotation file"
    )

    args = parser.parse_args()

    main(args.image, args.xml)
