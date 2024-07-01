import unittest
from ver import verificar

class TestFuncoes(unittest.TestCase):

    def test_fizzbuzz(self):
        self.assertEqual(verificar(35), "FizzBuzz")

    def test_fizz(self):
        self.assertEqual(verificar(10), "Fizz")

    def test_buzz(self):
        self.assertEqual(verificar(14), "Buzz")

    def test_nao_divisivel(self):
        self.assertEqual(verificar(8), "miss")

if __name__ == '_main_':
    unittest.main()