class BinaryTree:
    """
    Instance of Class contains codes of the products and their prices
    in binary tree. Constructor creates a node with data.
    Method 'insert' sorts input data by product codes and
    inserts it into the tree in a form of a node.
    Method 'get_price' returns price of a product,
    which is searched by product code, or None
    if a product with such a code doesn't exist.
    """
    product_code = None
    price = 0
    left = right = None

    def __init__(self, product, prc):
        if not isinstance(product, int) or not isinstance(prc, (int, float)):
            raise TypeError("Invalid type of data was entered.")
        self.product_code = product
        self.price = prc

    def insert(self, product, prc):
        if not isinstance(product, int) or not isinstance(prc, (int, float)):
            raise TypeError("Invalid type of data was entered.")
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

    def get_price(self, product):
        if not isinstance(product, int):
            raise TypeError("Invalid type of data was entered.")
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


def main():
    price_tree = BinaryTree(1, 10)
    try:
        price_tree.get_price('2')
    except TypeError as e:
        print(e)
    price_tree.insert(2, 25)
    try:
        price_tree.insert('2', 5)
    except TypeError as e:
        print(e)
    try:
        price_tree.insert(2, '5')
    except TypeError as e:
        print(e)
    while True:
        inp = input("Enter ProductCode: ")
        if inp.isdigit():
            if price_tree.get_price(int(inp)) is not None:
                break
            else:
                print("This product code does not exist.\n")  #, end="")
        else:
            print("Wrong input!\n")
    while True:
        quantity = input("Enter Quantity: ")
        if quantity.isdigit():
            break
        print("Wrong input!\n")
    print(f"Price of product: {price_tree.get_price(int(inp))}\n" +
          f"Cost of all products: {price_tree.get_price(int(inp)) * int(quantity)}")


main()
