import variable
import sqlite3

class SearchDate:
    def __init__(self) -> None:
        """to search about different date"""
        self.ids = []

    def compar(self, year: int, month: int, day: int) -> int:
        """give a number to each date to compar it simply"""
        return 100000 * year + 100 * month + day

    def by_date(self, date_down = variable.Date(1900,1,1), date_up = variable.Date(3000, 1, 1)):
        """search for special date in the table"""
        date_down = self.compar(date_down.year, date_down.month, date_down.day)
        date_up = self.compar(date_up.year, date_up.month, date_up.day)

        data = sqlite3.connect('data.db')
        data.create_function("compar", 3, self.compar)
        cur = data.cursor()

        cur.execute(f"""SELECT id FROM dates
                                WHERE compar(year, month, day) >= {date_down}
                                AND compar(year, month, day) <= {date_up};
        """)
        self.ids.append(list(map(lambda x: x[0], cur.fetchall())))
        data.close()
    
    def by_id(self, id: int) -> None:
        """search for special id in the table"""

        data = sqlite3.connect('data.db')
        cur = data.cursor()
        cur.execute(f"""SELECT id FROM dates
                                WHERE id = "{id}";
        """)
        self.ids.append(list(map(lambda x: x[0], cur.fetchall())))
        data.close()

    def make_object(self, data: tuple) -> list:
        """make objects from ids and return the list of objects"""
        ans = []
        for i in data:
            temp = variable.Date(i[1], i[2], i[3])
            temp.id = i[0]
            temp.added = 1
            ans.append(temp)
        return ans

    def run(self) -> list:
        self.by_date()
        """do the main job and return the answer as a list of objects"""
        ids = tuple(self.ids[0])
        if(len(ids) == 1):
            ids = '(' + str(ids[0]) + ')'

        data = sqlite3.connect('data.db')
        cur = data.cursor()
        cur.execute(f"""SELECT * FROM dates
                                WHERE id IN {ids};
        """)
        ans = self.make_object(cur.fetchall())
        data.close()
        return ans
    

if __name__ == "__main__":
    date = SearchDate()
    date.by_date(date_down=variable.Date(2028, 6, 12), date_up = variable.Date(2028, 6, 12))
    for i in date.run():
        print(i.week_day)
    