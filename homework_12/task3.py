import unittest
import func 

class FuncTest(unittest.TestCase):

    def test_product(self):
        self.assertNotEqual(func.product(3.1, 4), 12)

    def test_encrypt(self):
        self.assertEqual(func.encrypt('Unit_test', 4), 'Yrmxcxiwx')

    def test_key_occur(self):
        self.assertEqual(func.key_occur('Hello Hello hi'), {'Hello' : 2, 'hi' : 1})
    
    def test_arithTask(self):
        self.assertIs(func.arithTask(2, 2, '+'), 4)
    
    def test_is_prime(self):
        self.assertTrue(func.is_prime(5))

if __name__ == '__main__':
    unittest.main()