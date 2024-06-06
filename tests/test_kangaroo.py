import unittest
from src.kangaroo import Kangaroo


class TestKangaroo(unittest.TestCase):
    def test_initialization(self):
        kangaroo = Kangaroo("kangaroo")
        self.assertEqual(kangaroo.pouch_contents, [])

    def test_kangaroo_str(self):
        kangaroo = Kangaroo("kangaroo")
        kangaroo.put_in_pouch("hello")
        kangaroo.put_in_pouch("world")
        print(kangaroo)

    def test_put_in_pouch(self):
        kanga = Kangaroo("kanga")
        roo = Kangaroo("roo")
        kanga.put_in_pouch(roo)
        print(kanga)


if __name__ == '__main__':
    unittest.main()
