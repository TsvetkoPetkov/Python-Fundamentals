class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product_name):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        result_list = [product for product in self.products if product[0] == first_letter]
        return result_list

    def __repr__(self):
        output = f"Items in the {self.name} catalogue:"

        for el in sorted(self.products):
            output += "\n" + el

        return output


catalogue = Catalogue("Furniture")

catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
