from unittest import TestCase
from encryption_ROT13 import encoder, function_correct, function_incorrect
import subprocess

subprocess.run(['icacls encryption_ROT13.py /grant Everyone:F'], shell=True)

class TestEncoder(TestCase):
    def test_simple_string(self) -> None:
        # Arrange
        input_string = 'hello world'
        expected_output = 'uryyb jbeyq'
        
        # Act
        encoded_string = encoder(input_string)
        
        # Assert
        self.assertEqual(expected_output, encoded_string)

    def test_string_with_special_symbols(self) -> None:
        # Arrange
        input_string = '1hel-_lo2 ()world*!?'
        expected_output = '1ury-_yb2 ()jbeyq*!?'
        
        # Act
        encoded_string = encoder(input_string)
        
        # Assert
        self.assertEqual(expected_output, encoded_string)

    def test_string_with_wrong_alphabet(self) -> None:
        # Arrange
        input_string = 'hello фыЪ汉字'
        expected_output = 'String must contain only Latin alphabet, digits and special characters'

        # Act
        with self.assertRaises(ValueError) as context:
            encoder(input_string)
        
        # Assert
        self.assertEqual(expected_output, context.exception.__str__())

    def test_empty_string(self) -> None:
        # Arrange
        input_string = ''
        expected_output = ''
        
        # Act
        encoded_string = encoder(input_string)
        
        # Assert
        self.assertEqual(expected_output, encoded_string)

    def test_stdin_valid_input(self) -> None:
        # Arrange
        input_string = 'hello world'
        expected_output = 'Encoded text is: uryyb jbeyq\n\n'
        
        # Act
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            encoder(input_string)
        
        # Assert
        self.assertEqual(expected_output, mock_stdout.getvalue())

    def test_stdin_invalid_input(self) -> None:
        # Arrange
        input_text = 'hello фыЪ汉字'
        expected_output = 'String must contain only Latin alphabet, digits and special characters\n'
    
        # Act
        result = subprocess.run(['python3', 'encryption_ROT13.py'], input=input_text.encode(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
        # Assert
        self.assertTrue(result.stderr.decode('utf-8').startswith(expected_output))

    def test_function_correct_exit_code(self) -> None:
        with self.assertRaises(SystemExit) as cm:
            function_correct()
            self.assertEqual(cm.exception.code, 0)

    def test_function_incorrect_exit_code(self) -> None:
        with self.assertRaises(SystemExit) as cm:
            function_incorrect()
            self.assertEqual(cm.exception.code, 1)
