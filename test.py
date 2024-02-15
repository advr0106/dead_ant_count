import unittest
from dead_ant_counter import dead_ant_count

class TestDeadAntCount(unittest.TestCase):
    def test_multiple_occurrences(self):
        # Arrange
        input = "ant ant …. a nt"
        expected = 1
        
        # Act
        result = dead_ant_count(input)
        
        # Assert
        self.assertEqual(result, expected)
    
    def test_empty_input(self):
        # Arrange
        input = ""
        expected = 0
        
        # Act
        result = dead_ant_count(input)
        
        # Assert
        self.assertEqual(result, expected)
        
    def test_input_with_spaces(self):
        # Arrange
        input = "  "
        expected = 0
        
        # Act
        result = dead_ant_count(input)
        
        # Assert
        self.assertEqual(result, expected)
        
    def test_varied_occurrences(self):
        # Arrange
        input = "ant anantt aantnt"
        expected = 2
        
        # Act
        result = dead_ant_count(input)
        
        # Assert
        self.assertEqual(result, expected)
        
    def test_null_input(self):
        # Arrange
        input = None
        expected = 0
        
        # Act
        result = dead_ant_count(input)
        
        # Assert
        self.assertEqual(result, expected)
        
    def test_ant_only_input(self):
        # Arrange
        input = "ant ant ant ant"
        expected = 0
        
        # Act
        result = dead_ant_count(input)
        
        # Assert
        self.assertEqual(result, expected)
        
    def test_no_ant_input(self):
        # Arrange
        input = "Prove"
        expected = 0
        
        # Act
        result = dead_ant_count(input)
        
        # Assert
        self.assertEqual(result, expected)

    def test_invalid_input(self):
        # Arrange
        input = "ant_1%#...a….ant"
        expected = 1
        
        # Act
        result = dead_ant_count(input)
        
        # Assert
        self.assertEqual(result, expected)