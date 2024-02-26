import unittest
from dead_ant_counter import dead_ant_count

class TestDeadAntCount(unittest.TestCase):
    def test_multiple_occurrences_returns_1(self):
        # Arrange
        input = "ant ant …. a nt"
        expected = 1
        
        # Act
        result = dead_ant_count(input)
        
        # Assert
        self.assertEqual(result, expected)
    
    def test_empty_input_returns_0(self):
        # Arrange
        input = ""
        expected = 0
        
        # Act
        result = dead_ant_count(input)
        
        # Assert
        self.assertEqual(result, expected)
        
    def test_input_with_spaces_returns_0(self):
        # Arrange
        input = "  "
        expected = 0
        
        # Act
        result = dead_ant_count(input)
        
        # Assert
        self.assertEqual(result, expected)
        
    def test_varied_occurrences_returns_2(self):
        # Arrange
        input = "ant anantt aantnt"
        expected = 2
        
        # Act
        result = dead_ant_count(input)
        
        # Assert
        self.assertEqual(result, expected)
        
    def test_null_input_returns_0(self):
        # Arrange
        input = None
        expected = 0
        
        # Act
        result = dead_ant_count(input)
        
        # Assert
        self.assertEqual(result, expected)
        
    def test_ant_only_input_returns_0(self):
        # Arrange
        input = "ant ant ant ant"
        expected = 0
        
        # Act
        result = dead_ant_count(input)
        
        # Assert
        self.assertEqual(result, expected)
        
    def test_no_ant_input_returns_0(self):
        # Arrange
        input = "Prove"
        expected = 0
        
        # Act
        result = dead_ant_count(input)
        
        # Assert
        self.assertEqual(result, expected)

    def test_invalid_input_returns_1(self):
        # Arrange
        input = "ant_1%#...a….ant"
        expected = 1
        
        # Act
        result = dead_ant_count(input)
        
        # Assert
        self.assertEqual(result, expected)