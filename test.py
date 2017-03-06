import unittest
from solutiontest import *


class PrimeNumbersTestCase(unittest.TestCase):
    def test_eight_not_in_list(self):
        result = primes(7)
        self.assertNotIn(8, result)

    def test_three_is_a_prime_number(self):
        result = primes(9)
        self.assertIn(3, result)

    def test_seventeen_is_in_the_result(self):
        result = primes(17)
        self.assertIn(17, result)

    def test_length_of_list_less_than_n(self):
        self.assertLess(len(primes(9)), 9)
   
    def test_ninety_seven_is_a_prime(self):
        result = primes(100)
        self.assertIn(97, result)

    def test_sixty_one_is_a_prime(self):
        result = primes(97)
        self.assertIn(61, result)
    def test_output_is_a_list(self):
        result = primes(43)
        result = isinstance(result, list)
        self.assertTrue(result)

    def test_return_empty_list_if_n_is_negative(self):
        result = primes(-7)
        self.assertListEqual([],result)

    def test_raise_error_if_input_is_not_integer(self):
    	with self.assertRaises(TypeError):
    		primes('string')


if __name__ == '__main__':
    unittest.main()

