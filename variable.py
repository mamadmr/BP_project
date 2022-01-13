"""
    in this file, we have some classes that use as a variable in the entire program 
    Expense       -> a class that each object contains a purchase
    Place         -> a class that each object contains a shop or a website or an organization
    Date          -> a class that each object contains a specific time which distinct by year, month, day, week day
    Person        -> a class that each object contains a family member
    PaymentMethod -> a class that each object contains a way to pay for purchase for instance a bank name   
"""

import datetime
import sqlite3
import database_maker

class Place:
    def __init__(self, name: str, distance: int, address: str) -> None:
        """
            the place could be a website or a shop or an organization 
            if the place is website put 0 as distance
            if the variable added is equal to one then means this place added to data base 
        """
        self.name = name
        self.distance = distance
        self.address = address
        self.added = 0
        self.id = -1

    def add_to_database(self)-> None:
        """just to add the object to database if it didn't add to database"""
        if self.added:
            return
        self.added = 1
        data = sqlite3.connect('data.db')
        cur = data.cursor()
        cur.execute(f"""
        INSERT INTO places(name, address, distance)
        VALUES("{self.name}", "{self.address}",{self.distance});
        """)

        self.id = cur.lastrowid
        data.commit()
        data.close()
    
    def remove_from_database(self):
        """remove the object from data base"""
        if self.added == 0:
            return

        data = sqlite3.connect('data.db')
        cur = data.cursor()
        cur.execute(f"""DELETE FROM places
                        WHERE id = {self.id}
        """)
        self.add = 0
        self.id = -1
        data.commit()
        data.close()

class Date:
    def __init__(self, year: int, month: int, day: int) -> None:
        """objects are dates respect to year month and day """
        self.year = year
        self.month = month
        self.day = day
        self.added = 0
        self._compute_week_day()
        self.id = -1
    
    def _compute_week_day(self) -> None:
        """to compute week day of the date """
        intDay = datetime.date(year=self.year, month=self.month, day=self.day).weekday()
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        self.week_day = days[intDay]

    def show(self) -> tuple:
        """return year/month/day hour:minute weekday"""
        return f"{self.year}/{self.month}/{self.day}", self.week_day


    def add_to_database(self)-> None:
        """just to add the object to database"""
        if self.added:
            return
        self.added = 1
        data = sqlite3.connect('data.db')
        cur = data.cursor()
        cur.execute(f"""
            INSERT INTO dates(year, month, day, weekday)
            VALUES({self.year}, {self.month},{self.day}, "{self.week_day}");
        """)

        self.id = cur.lastrowid
        data.commit()
        data.close()
    
    def remove_from_database(self):
        """remove the object from data base"""
        if self.added == 0:
            return

        data = sqlite3.connect('data.db')
        cur = data.cursor()
        cur.execute(f"""DELETE FROM dates
                        WHERE id = {self.id}
        """)
        self.add = 0
        self.id = -1
        data.commit()
        data.close()

class Person:
    def __init__(self, name: str, age: int, gender: str) -> None:
        """each object is a person who can buy things"""
        self.name = name
        self.age = age
        self.gender = gender
        self.added = 0
        self.id = -1

    def add_to_database(self)-> None:
        """just to add the object to database"""
        if self.added:
            return
        self.added = 1
        data = sqlite3.connect('data.db')
        cur = data.cursor()
        cur.execute(f"""
            INSERT INTO persons(name, age, gender)
            VALUES("{self.name}", {self.age}, "{self.gender}");
        """)
        self.id = cur.lastrowid
        data.commit()
        data.close()
    
    def remove_from_database(self):
        """remove the object from data base"""
        if self.added == 0:
            return

        data = sqlite3.connect('data.db')
        cur = data.cursor()
        cur.execute(f"""DELETE FROM persons
                        WHERE id = {self.id}
        """)
        self.add = 0
        self.id = -1
        data.commit()
        data.close()

class PaymentMethod:
    def __init__(self, name: str, number:str) -> None:
        """if the payment method doesn't have any number, use "0000" as number"""
        self.name = name
        self.number = number
        self.added = 0
        self.id = -1

    def add_to_database(self)-> None:
        """just to add the object to database"""
        self.added = 1
        data = sqlite3.connect('data.db')
        cur = data.cursor()
        cur.execute(f"""
            INSERT INTO payment_methods(name, number)
            VALUES("{self.name}", "{self.number}");
        """)

        self.id = cur.lastrowid
        data.commit()
        data.close()
    
    def remove_from_database(self):
        """remove the object from data base"""
        if self.added == 0:
            return

        data = sqlite3.connect('data.db')
        cur = data.cursor()
        cur.execute(f"""DELETE FROM payment_methods
                        WHERE id = {self.id}
        """)
        self.add = 0
        self.id = -1
        data.commit()
        data.close()

class Expense:
    def __init__(self, amount: int, place: Place, date: Date, explanation: str,
                 person: Person, payment_method: PaymentMethod, discount: int)  -> None:
        self.amount = amount
        self.place = place
        self.date = date
        self.explanation = explanation
        self.person = person
        self.payment_method = payment_method
        self.discount = discount
        self.added = 0
        self.id = -1

    def add_to_database(self)-> None:
        """just to add the object to database"""
        if self.added:
            return
        self.added = 1
        data = sqlite3.connect('data.db')
        cur = data.cursor()
        cur.execute(f"""
            INSERT INTO expenses(amount, explanation, discount, place, date, person, payment_method)
            VALUES({self.amount}, "{self.explanation}", {self.discount}
            , {self.place.id}, {self.date.id}, {self.person.id}, {self.payment_method.id});
        """)
        self.id = cur.lastrowid
        data.commit()
        data.close()
    
    def remove_from_database(self):
        """remove the object from data base"""
        if self.added == 0:
            return

        data = sqlite3.connect('data.db')
        cur = data.cursor()
        cur.execute(f"""DELETE FROM expenses
                        WHERE id = {self.id}
        """)
        self.add = 0
        self.id = -1
        data.commit()
        data.close()

if __name__ == "__main__":
    database_maker.run()

    date = Date(2022, 1, 2)
    date.add_to_database()

    amount = 1000
    explanation = 'buy some pens and notebooks'
    discount = 0

    place = Place("Amazon", 0, 'www.amazon.de')
    place.add_to_database()

    person = Person("Mohammad Mahdi Reisi", 10, 'male')
    person.add_to_database()

    payment_method = PaymentMethod("visa card", '1234-5678-1234-1234')
    payment_method.add_to_database()

    expense = Expense(amount, place, date, explanation, person, payment_method, discount)
    expense.add_to_database()

    # place.remove_from_database()
    # date.remove_from_database()
    # person.remove_from_database()
    # payment_method.remove_from_database()
    # expense.remove_from_database()

