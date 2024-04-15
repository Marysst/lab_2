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

    @patch('sys.stdout', new_callable=StringIO)
    def test_encoder_simple_output(self, mock_stdout):
        # Arrange
        input_text = "hello world"
        expected_output = "Encoded text is: uryyb jbeyq\n"
    
        # Act
        translation_table = create_translation_table()
        result = encoder(input_text, translation_table)
        stdout.write(f'Encoded text is: {result}\n')
    
        # Assert
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_encoder_output_special_characters(self, mock_stdout):
        # Arrange
        input_text = "hello, world!"
        expected_output = "Encoded text is: uryyb, jbeyq!\n"
    
        # Act
        translation_table = create_translation_table()
        result = encoder(input_text, translation_table)
        stdout.write(f'Encoded text is: {result}\n')
    
        # Assert
        self.assertEqual(mock_stdout.getvalue(), expected_output)
        
    @patch('sys.stdout', new_callable=StringIO)
    def test_encoder_output_empty_string(self, mock_stdout):
        # Arrange
        input_text = ""
        expected_output = "Encoded text is: \n"
    
        # Act
        translation_table = create_translation_table()
        result = encoder(input_text, translation_table)
        stdout.write(f'Encoded text is: {result}\n')
    
        # Assert
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_encoder_with_invalid_alphabet(self):
        # Arrange
        input_text = "hello фыЪ汉字"
        expected_error = 'String must contain only Latin alphabet characters\n'

        # Act & Assert
        with patch('sys.stdin', StringIO(input_text)):
            with patch('sys.stderr', new_callable=StringIO) as mock_stderr:
                self.assertRaises(ValueError, encoder)

                # Assert
                self.assertEqual(mock_stderr.getvalue(), expected_error)

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
