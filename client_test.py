import unittest
from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """


  """ ------------ Add more unit tests ------------ """



if __name__ == '__main__':
    unittest.main()


class TestYourFuction(unittest.TestCase):
  def test_divide_by_zero(self):
    # Test of when price_b is 0
    price_a = 5
    price_b = 0
    self.assertIsNone(getRatio(price_a, price_b))

  def test_a_is_zero(self):
    # Test of when price_a is 0
    price_a = 0
    price_b = 10
    self.assertEqual(getRatio(price_a, price_b), 0)

  def normal_case(self):
    # When neither inputs are 0 and both are integers
    price_a = 300
    price_b = 30
    self.assertEqual(getRatio(price_a, price_b), 10)

  def float_variable_a(self):
    # When neither inputs are 0 and price_a is a float
    price_a = 12.5
    price_b = 10
    self.assertEqual(getRatio(price_a, price_b), 1.25)