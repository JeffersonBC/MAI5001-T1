from product import Product
from typing import List


class StaticList:
    __MAX = 100000

    def __init__(self):
        self.__list: List[Product or None] = [None] * self.__MAX
        self.__count = 0

    def insert(self, item: Product):
        if self.__count < self.__MAX and item.get_code() in range(0, 10000):
            self.__list[self.__count] = item
            self.__count += 1
            print('Ok')

        else:
            print('Erro')

    def ordered_insert(self, item: Product):
        if self.__count < self.__MAX:
            for i in range(self.__count):
                if self.__list[i].get_code() == item.get_code():
                    print('Duplicado')
                    return

                elif self.__list[i].get_code() > item.get_code():
                    for j in range(self.__count, i, -1):
                        self.__list[j + 1] = self.__list[j]

                    self.__list[i] = item
                    self.__count += 1
                    print('Ok')
                    return

        print('Erro')

    def remove(self, code: int):
        for i in range(self.__count):
            if self.__list[i].get_code() == code:
                for j in range(i + 1, self.__count):
                    self.__list[j - 1] = self.__list[j]

                self.__count -= 1
                print('Ok')

        print('Erro')

    def query(self, code: int):
        for i in range(self.__count):
            if self.__list[i].get_code() == code:
                print('Ok')
                self.__list[i].print()
                return

        print('Erro')

    def list_products(self):
        for i in range(self.__count):
            self.__list[i].print_inline()
