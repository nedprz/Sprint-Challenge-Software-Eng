import unittest
from acme import Product
from acme_report import inventory_report , generate_products
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """ Test default product weight being 20. """
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)
    
    def test_stealability_and_explode(self):
        prod = Product(name = 'n' , price = 5 ,  weight=25, flammability=.4)
        """ Test flammability and stealability. """
        self.assertEqual(prod.flammability, .4)
        self.assertEqual(prod.stealability , 5 )
    
    def test_identifier(self):
        """ Test that identifier is in range """
        prod =Product('blah')
        self.assertTrue(1000000 <prod.identifier < 9999999)

class AcmeReportTests(unittest.TestCase):
    def test_default_num_products(self):
        a,b,c,d,length = inventory_report(generate_products())
        self.assertEqual(length ,30)

    def test_legal_names(self):
        self.assertIn()
        


if __name__ == '__main__':
    unittest.main()