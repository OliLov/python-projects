"""Convert dataset from PASCAL VOC XML format to YOLO format."""

import argparse
import os
import xml.etree.ElementTree as ET


def convert_bbox_to_yolo(
    size: tuple[float, float], box: tuple[float, float, float, float]
) -> tuple[float, float, float, float]:
    """Convert bounding box from absolute coordinates to relative coordinates.

    :param size: Tuple of (width, height) of the image.
    :param box: Tuple of (xmin, ymin, xmax, ymax) for the bounding box.
    :return: Tuple of (x_center, y_center, width, height) in relative
        coordinates.
    """
    scale_width = 1.0 / size[0]
    scale_height = 1.0 / size[1]

    center_x = (box[0] + box[2]) / 2.0
    center_y = (box[1] + box[3]) / 2.0
    box_width = box[2] - box[0]
    box_height = box[3] - box[1]

    rel_center_x = center_x * scale_width
    rel_center_y = center_y * scale_height
    rel_width = box_width * scale_width
    rel_height = box_height * scale_height

    return (rel_center_x, rel_center_y, rel_width, rel_height)


def xml_to_txt(input_xml: str, output_txt: str, class_mapping: dict[str, int]):
    """Parse an XML file and write to a .txt file in YOLO format.

    :param input_xml: Path to the input XML file.
    :param output_txt: Path to the output .txt file.
    :param class_mapping: Dictionary mapping class names to class.
    """
    tree = ET.parse(input_xml)
    root = tree.getroot()
    width = int(root.find(".//size/width").text)
    height = int(root.find(".//size/height").text)

    with open(output_txt, "w", encoding="utf-8") as txt_file:
        for obj in root.iter("object"):
            cell_name = obj.find("name").text
            cell_id = class_mapping.get(cell_name, -1)

            if cell_id == -1:
                continue

            xmlbox = obj.find("bndbox")
            box = (
                float(xmlbox.find("xmin").text),
                float(xmlbox.find("ymin").text),
                float(xmlbox.find("xmax").text),
                float(xmlbox.find("ymax").text),
            )
            bbox = convert_bbox_to_yolo((width, height), box)
            txt_file.write(f"{cell_id} {' '.join([str(a) for a in bbox])}\n")


def main(input_dir: str, output_dir: str) -> None:
    """Convert dataset main function.

    Iterates through a directory of XML files, converting each to YOLO format
    and saving the result to a specified output directory.

    :param input_dir: Path to the input directory containing input XML files.
    :param output_dir: Path to the output directory.
    """
    class_mapping = {"RBC": 0, "WBC": 1, "Platelets": 2}

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for xml_file in os.listdir(input_dir):
        if xml_file.endswith(".xml"):
            input_xml_path = os.path.join(input_dir, xml_file)
            output_txt_path = os.path.join(
                output_dir, xml_file.replace(".xml", ".txt")
            )
            xml_to_txt(input_xml_path, output_txt_path, class_mapping)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Convert XML dataset to YOLO format"
    )
    parser.add_argument(
        "input_dir", type=str, help="Directory containing input XML files"
    )
    parser.add_argument(
        "output_dir", type=str, help="Directory to save converted .txt files"
    )

    args = parser.parse_args()
    main(args.input_dir, args.output_dir)
