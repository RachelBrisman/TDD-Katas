# Create a simple app for scanning bar codes to sell products.

# Requirements
# 1. Barcode ‘12345’ should display price ‘$7.25’
# 2. Barcode ‘23456’ should display price ‘$12.50’
# 3. Barcode ‘99999’ should display ‘Error: barcode not found’
# 4. Empty barcode should display ‘Error: empty barcode’
# 5. Introduce a concept of total command where it is possible to scan multiple items. The command would display the sum of the scanned product prices

import unittest
from barcodes import Barcodes

class BarcodesTest(unittest.TestCase):

    def test_12345_returns_725(self):
        barcode = Barcodes()
        result = barcode.scan(12345)
        self.assertEqual(result, "$7.25")

    def test_23456_returns_(self):
        barcode = Barcodes()
        result = barcode.scan(23456)
        self.assertEqual(result, "$12.50")
        
    def test_9999_returns_barcode_not_found(self):
        barcode = Barcodes()
        result = barcode.scan(99999)
        self.assertEqual(result, "Error: barcode not found")

    def test_empty_returns_barcode_not_found(self):
        barcode = Barcodes()
        result = barcode.scan("")
        self.assertEqual(result, "Error: empty barcode")

    def test_other_input_returns_error(self):
        barcode = Barcodes()
        self.assertRaises(Exception, barcode.scan, 66)

    def test_scan_many_returns_sum(self):
        barcode = Barcodes()
        result = barcode.scan_many((23456, 12345, 12345))
        self.assertEqual(result, 27)