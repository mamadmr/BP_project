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


class Place:
    def __init__(self, name: str, distance: int, address: str) -> None:
        """
            the place could be a website or a shop or an organization 
            if the place is website put 0 as distance
        """
        self.name = name
        self.distance = distance
        self.address = address
        self.added = 0

    def add_to_database(self)-> None:
        """just to add the object to database"""
        self.added = 1
        data = sqlite3.connect('data.db')
        cur = data.cursor()
        cur.execute(f"""
        INSERT INTO places(name, address, distance)
        VALUES("{self.name}", "{self.address}",{self.distance});
        """)

        data.commit()
        data.close()

class Date:
    def __init__(self, year: int, month: int, day: int) -> None:
        self.year = year
        self.month = month
        self.day = day
        self.added = 0
        self._compute_week_day()
    
    def _compute_week_day(self) -> None:
        intDay = datetime.date(year=self.year, month=self.month, day=self.day).weekday()
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        self.week_day = days[intDay]

    def show(self) -> tuple:
        """return year/month/day hour:minute weekday"""
        return f"{self.year}/{self.month}/{self.day}", self.week_day


    def add_to_database(self)-> None:
        """just to add the object to database"""
        self.added = 1
        data = sqlite3.connect('data.db')
        cur = data.cursor()
        cur.execute(f"""
            INSERT INTO dates(year, month, day, weekday)
            VALUES({self.year}, {self.month},{self.day}, "{self.week_day}");
        """)

        data.commit()
        data.close()

class Person:
    def __init__(self, name: str, age: int, gender: str) -> None:
        self.name = name
        self.age = age
        self.gender = gender
        self.added = 0

    def add_to_database(self)-> None:
        """just to add the object to database"""
        self.added = 1
        data = sqlite3.connect('data.db')
        cur = data.cursor()
        cur.execute(f"""
            INSERT INTO persons(name, age, gender)
            VALUES("{self.name}", {self.age}, "{self.gender}");
        """)

        data.commit()
        data.close()

class PaymentMethod:
    def __init__(self, name: str, number:str) -> None:
        """if the payment method doesn't have any number, use "0000" as number"""
        self.name = name
        self.number = number
        self.added = 0

    def add_to_database(self)-> None:
        """just to add the object to database"""
        self.added = 1
        data = sqlite3.connect('data.db')
        cur = data.cursor()
        cur.execute(f"""
            INSERT INTO payment_methods(name, number)
            VALUES("{self.name}", "{self.number}");
        """)

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

    def add_to_database(self)-> None:
        """just to add the object to database"""
        self.added = 1
        

if __name__ == "__main__":
    date = Date(2022, 1, 2)
    print(*date.show(), sep=' - ')
    amount = 1000
    place = Place("Amazon", 0, 'www.amazon.de')
    explanation = 'buy some pens and notebooks'
    person = Person("Mohammad Mahdi Reisi", 13, 'male')
    payment_method = PaymentMethod("visa card", '1234-5678-1234-1234')
    discount = 0
    expense = Expense(amount, place, date, explanation, person, payment_method, discount)
    print(expense.date.week_day)
    person.add_to_database()
    payment_method.add_to_database()