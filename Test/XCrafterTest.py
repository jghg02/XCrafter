import unittest
from unittest.mock import patch, mock_open, MagicMock
import os
import json

from XCrafter import to_snake_case, to_camel_case, create_xcassets, generate_swift_enum

class TestXcassetsCreator(unittest.TestCase):

    def test_to_snake_case(self):
        self.assertEqual(to_snake_case("MyTestString"), "my_test_string")
        self.assertEqual(to_snake_case("My-Test-String"), "my_test_string")
        self.assertEqual(to_snake_case("My  Test  String"), "my_test_string")
        self.assertEqual(to_snake_case("My_Test__String"), "my_test_string")

    def test_to_camel_case(self):
        self.assertEqual(to_camel_case("my_test_string"), "myTestString")

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.join')
    @patch('os.makedirs')
    def test_generate_swift_enum(self, mock_makedirs, mock_path_join, mock_open):
        enum_class_name = "Icons"
        cases = ["case icon1 = \"icon1\"", "case icon2 = \"icon2\""]
        output_folder = "/mock/output_folder"

        generate_swift_enum(enum_class_name, cases, output_folder)

        # Check that Swift file was written
        swift_file_path = os.path.join(output_folder, f"{enum_class_name}.swift")
        mock_open.assert_called_with(swift_file_path, 'w')

        # Validate the content of the Swift file
        expected_content = """
    import UIKit

    public enum Icons: String, CaseIterable {
        case icon1 = "icon1"
        case icon2 = "icon2"

        static var allIcons: [Icons] {
            return Icons.allCases
        }

        var iconName: String {
            return rawValue
        }
    }
    """
        handle = mock_open()
        handle().write.assert_called_with(expected_content.strip())



if __name__ == '__main__':
    unittest.main()