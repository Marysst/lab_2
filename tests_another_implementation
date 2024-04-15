from unittest import TestCase
from unittest.mock import patch
from io import StringIO
import sys
from another_implementation import encoder, function_correct, function_incorrect, create_translation_table

class TestAnotherImplementation(TestCase):
    @patch('sys.stdout', new_callable=StringIO)
      def test_create_translation_table(self):
        # Act
        translation_table = create_translation_table()

        # Assert
        self.assertIsNotNone(translation_table)

    def test_encoder_output(self, mock_stdout):
        # Arrange
        input_text = "hello world"
        expected_output = "Encoded text is: uryyb jbeyq\n"

        # Act
        with patch('sys.stdin', StringIO(input_text)):
            encoder()

        # Assert
        self.assertEqual(mock_stdout.getvalue(), expected_output)

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
