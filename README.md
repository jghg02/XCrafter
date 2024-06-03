# XCrafter


A Python script to create an `.xcassets` folder structure for an Xcode project. The script can process images, create image sets, and optionally generate a Swift enum to reference the assets.

## Features

- Convert image names to snake_case.
- Optionally create a subfolder inside the `.xcassets` folder.
- Group images by their base names and create image sets.
- Generate a `Contents.json` file for each image set.
- Optionally generate a Swift enum to reference the assets.

## Requirements

- Python 3.x

## Installation

1. Clone this repository or download the script.

```sh
git clone git@github.com:jghg02/XCrafter.git
cd XCrafter
```

2. Ensure you have Python 3 installed on your machine.

3. Execute the `setup.sh` script and then reload your terminal.

4. Ensure you could execute `xcrafter` in your terminal.

## Usage

The script provides several options to customize the creation of the .xcassets folder and the Swift enum.

Command-line Arguments

	• -n, --name: (Required) The name of the asset to create (will be converted to snake case).
	• -i, --images_folder: (Required) The folder containing the images.
	• -o, --output_folder: The output folder to save the .xcassets and Swift enum. By default the path are in your `Desktop`.
	• -s, --subfolder: The name of the subfolder to create inside the .xcassets folder.
	• --enum: The name of the Swift enum class to create. If not provided, the enum will not be generated.


## Example Usage

1.	Create an .xcassets folder named MyIcon.xcassets with images from the specified folder:
```sh
xcrafter -n MyIcon -i /path/to/images_folder
```

2. Create an .xcassets folder named MyIcon.xcassets with images from the specified folder and create a subfolder inside .xcassets:
```sh
xcrafter -n MyIcon -i /path/to/images_folder -s MySubfolder
```

3. Create an .xcassets folder and generate a Swift enum named Icons:
```sh
xcrafter -n MyIcon -i /path/to/images_folder --enum Icons
```

4. Create an .xcassets folder, create a subfolder inside .xcassets, and generate a Swift enum:
```sh
xcrafter -n MyIcon -i /path/to/images_folder -s MySubfolder --enum Icons
```

5. Create an .xcassets folder, create a subfolder inside .xcassets, generate a Swift enum and specify the output folder
```sh
xcrafter -n MyIcon -i /path/to/images_folder -s MySubfolder --enum Icons -o /your/path/here
```


## Generated Swift Enum

If the --enum parameter is provided, the script generates a Swift enum with cases for each image base name. The enum case names are in camel case, while the raw values are in snake case.

## Example

| Folder Images  | XCAssest  | 
|:------------- |:---------------:|
| ![CleanShot 2024-06-03 at 11 34 21@2x](https://github.com/nicklockwood/SwiftFormat/assets/1470487/e8c30fe4-cb46-459b-85ff-b885bb0f5f1c)  | ![CleanShot 2024-06-03 at 11 38 22@2x](https://github.com/nicklockwood/SwiftFormat/assets/1470487/28c9ff21-543f-4997-87b7-96b1486b6961)          |


For images ic_cog.svg and ic_undo_dos@2x.png, the generated enum would be:

```swift
import UIKit

public enum Icons: String, CaseIterable {
 case cog = "ic_cog"
 case undoDos = "ic_undo_dos"

 static var allIcons: [Icons] {
   return Icons.allCases
 }

 var iconName: String {
    return rawValue
 }
}
```

And then you can drag and drop into your Xcode project. 
