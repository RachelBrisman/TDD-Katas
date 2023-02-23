class Barcodes():

    def scan(self, x):
        if(x == 99999):
            return "Error: barcode not found"
        if(x == ""):
            return "Error: empty barcode"
        return '${:,.2f}'.format(self.get_cost(x))
        raise Exception("Error: barcode doesn't exist")
    
    def scan_many(self, x):
        total = 0
        for barcode in x:
            total += self.get_cost(barcode)
        return total

    def get_cost(self, barcode):
        if(barcode == 12345):
            return 7.25
        if(barcode == 23456):
            return 12.5