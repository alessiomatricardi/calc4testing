from calc.calculator import calculator as c
import unittest

class TestAdd(unittest.TestCase):
    def test_add_integers_positive(self):
        result = c.sum(1, 2)
        self.assertEqual(result, 3)

    def test_add_integers_negative(self):
        result = c.sum(-1, -2)
        self.assertEqual(result, -3)

    def test_add_integers_pos_neg(self):
        result = c.sum(1, -2)
        self.assertEqual(result, -1)

    def test_add_integers_neg_pos(self):
        result = c.sum(-1, 2)
        self.assertEqual(result, 1)

    def test_divide_integers_positive(self):
        result = c.divide(6, 3)
        self.assertEqual(result, 2)

    def test_divide_integers_positive2(self):
        result = c.divide(7, 3)
        self.assertEqual(result, 2)

    def test_divide_integers_negative(self):
        result = c.divide(-6, -2)
        self.assertEqual(result, 3)

    def test_divide_integers_negative2(self):
        result = c.divide(-7, -2)
        self.assertEqual(result, 3)

    def test_divide_integers_pos_neg(self):
        result = c.divide(6, -2)
        self.assertEqual(result, -3)

    def test_divide_integers_pos_neg2(self):
        result = c.divide(9, -2)
        self.assertEqual(result, -4)

    def test_divide_integers_neg_pos(self):
        result = c.divide(-6, 2)
        self.assertEqual(result, -3)

    def test_divide_integers_neg_pos2(self):
        result = c.divide(-7, 2)
        self.assertEqual(result, -3)

    def test_divide_zero(self):
        result = c.divide(0, 2)
        self.assertEqual(result, 0)

    def test_divide_by_zero(self):
        self.assertRaises(ZeroDivisionError, c.divide, 6, 0)

    def test_multiply_int_pos(self):
        result = c.multiply(5, 7)
        self.assertEqual(result, 35)
    
    def test_multiply_int_pos_neg(self):
        result = c.multiply(5, -7)
        self.assertEqual(result, -35)

    def test_multiply_int_neg_pos(self):
        result = c.multiply(-5, 7)
        self.assertEqual(result, -35)

    def test_multiply_int_neg(self):
        result = c.multiply(-5, -7)
        self.assertEqual(result, 35)
    
    def test_sub_integers_positive(self):
            result = c.subtract(1, 2)
            self.assertEqual(result, -1)

    def test_sub_integers_negative(self):
        result = c.subtract(-1, -2)
        self.assertEqual(result, 1)

    def test_sub_integers_pos_neg(self):
        result = c.subtract(1, -2)
        self.assertEqual(result, 3)

    def test_sub_integers_neg_pos(self):
        result = c.subtract(-1, 2)
        self.assertEqual(result, -3)
        
if __name__ == "__main__":
    unittest.main()
