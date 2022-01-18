import variable
import sqlite3

class SearchPaymentMethod:
    def __init__(self) -> None:
        """search for different payment methods"""
        self.ids = []

    def by_name(self, name: str):
        """search for special name in the table"""

        data = sqlite3.connect('data.db')
        cur = data.cursor()
        cur.execute(f"""SELECT id FROM payment_methods
                                WHERE name = "{name}";
        """)
        self.ids.append(list(map(lambda x: x[0], cur.fetchall())))
        data.close()

    def by_number(self, number: str):
        """search for special number in the table"""

        data = sqlite3.connect('data.db')
        cur = data.cursor()
        cur.execute(f"""SELECT id FROM payment_methods
                                WHERE number = "{number}";
        """)
        self.ids.append(list(map(lambda x: x[0], cur.fetchall())))
        data.close()
    
    def by_id(self, id: int) -> None:
        """search for special id in the table"""

        data = sqlite3.connect('data.db')
        cur = data.cursor()
        cur.execute(f"""SELECT id FROM payment_methods
                                WHERE id = "{id}";
        """)
        self.ids.append(list(map(lambda x: x[0], cur.fetchall())))
        data.close()

    def transport(self) -> tuple:
        """intersections ids and return the ids that exist in all list"""
        temp = set(self.ids[0])
        for i in self.ids:
            temp = temp.intersection(set(i))
        return tuple(temp)
    
    def make_object(self, data: tuple) -> list:
        """make objects from ids and return the list of objects"""
        ans = []
        for i in data:
            temp = variable.PaymentMethod(i[1], i[2])
            temp.id = i[0]
            temp.added = 1
            ans.append(temp)
        return ans

    def run(self) -> list:
        """do the main job and return the answer as a list of objects"""
        ids = self.transport()
        if(len(ids) == 1):
            ids = '(' + str(ids[0]) + ')'
    
        data = sqlite3.connect('data.db')
        cur = data.cursor()
        cur.execute(f"""SELECT * FROM payment_methods
                                WHERE id IN {ids};
        """)
        ans = self.make_object(cur.fetchall())
        data.close()
        return ans

if __name__ == "__main__":
    pay = SearchPaymentMethod()
    pay.by_name("visa card")
    pay.by_number("64")
    for i in pay.run():
        print(i.id, i.name, i.number)