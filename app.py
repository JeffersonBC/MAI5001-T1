from static_list import StaticList
from product import Product


class App:
    def __init__(self):
        self.s_list: StaticList = StaticList()

    def run(self):
        c: str = input()

        while c != 'F':
            if c == 'I':
                self.s_list.insert(
                    Product(int(input()), input(), float(input()))
                )

            elif c == 'O':
                self.s_list.ordered_insert(
                    Product(int(input()), input(), float(input()))
                )

            elif c == 'C':
                self.s_list.query(int(input()))

            elif c == 'R':
                self.s_list.remove(int(input()))

            elif c == 'L':
                self.s_list.list_products()

            else:
                print('Erro')

            c = input()

        print('Fim')
