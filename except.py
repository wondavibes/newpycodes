class ValuetooHigh(Exception):
    def __init__(self, value, limit):
        self.value = value
        self.limit = limit
        super().__init__(f"Value {value} exceeds the limit of {limit}.")

    def __str__(self):
        return f"Value {self.value} is too high; it should not exceed {self.limit}."


def check_value(value, limit=100):
    if value > limit:
        raise ValuetooHigh(value, limit)
    else:
        print(f"Value {value} is within the acceptable range.")


if __name__ == "__main__":
    try:
        check_value(150)
    except ValuetooHigh as e:
        print(e)
    try:
        check_value(50)
    except ValuetooHigh as e:
        print(e)
