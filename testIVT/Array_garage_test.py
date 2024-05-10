import unittest
import sys

sys.path.insert(1, '../')  # Including the parent directory to the path so that the module can be imported

from algorithms.arrays.garage import garage  # Import the garage function directly

class TestGarage(unittest.TestCase):

    def test_garage(self):
        initial_state = [1, 2, 3, 0, 4]
        final_state = [0, 3, 2, 1, 4]
        expected_steps = 4
        expected_sequence = [
            [0, 2, 3, 1, 4],
            [2, 0, 3, 1, 4],
            [2, 3, 0, 1, 4],
            [0, 3, 2, 1, 4]
        ]
        
        steps, sequence = garage(initial_state, final_state)
        
        self.assertEqual(steps, expected_steps)
        self.assertEqual(sequence, expected_sequence)
        
    def test_garage_no_movement_needed(self):
        initial_state = [0, 1, 2, 3, 4]
        final_state = [0, 1, 2, 3, 4]
        expected_steps = 0
        expected_sequence = []
    
        steps, sequence = garage(initial_state, final_state)
    
        self.assertEqual(steps, expected_steps)
        self.assertEqual(sequence, expected_sequence)


if __name__ == '__main__':
    unittest.main()