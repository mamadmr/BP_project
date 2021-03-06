from numpy import var
import variable
import sqlite3 
import search_place
import search_persons
import search_payment_methods
import search_date

class SearchExpense:
    def __init__(self) -> None:
        """to search for different expense with different methods"""
        self.ids = []
    
    def by_amount(self, amount_down: int=0, amount_up: int=1e100) -> None:
        """search for different amount between amount_down and amount_up"""

        data = sqlite3.connect('data.db')
        cur = data.cursor()
        cur.execute(f"""SELECT id FROM expenses
                                WHERE {amount_down} <= amount
                                AND {amount_up} >= amount;
        """)
        self.ids.append(list(map(lambda x: x[0], cur.fetchall())))
        data.close()

    def by_discount(self, discount_down: int=0, discount_up: int=1e100) -> None:
        """search for different discount between discount_down and discount_up"""

        data = sqlite3.connect('data.db')
        cur = data.cursor()
        cur.execute(f"""SELECT id FROM expenses
                                WHERE {discount_down} <= discount
                                AND {discount_up} >= discount;
        """)
        self.ids.append(list(map(lambda x: x[0], cur.fetchall())))
        data.close()

    def by_place(self, places: list) -> None:
        """search for different expense that bought in these places"""
        ids = tuple([i.id for i in places])
        if len(ids) == 1:
            ids = '(' + str(ids[0]) + ')'
        
        data = sqlite3.connect('data.db')
        cur = data.cursor()
        cur.execute(f"""SELECT * FROM expenses
                                WHERE place IN {ids};
        """)

        self.ids.append(list(map(lambda x: x[0], cur.fetchall())))
        data.close()
    
    def by_person(self, persons: list) -> None:
        """search for expenses these peoples bought them"""
        ids = tuple([i.id for i in persons])
        if len(ids) == 1:
            ids = '(' + str(ids[0]) + ')'
        
        data = sqlite3.connect('data.db')
        cur = data.cursor()
        cur.execute(f"""SELECT * FROM expenses
                                WHERE person IN {ids};
        """)

        self.ids.append(list(map(lambda x: x[0], cur.fetchall())))
        data.close()

    def by_date(self, dates: list) -> None:
        """search for expenses that bought in these dates """
        ids = tuple([i.id for i in dates])
        if len(ids) == 1:
            ids = '(' + str(ids[0]) + ')'
        
        data = sqlite3.connect('data.db')
        cur = data.cursor()
        cur.execute(f"""SELECT * FROM expenses
                                WHERE date IN {ids};
        """)

        self.ids.append(list(map(lambda x: x[0], cur.fetchall())))
        data.close()
    
    def by_payment_method(self, payment_methods: list) -> None:
        """search for the expense that payed in this payment methodes"""
        ids = tuple([i.id for i in payment_methods])
        if len(ids) == 1:
            ids = '(' + str(ids[0]) + ')'
        
        data = sqlite3.connect('data.db')
        cur = data.cursor()
        cur.execute(f"""SELECT * FROM expenses
                                WHERE payment_method IN {ids};
        """)

        self.ids.append(list(map(lambda x: x[0], cur.fetchall())))
        data.close()

    def transport(self) -> tuple:
        """intersections ids and return the ids that exist in all list"""
        if len(self.ids) == 0:
            return ()
        temp = set(self.ids[0])
        for i in self.ids:
            temp = temp.intersection(set(i))
        return tuple(temp)

    def make_object(self, data: tuple) -> list:
        """make person objects from ids and return the list of objects"""
        ans = []
        for i in data:
            sch = search_persons.SearchPerson()
            sch.by_id(i[6])
            person_obj = sch.run()[0]
            
            sch = search_payment_methods.SearchPaymentMethod()
            sch.by_id(i[7])
            payment_opj = sch.run()[0]

            sch = search_date.SearchDate()
            sch.by_id(i[5])
            date_obj = sch.run()[0]

            sch = search_place.SearchPlace()
            sch.by_id(i[4])
            place_obj = sch.run()[0]

            temp = variable.Expense(i[1], place_obj, date_obj, i[2], person_obj, payment_opj, i[3])

            temp.id = i[0]
            temp.added = 1
            ans.append(temp)
        return ans

    def run(self) -> list: 
        """do the main job and return the answer as a list of objects"""
        self.by_discount()
        ids = self.transport()
        if len(ids) == 0:
            return []

        if(len(ids) == 1):
            ids = '(' + str(ids[0]) + ')'
        data = sqlite3.connect('data.db')
        cur = data.cursor()
        cur.execute(f"""SELECT * FROM expenses
                                WHERE id IN {ids};
        """)
        ans = self.make_object(cur.fetchall())
        data.close()
        return ans
    
if __name__ == "__main__":
    temp = SearchExpense()
#    temp.by_amount(4500, 10000)
#    temp.by_discount(18, 100)
#    places = search_place.SearchPlace()
#    places.by_name("Amazon")
#    temp.by_place(places.run())
#    person = search_persons.SearchPerson()
#    person.by_name("Mohammad Mahdi Reisi")
#    temp.by_person(person.run())
#    date = search_date.SearchDate()
#    date.by_date(date_down= variable.Date(2022, 1, 1))
#    temp.by_date(date.run())
    payment = search_payment_methods.SearchPaymentMethod()
    payment.by_number('1234567812341234')
    temp.by_payment_method(payment.run())

    for i in temp.run():
        print(i.explanation)