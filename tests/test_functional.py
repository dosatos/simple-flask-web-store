import unittest
import requests


class TestProductsPage(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_can_open_list_of_products_page(self):
        url = "http://127.0.0.1:5000/products/"
        request = requests.get(url)
        html = request.content.decode("utf8").lower()
        self.assertIn("<p> #1: computer </p>", html)
        self.assertIn("<p> #2: smartphone </p>", html)
        self.assertIn("<p> #3: watches </p>", html)


class TestSingleProductPage(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_can_open_page_with_computer(self):
        url = "http://127.0.0.1:5000/products/1"
        request = requests.get(url)
        html = request.content.decode("utf8").lower()
        self.assertIn("computer", html)

    def test_can_open_page_with_smartphone(self):
        url = "http://127.0.0.1:5000/products/2"
        request = requests.get(url)
        html = request.content.decode("utf8").lower()
        self.assertIn("smartphone", html)

    def test_can_open_page_with_watches(self):
        url = "http://127.0.0.1:5000/products/3"
        request = requests.get(url)
        html = request.content.decode("utf8").lower()
        self.assertIn("watches", html)


if __name__ == "__main__":
    unittest.main()
