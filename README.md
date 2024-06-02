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
git clone https://github.com/yourusername/xcassets-creator.git
cd xcassets-creator
```

2. Ensure you have Python 3 installed on your machine.

## Usage

The script provides several options to customize the creation of the .xcassets folder and the Swift enum.

Command-line Arguments

	• -n, --name: (Required) The name of the asset to create (will be converted to snake case).
	• -i, --images_folder: (Required) The folder containing the images.
	• -s, --subfolder: The name of the subfolder to create inside the .xcassets folder.
	• --enum: The name of the Swift enum class to create. If not provided, the enum will not be generated.


## Example Usage

1.	Create an .xcassets folder named MyIcon.xcassets with images from the specified folder:
```sh
python XCrafter.py -n MyIcon -i /path/to/images_folder
```

2. Create an .xcassets folder named MyIcon.xcassets with images from the specified folder and create a subfolder inside .xcassets:
```sh
python XCrafter.py -n MyIcon -i /path/to/images_folder -s MySubfolder
```

3. Create an .xcassets folder and generate a Swift enum named Icons:
```sh
python XCrafter.py -n MyIcon -i /path/to/images_folder --enum Icons
```

4. Create an .xcassets folder, create a subfolder inside .xcassets, and generate a Swift enum:
```sh
python XCrafter.py -n MyIcon -i /path/to/images_folder -s MySubfolder --enum Icons
```


## Generated Swift Enum

If the --enum parameter is provided, the script generates a Swift enum with cases for each image base name. The enum case names are in camel case, while the raw values are in snake case.

Example

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

