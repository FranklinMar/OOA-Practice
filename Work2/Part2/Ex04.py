class BinaryTree:
    product_code = None
    price = 0
    left = right = None

    def __init__(self, product, prc):
        if isinstance(product, int) and isinstance(prc, int):
            self.product_code = product
            self.price = prc
        else:
            raise TypeError("Invalid type of data was entered.")

    def insert(self, product, prc):
        if isinstance(product, int) and isinstance(prc, int):
            if self.product_code == product:
                return
            if self.product_code > product:
                if self.left is None:
                    self.left = BinaryTree(product, prc)
                else:
                    self.left.insert(product, prc)
                return
            if self.right is None:
                self.right = BinaryTree(product, prc)
            else:
                self.right.insert(product, prc)
        else:
            raise TypeError("Invalid type of data was entered.")

    def get_price(self, product):
        if isinstance(product, int):
            if self.product_code == product:
                return self.price
            elif self.product_code > product:
                if self.left is None:
                    return None
                else:
                    return self.left.get_price(product)
            else:
                if self.right is None:
                    return None
                else:
                    return self.right.get_price(product)
        else:
            raise TypeError("Invalid type of data was entered.")


def main():
    price_tree = BinaryTree(1, 10)
    try:
        price_tree.get_price('2')
    except TypeError as e:
        print("Yes")
    price_tree.insert(2, 25)
    try:
        price_tree.insert('2', 5)
    except TypeError as e:
        print("Yes")
    try:
        price_tree.insert(2, '5')
    except TypeError as e:
        print("Yes\n")
    
    while True:
        inp = input("Enter ProductCode: ")
        if inp.isdigit():
            if price_tree.get_price(int(inp)) is not None:
                break
            else:
                print("This product code does not exist.", end="")
        print("Wrong input!\n")
    while True:
        quantity = input("Enter Quantity: ")
        if quantity.isdigit() and eval(quantity) >= 0:
            break
        print("Wrong input!\n")

    print(f"Price of product: {price_tree.get_price(int(inp))}\n" +
          f"Cost of all products: {price_tree.get_price(int(inp)) * int(quantity)}")


main()
