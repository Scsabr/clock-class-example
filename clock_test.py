# provided by chatGPT
import unittest
from clock import Clock

class TestClock(unittest.TestCase):
    
    def test_initialization(self):
        # Valid initialization
        clock = Clock(12, 30, 45)
        self.assertEqual(clock.hours, 12)
        self.assertEqual(clock.minutes, 30)
        self.assertEqual(clock.seconds, 45)
        
        # Edge cases for initialization
        with self.assertRaises(ValueError):
            Clock(25, 0, 0)  # Invalid hour
        with self.assertRaises(ValueError):
            Clock(12, 61, 0)  # Invalid minute
        with self.assertRaises(ValueError):
            Clock(12, 30, 61)  # Invalid second
    
    def test_set_hours(self):
        clock = Clock(0, 0, 0)
        clock.set_hours(23)
        self.assertEqual(clock.hours, 23)
        
        with self.assertRaises(ValueError):
            clock.set_hours(25)  # Invalid hour

    def test_set_minutes(self):
        clock = Clock(0, 0, 0)
        clock.set_minutes(59)
        self.assertEqual(clock.minutes, 59)
        
        with self.assertRaises(ValueError):
            clock.set_minutes(61)  # Invalid minute
    
    def test_set_seconds(self):
        clock = Clock(0, 0, 0)
        clock.set_seconds(59)
        self.assertEqual(clock.seconds, 59)
        
        with self.assertRaises(ValueError):
            clock.set_seconds(61)  # Invalid second

    def test_str_representation(self):
        clock = Clock(1, 2, 3)
        self.assertEqual(str(clock), "01:02:03")
        
        clock = Clock(12, 30, 45)
        self.assertEqual(str(clock), "12:30:45")
    
    def test_tick(self):
        # Test normal increment
        clock = Clock(0, 0, 0)
        clock.tick()
        self.assertEqual(str(clock), "00:00:01")
        
        # Test second wrap-around
        clock = Clock(0, 0, 59)
        clock.tick()
        self.assertEqual(str(clock), "00:01:00")
        
        # Test minute and second wrap-around
        clock = Clock(0, 59, 59)
        clock.tick()
        self.assertEqual(str(clock), "01:00:00")
        
        # Test hour, minute, and second wrap-around
        clock = Clock(23, 59, 59)
        clock.tick()
        self.assertEqual(str(clock), "00:00:00")

if __name__ == '__main__':
    unittest.main()
