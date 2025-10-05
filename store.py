class OutofStockError(Exception):
    """custom exception to indicate that an item is out of stock"""

    def __init__(self, item_id):
        self.item_id = item_id
        super().__init__(f"Item with ID {item_id} is out of stock.")

    def __str__(self):
        return f"Sorry, the item {self.item_id} is out of stock."


product_inventory = {
    "Iphone X": 5,
    "Samsung Galaxy S21": 0,
    "Google Pixel 5": 3,
    "OnePlus 9": 2,
    "Sony Xperia 1": 4,
    "Nokia 3310": 0,
}


def purchase_item(item_id):
    try:
        if product_inventory[item_id] > 0:
            product_inventory[item_id] -= 1
            print(
                f"Successfully purchased {item_id}. Remaining stock: {product_inventory[item_id]}"
            )
        else:
            raise OutofStockError(item_id)
    except OutofStockError as e:
        print(e)
    except KeyError:
        print(f"The item {item_id} does not exist in the inventory.")


if __name__ == "__main__":
    purchase_item("Samsung Galaxy S21")
    purchase_item("Nokia 3310")
    purchase_item("Iphone X")
    purchase_item("NonExistentItem")
