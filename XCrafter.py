import os
import json
import argparse
import shutil
import re


def to_snake_case(name):
    name = re.sub(r'[\s\-]+', '_', name)
    name = re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()
    name = re.sub(r'_+', '_', name)  # Replace multiple underscores with a single underscore
    return name


def to_camel_case(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])


def create_xcassets(asset_name, images_folder, subfolder_name=None, enum_class_name=None):
    # Define the paths
    xcassets_path = asset_name + ".xcassets"
    os.makedirs(xcassets_path, exist_ok=True)

    # Optionally create a subfolder inside .xcassets
    if subfolder_name:
        xcassets_path = os.path.join(xcassets_path, subfolder_name)
        os.makedirs(xcassets_path, exist_ok=True)

    # List all images in the specified folder and filter out non-image files
    images = [f for f in os.listdir(images_folder) if
              f.endswith(('.png', '.svg')) and os.path.isfile(os.path.join(images_folder, f))]

    # Group images by their base name (without @2x, @3x, etc.)
    image_groups = {}
    for image in images:
        base_name = re.sub(r'(@[23]x)?(\.png|\.svg)$', '', image)
        if base_name not in image_groups:
            image_groups[base_name] = []
        image_groups[base_name].append(image)

    # Process each group of images
    icon_cases = []
    for base_name, image_group in image_groups.items():
        snake_case_base_name = to_snake_case(base_name)
        camel_case_name = to_camel_case(snake_case_base_name)
        asset_folder_path = os.path.join(xcassets_path, snake_case_base_name + ".imageset")
        os.makedirs(asset_folder_path, exist_ok=True)
        contents_json_path = os.path.join(asset_folder_path, "Contents.json")

        # Prepare the image entries for Contents.json
        images_json = []
        for image in image_group:
            # Convert image name to snake case and lowercase if it is not already in the correct format
            snake_case_image = to_snake_case(os.path.splitext(image)[0]) + os.path.splitext(image)[1].lower()

            if image.endswith('.svg'):
                image_entry = {
                    "filename": snake_case_image,
                    "idiom": "universal"
                }
            else:
                if '@2x' in image:
                    scale = '2x'
                elif '@3x' in image:
                    scale = '3x'
                else:
                    scale = '1x'  # default scale for png

                image_entry = {
                    "filename": snake_case_image,
                    "idiom": "universal",
                    "scale": scale
                }

            images_json.append(image_entry)

            # Copy and rename images to the .xcassets folder
            shutil.copy(os.path.join(images_folder, image), os.path.join(asset_folder_path, snake_case_image))

        # Define the Contents.json structure
        contents_json = {
            "images": images_json,
            "info": {
                "version": 1,
                "author": "xcode"
            }
        }

        # Write the Contents.json file
        with open(contents_json_path, 'w') as json_file:
            json.dump(contents_json, json_file, indent=4)

        # Add to the enum cases
        icon_cases.append(f'case {camel_case_name} = "{snake_case_base_name}"')

    print(f".xcassets folder created at: {os.path.abspath(xcassets_path)}")

    # Generate the Swift Enum if class name is provided
    if enum_class_name:
        generate_swift_enum(enum_class_name, icon_cases)


def generate_swift_enum(enum_class_name, cases):
    enum_template = """
    import UIKit

    enum %s: String {
    %s
    }
    """
    enum_cases = "\n".join([f"    {case}" for case in cases])
    enum_content = enum_template % (enum_class_name, enum_cases)

    with open(f"{enum_class_name}.swift", "w") as swift_file:
        swift_file.write(enum_content)

    print(f"{enum_class_name}.swift file created with the following content:")
    print(enum_content)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Create .xcassets folder structure for an Xcode project",
        epilog="Example usage:\n  python create_xcassets.py -n MyIcon -i /path/to/images_folder -s SubfolderName --enum Icons",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("-n", "--name", required=True,
                        help="The name of the asset to create (will be converted to snake case)")
    parser.add_argument("-i", "--images_folder", required=True, help="The folder containing the images")
    parser.add_argument("-s", "--subfolder", help="The name of the subfolder to create inside the .xcassets folder")
    parser.add_argument("--enum", help="The name of the Swift enum class to create")

    args = parser.parse_args()

    create_xcassets(args.name, args.images_folder, args.subfolder, args.enum)