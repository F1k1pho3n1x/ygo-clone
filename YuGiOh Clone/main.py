class TestClass:
    number: int = 0
    text: str = "N/a"
    list_of_numbers: list[tuple[int, int]] = []

    def __init__(self, number = 0, text = "N/a", list_numbers = []):
        self.number = number
        self.text = text
        self.list_of_numbers = list_numbers

    def __str__(self):
        return f"{self.number} {self.text} {len(self.list_of_numbers)}\n"

my_obj = TestClass()
print(my_obj)
my_obj2 = TestClass(10, "Hello!", [(2,1), (3,5)])
print(my_obj2)

