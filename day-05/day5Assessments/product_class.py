class Product:
    def __init__(self, prod_id, prod_name, price):
        self.prod_id = prod_id
        self.prod_name = prod_name
        self.price = price

        # Validate product name length
        if len(prod_name) > 10:
            raise ValueError('Character length cannot be greater than 10')

    # Function to calculate total price
    def calc_tot_price(self):
        tot = self.price
        return tot

    # Function to calculate price including VAT (15%)
    def price_vat(self):
        vat = self.price * 0.15
        return self.price + vat


def main():
    product1 = Product("pr01", "Eno", 10)
    product2 = Product("pr02", "biscuit", 30)

    # Display product details
    print(product1.prod_id, product1.prod_name, product1.price)
    print(product2.prod_id, product2.prod_name, product2.price)

    # Calculate total price
    total = product1.calc_tot_price() + product2.calc_tot_price()
    print("Total price:", total)

    # Display prices including VAT
    print("Eno price including VAT:", product1.price_vat())
    print("Biscuit price including VAT:", product2.price_vat())


if __name__ == "__main__":
    main()