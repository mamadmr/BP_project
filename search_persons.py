import variable
import sqlite3

class SearchPerson: 
    def __init__(self) -> None:
        """this class is for Search in a different way for some Persons"""
        self.ids = [] 
    
    def by_name(self, name: str) -> None:
        """search for special name in the table (just one name)"""

        data = sqlite3.connect('data.db')
        cur = data.cursor()
        cur.execute(f"""SELECT id FROM persons
                                WHERE name = "{name}";
        """)
        self.ids.append(list(map(lambda x: x[0], cur.fetchall())))
        data.close()
    
    def by_age(self, age_down: int=-10, age_up: int = 1000) -> None:
        """search for ages between age_down and age_up"""

        data = sqlite3.connect('data.db')
        cur = data.cursor()
        cur.execute(f"""SELECT id FROM persons
                                WHERE {age_down} <= age
                                AND {age_up} >= age;
        """)
        self.ids.append(list(map(lambda x: x[0], cur.fetchall())))
        data.close()

    def by_gender(self, gender: str) -> None:
        """search for genders -> male and female"""
        data = sqlite3.connect('data.db')
        cur = data.cursor()
        cur.execute(f"""SELECT id FROM persons
                                WHERE gender = "{gender}"
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
            temp = variable.Person(i[1], i[2], i[3])
            temp.id = i[0]
            temp.added = 1
            ans.append(temp)
        return ans

    def run(self) -> list:
        """do the main job and return the answer as a list of objects"""
        ids = self.transport()
        if len(ids) == 1:
            ids = '(' + str(ids[0]) + ')'
        if len(ids) == 0:
            return []
    
        data = sqlite3.connect('data.db')
        cur = data.cursor()
        cur.execute(f"""SELECT * FROM persons
                                WHERE id IN {ids};
        """)
        ans = self.make_object(cur.fetchall())
        data.close()
        return ans


if __name__ == "__main__":
    person = SearchPerson()
    person.by_name("sara 0")
    person.by_age(age_down=5, age_up=13)
    person.by_gender("male")
    for i in person.run():
        print(i.name, i.age)
    print(person.ids)