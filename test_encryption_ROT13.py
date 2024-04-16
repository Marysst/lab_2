from unittest import TestCase
from encryption_ROT13 import encoder

class TestEncoder(TestCase):
    def test_simple_string(self) -> None:
        # Arrange
        input_string = 'hello world'
        expected_output = 'Encoded text is: uryyb jbeyq'
        
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

        # Act & Assert
        with self.assertRaises(ValueError) as context:
            encoder(input_string)
        
        self.assertEqual(expected_output, context.exception.__str__())

    def test_empty_string(self) -> None:
        # Arrange
        input_string = ''
        expected_output = ''
        
        # Act
        encoded_string = encoder(input_string)
        
        # Assert
        self.assertEqual(expected_output, encoded_string)
    
    def test_encoder_with_correct_input(self):
        # Arrange
        input_text = "hello world"
        
        # Act & Assert
        with self.assertRaises(SystemExit) as cm:
            encoder(input_text)
        
            # Assert
            self.assertEqual(cm.exception.code, 0)
    
    def test_encoder_with_incorrect_input(self):
        # Arrange
        input_text = "hello фыЪ汉字"
        
        # Act & Assert
        with self.assertRaises(SystemExit) as cm:
                encoder(input_text)
    
                # Assert
                self.assertEqual(cm.exception.code, 1)

