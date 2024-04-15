import unittest
from unittest.mock import patch
from io import StringIO
from sys import stdout
from another_implementation import encoder, function_correct, function_incorrect, create_translation_table

class TestAnotherImplementation(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_create_translation_table(self, mock_stdout):
        # Act
        translation_table = create_translation_table()

        # Assert
        self.assertIsNotNone(translation_table)

    def test_encoder_simple_string(self):
        # Arrange
        translation_table = create_translation_table()
        input_text = "Hello World!"
        expected_output = "Uryyb Jbeyq!"

        # Act
        encoded_text = encoder(input_text, translation_table)

        # Assert
        self.assertEqual(encoded_text, expected_output)

    def test_encoder_digits(self):
        # Arrange
        translation_table = create_translation_table()
        input_text = "12345"
        expected_output = "12345"

        # Act
        encoded_text = encoder(input_text, translation_table)

        # Assert
        self.assertEqual(encoded_text, expected_output)

    def test_encoder_special_characters(self):
        # Arrange
        translation_table = create_translation_table()
        input_text = "!@#$%^&*()"
        expected_output = "!@#$%^&*()"

        # Act
        encoded_text = encoder(input_text, translation_table)

        # Assert
        self.assertEqual(encoded_text, expected_output)

    def test_encoder_non_latin_characters(self):
        # Arrange
        translation_table = create_translation_table()
        input_text = "Привіт, світ!"
    
        # Act & Assert
        with self.assertRaises(ValueError):
            encoder(input_text, translation_table)

    def test_function_correct(self):
        # Arrange & Act
        with self.assertRaises(SystemExit) as cm:
            function_correct()

        # Assert
        self.assertEqual(cm.exception.code, 0)

    def test_function_incorrect(self):
        # Arrange & Act
        with self.assertRaises(SystemExit) as cm:
            function_incorrect()

        # Assert
        self.assertEqual(cm.exception.code, 1)

if __name__ == '__main__':
    unittest.main()
