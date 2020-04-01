class Product:
    def __init__(self, code: int, description: str, price: float):
        self.__code = code
        self.__desc = description
        self.__price = price

    def print(self):
        print(self.__code)
        print(self.__desc)
        print(self.__price)

    def print_inline(self):
        print('{0} - {1} - {2:.2f}'.format(self.__code, self.__desc, self.__price))

    def get_code(self):
        return self.__code
