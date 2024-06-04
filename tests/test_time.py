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
        self.assertTrue(Time.is_after(t1, t2))

        t3 = Time(11, 3, 17)
        self.assertTrue(Time.is_after(t3, t2))
        self.assertFalse(Time.is_after(t2, t3))

    def test_time_to_int_to_time(self):
        t = Time(8, 54, 16)
        self.assertEqual(Time.time_to_int(t), 32056)
        self.assertEqual(Time.time_to_int(Time.int_to_time(32056)), 32056)


if __name__ == '__main__':
    unittest.main()
