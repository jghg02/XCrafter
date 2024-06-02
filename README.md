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

	•	-n, --name: (Required) The name of the asset to create (will be converted to snake case).
	•	-i, --images_folder: (Required) The folder containing the images.
	•	-s, --subfolder: The name of the subfolder to create inside the .xcassets folder.
	•	--enum: The name of the Swift enum class to create. If not provided, the enum will not be generated.


## Generated Swift Enum

If the --enum parameter is provided, the script generates a Swift enum with cases for each image base name. The enum case names are in camel case, while the raw values are in snake case.

Example

For images ic_cog.svg and ic_undo_dos@2x.png, the generated enum would be:

```swift
import UIKit

enum Icons: String {
    case cog = "ic_cog"
    case undoDos = "ic_undo_dos"
}
```

