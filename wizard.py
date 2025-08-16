from classes import Student

class Senior(Student):
    def __init__(self, name, course, house):
        self.course = course
        super().__init__(name, house)



class Pupil(Student):
    def __init__(self,name,house,sport):
        self.sport = sport
        super().__init__(name,house)

    def __str__(self):
        return f"{self.name} is in {self.house} House playing {self.sport}"
        
    @classmethod
    def fetch(cls):
        name = input("Name: ") 
        house = input("House: ")
        sport =input("Sport: ")
        return cls(name, house, sport)


def main():
    Isha = Pupil.fetch()
    print(Isha)

if __name__ == "__main__":
    main()