class Student: 
    def __init__(self, name, house):
        if not name:
            raise ValueError("missing name")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house} house!"
    
    @classmethod
    def get(cls):
        name = input("Name: ") 
        house = input("House: ")
        return cls(name, house)


def main():
    student = Student.get()
    print(student)


if __name__ == "__main__":
    main() 