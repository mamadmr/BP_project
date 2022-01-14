import variable
import sqlite3

class SearchPlace:
    def __init__(self) -> None:
        self.ids = []
    
    def by_name(self, name: str):
        """search for special name in the table"""

        data = sqlite3.connect('data.db')
        cur = data.cursor()
        cur.execute(f"""SELECT id FROM places
                                WHERE name = "{name}";
        """)
        self.ids.append(list(map(lambda x: x[0], cur.fetchall())))
        data.close()
    
    def by_distance(self, distance_down: int, distance_up: int) -> None:
        """search for ages between age_down and age_up"""

        data = sqlite3.connect('data.db')
        cur = data.cursor()
        cur.execute(f"""SELECT id FROM places
                                WHERE {distance_down} <= distance
                                AND {distance_up} >= distance;
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
        """make person objects from ids and return the list of objects"""
        ans = []
        for i in data:
            temp = variable.Place(i[1], i[3], i[2])
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
        cur.execute(f"""SELECT * FROM places
                                WHERE id IN {ids};
        """)
        ans = self.make_object(cur.fetchall())
        data.close()
        return ans


if __name__ == "__main__":
    temp = SearchPlace()
    temp.by_name("Amazon1")
    temp.by_distance(10, 100)
    for i in temp.run():
        print(i.name, i.distance, i.address)