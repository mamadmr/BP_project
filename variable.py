import datetime
import sqlite3
import database_maker

class Place:
    def __init__(self, name: str, distance: int, address: str) -> None:
        """
            the place could be a website or a shop or an organization 
            if the place is website put 0 as distance
            if the variable "added" is equal to one, means this object is in the database 
            if "id" is equal to -1 means this object is not in database yet
        """
        self.name = name
        self.distance = distance
        self.address = address
        self.added = 0
        self.id = -1

    def add_to_database(self)-> bool:
        """just to add the object to database if it hasn't added to database yet 
            return 1 if the object added and return 0 if the object exist in the database"""
        if self.added == 1:
            # check if the object isn't in database
            return 0

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
        return 1
    
    def remove_from_database(self) -> bool:
        """remove the object from data base if it's in the database
        return 1 if the object removed and return 0 if the object is not exists in the database"""
        if self.added == 0:
            # check if the object is exist in database
            return 0

        data = sqlite3.connect('data.db')
        cur = data.cursor()
        cur.execute(f"""DELETE FROM places
                        WHERE id = {self.id};
        """)
        self.added = 0
        self.id = -1
        data.commit()
        data.close()
        return 1

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

    def show(self) -> str:
        """return year/month/day hour:minute weekday"""
        return f"{self.year}/{self.month}/{self.day} {self.week_day}"

    def add_to_database(self)-> bool:
        """just to add the object to database if it's not exist if the object is not in 
        database return 1 else return 1"""

        if self.added == 1:
            return 0
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
        return 1

    def remove_from_database(self) -> bool:
        """remove the object from data base
           if the job has done return 1 else return 0"""
        if self.added == 0:
            return 0

        data = sqlite3.connect('data.db')
        cur = data.cursor()
        cur.execute(f"""DELETE FROM dates
                        WHERE id = {self.id};
        """)
        self.added = 0
        self.id = -1
        data.commit()
        data.close()
        return 1

class Person:
    def __init__(self, name: str, age: int, gender: str) -> None:
        """each object is a person who can buy things"""
        self.name = name
        self.age = age
        self.gender = gender
        self.added = 0
        self.id = -1

    def add_to_database(self)-> bool:
        """just to add the object to database if every thing done good return 1 else return 0"""
        if self.added == 1:
            # check if the object not exist in database
            return 0
    
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
        return 1

    def remove_from_database(self) -> bool:
        """remove the object from data base if the job has done return 1 else return 0"""
        if self.added == 0:
            return 0

        data = sqlite3.connect('data.db')
        cur = data.cursor()
        cur.execute(f"""DELETE FROM persons
                        WHERE id = {self.id};
        """)
        self.add = 0
        self.id = -1
        data.commit()
        data.close()
        return 1

class PaymentMethod:
    def __init__(self, name: str, number:str='0000') -> None:
        """if the payment method doesn't have any number, use "0000" as number"""
        self.name = name
        self.number = number
        self.added = 0
        self.id = -1

    def add_to_database(self)-> bool:
        """just to add the object to database if job has done well return 1 else return 0"""
        if self.added == 1:
            # check if the object exist in database
            return 0
        
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
        return 1

    def remove_from_database(self) -> bool:
        """remove the object from data base return 1 if the job has been done well else return 0"""
        if self.added == 0:
            # check if the object is not exist in database
            return 0

        data = sqlite3.connect('data.db')
        cur = data.cursor()
        cur.execute(f"""DELETE FROM payment_methods
                        WHERE id = {self.id};
        """)
        self.added = 0
        self.id = -1
        data.commit()
        data.close()
        return 1

class Expense:
    def __init__(self, amount: int, place: Place, date: Date, explanation: str,
                 person: Person, payment_method: PaymentMethod, discount: int)  -> None:
        """each object contains an expense with it's information"""
        self.amount = amount
        self.place = place
        self.date = date
        self.explanation = explanation
        self.person = person
        self.payment_method = payment_method
        self.discount = discount
        self.added = 0
        self.id = -1

    def add_to_database(self)-> bool:
        """just to add the object to database
            return 1 if the job has been done well else return 0"""
        if self.added == 1:
            return 0

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
        return 1

    def remove_from_database(self)-> bool:
        """remove the object from data base
        return 1 if the job has been done well else return 0"""

        if self.added == 0:
            return 0

        data = sqlite3.connect('data.db')
        cur = data.cursor()
        cur.execute(f"""DELETE FROM expenses
                        WHERE id = {self.id};
        """)
        self.added = 0
        self.id = -1
        data.commit()
        data.close()
        return 1

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

    payment_method = PaymentMethod("visa card", '1234567812341234')
    payment_method.add_to_database()

    expense = Expense(amount, place, date, explanation, person, payment_method, discount)
    expense.add_to_database()

    # place.remove_from_database()
    # date.remove_from_database()
    # person.remove_from_database()
    # payment_method.remove_from_database()
    # expense.remove_from_database()

