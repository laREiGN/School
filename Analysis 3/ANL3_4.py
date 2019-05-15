class Product:
    product_name = None
    product_id = None
    product_price = None

    def __init__(self, name, product_id, price):
        self.product_name = name
        self.product_id = product_id
        self.product_price = price

    def product_information(self):
        print(self.product_name, self.product_id, self.product_price)
        self.product_list()

    def product_list(self):
        current_product = [self.product_name, self.product_id, self.product_price]
        print(current_product)

p1 = Product('Nintendo', '12345', '14.99')
p2 = Product('Computer', '1337', '200,00')

p1.product_information()
p2.product_information()
