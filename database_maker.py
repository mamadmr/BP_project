# this file is just make tables if they aren't exist in database
import sqlite3

def run():
	data = sqlite3.connect('data.db')
	cur = data.cursor()

	cur.execute("""
	CREATE TABLE IF NOT EXISTS places (
		id integer PRIMARY KEY,
		name text NOT NULL,
		address text NOT NULL,
		distance integer
	);
	""")

	cur.execute("""
	CREATE TABLE IF NOT EXISTS persons (
		id integer PRIMARY KEY,
		name text NOT NULL,
		age integer,
		gender text
	);
	""")

	cur.execute("""
	CREATE TABLE IF NOT EXISTS dates (
		id integer PRIMARY KEY,
		year integer,
		month integer,
		day integer,
		weekday text NOT NULL
	);
	""")

	cur.execute("""
	CREATE TABLE IF NOT EXISTS payment_methods (
		id integer PRIMARY KEY,
		name text NOT NULL,
		number text NOT NULL
	);
	""")

	cur.execute("""
	CREATE TABLE IF NOT EXISTS expenses (
		id integer PRIMARY KEY,
		amount integer,
		explanation text,
		discount integer,
		place integer NOT NULL,
		date integer NOT NULL,
		person integer NOT NULL,
		payment_method integer NOT NULL,
		FOREIGN KEY (place) REFERENCES places(id),
		FOREIGN KEY (date) REFERENCES dates(id),
		FOREIGN KEY (person) REFERENCES persons(id),
		FOREIGN KEY (payment_method) REFERENCES payment_methods(id) 
	);
	""")

	data.commit()
	data.close()