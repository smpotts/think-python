import unittest
from src.time import Time


class TestTime(unittest.TestCase):

    def test_default_initialization(self):
        t = Time()
        self.assertEqual(t.hours, 0)
        self.assertEqual(t.minutes, 0)
        self.assertEqual(t.seconds, 0)

    def test_print_time(self):
        t = Time(9, 45, 2)
        self.assertEqual(t.print_time(), "09:45:02")

    def test_is_after(self):
        t1 = Time(9, 15, 12)
        t2 = Time(3, 28, 56)
        self.assertFalse(Time.is_after(t1, t2))


if __name__ == '__main__':
    unittest.main()
