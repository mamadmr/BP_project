import database_maker
import variable
import sqlite3


def setup():
    database_maker.run()

def add_person(person: variable.Person):
    data = sqlite3.connect('data.db')
    cur = data.cursor()
    cur.execute(f"""
        INSERT INTO persons(name, age, gender)
        VALUES("{person.name}", {person.age}, "{person.gender}");
    """)

    data.commit()
    data.close()

def add_date(date: variable.Date):
    data = sqlite3.connect('data.db')
    cur = data.cursor()
    cur.execute(f"""
        INSERT INTO dates(year, month, day, weekday)
        VALUES("{date.year}", {date.month},{date.day}, "{date.week_day}");
    """)

    data.commit()
    data.close()

if __name__ == '__main__':
    setup()
    someone = variable.Person("Mohammad Mahdi Reisi", 19, 'male')
    add_person(someone)
    somedate = variable.Date(2022, 11, 21)
    add_date(somedate)
