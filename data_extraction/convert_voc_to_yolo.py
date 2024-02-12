"""Convert dataset from PASCAL VOC XML format to YOLO format."""

import argparse
import xml.etree.ElementTree as ET
from pathlib import Path


def convert_bbox_to_yolo(
    size: tuple[int, int], box: tuple[float, float, float, float]
) -> tuple[float, float, float, float]:
    """Convert bounding box coordinates from PASCAL VOC format to YOLO format.

    :param size: A tuple of the image size: (width, height)
    :param box: A tuple of the PASCAL VOC bbox: (xmin, ymin, xmax, ymax)
    :return: A tuple of the YOLO bbox: (x_center, y_center, width, height)
    """
    dw = 1.0 / size[0]
    dh = 1.0 / size[1]
    x_center = (box[0] + box[2]) / 2.0
    y_center = (box[1] + box[3]) / 2.0
    width = box[2] - box[0]
    height = box[3] - box[1]
    rel_x_center = x_center * dw
    rel_width = width * dw
    rel_y_center = y_center * dh
    rel_height = height * dh
    return (rel_x_center, rel_y_center, rel_width, rel_height)


def xml_to_txt(input_file: Path, output_txt: Path, classes: list[str]) -> None:
    """Parse an XML file in PASCAL VOC format and convert it to YOLO format.

    :param input_xml: Path to the input XML file.
    :param output_txt: Path to the output .txt file in YOLO format.
    :param classes: A list of class names as strings.
    """
    if input_file.suffix == ".txt":
        try:
            # Attempt to parse the file content as XML
            with input_file.open("r", encoding="utf-8") as file:
                file_content = file.read()
            root = ET.fromstring(file_content)
        except ET.ParseError as e:
            print(f"Error parsing {input_file}: {e}")
            return  # Skip this file and continue with the next
    else:
        try:
            tree = ET.parse(input_file)
            root = tree.getroot()
        except ET.ParseError as e:
            print(f"Error parsing {input_file}: {e}")
            return  # Skip this file and continue with the next

    root = tree.getroot()
    size_element = root.find("size")
    image_width = int(size_element.find("width").text)
    image_height = int(size_element.find("height").text)

    with output_txt.open("w") as file:
        for obj in root.iter("object"):
            is_difficult = obj.find("difficult").text
            class_name = obj.find("name").text
            if class_name not in classes or int(is_difficult) == 1:
                continue
            class_id = classes.index(class_name)
            xml_box = obj.find("bndbox")
            bbox = (
                float(xml_box.find("xmin").text),
                float(xml_box.find("ymin").text),
                float(xml_box.find("xmax").text),
                float(xml_box.find("ymax").text),
            )
            yolo_bbox = convert_bbox_to_yolo((image_width, image_height), bbox)
            file.write(f"{class_id} {' '.join(map(str, yolo_bbox))}\n")


def main(input_dir: Path, output_dir: Path, classes_file: Path) -> None:
    """Convert dataset main function.

    :param input_xml: Path to the input XML file.
    :param output_txt: Path to the output .txt file in YOLO format.
    :param classes: A list of class names as strings.
    """
    classes = classes_file.read_text().splitlines()

    output_dir.mkdir(parents=True, exist_ok=True)

    for xml_file in input_dir.glob("*"):
        output_txt_path = output_dir / xml_file.with_suffix(".txt").name
        xml_to_txt(xml_file, output_txt_path, classes)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Convert XML dataset to YOLO format"
    )
    parser.add_argument(
        "input_dir", type=Path, help="Directory containing input XML files"
    )
    parser.add_argument(
        "output_dir", type=Path, help="Directory to save converted .txt files"
    )
    parser.add_argument(
        "classes_file",
        type=Path,
        help="File containing class names, one per line",
    )

    args = parser.parse_args()
    main(args.input_dir, args.output_dir, args.classes_file)
