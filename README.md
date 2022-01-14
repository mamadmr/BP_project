# BP_project
an app aims to manage families expenses, it's just a simple object-oriented program 
## tables
####  places:
		id integer PRIMARY KEY,
		name text NOT NULL,
		address text NOT NULL,
		distance integer

#### persons:
		id integer PRIMARY KEY,
		name text NOT NULL,
		age integer,
		gender text

#### dates: 
		id integer PRIMARY KEY,
		year integer,
		month integer,
		day integer,
		weekday text NOT NULL

#### payment_methods
		id integer PRIMARY KEY,
		name text NOT NULL,
		number text NOT NULL
#### expenses 
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
## files 

### data.db 
this file is a main database file, I used sqlite3 as database 



### database_maker.py
this file is just to make tables in database if they don't exist.

it contains "run" function that makes tables, run it without any worried, if the tables exist it won't do anything 

### variable.py
this file contains the classes that used as datatype in the whole program 

		class Place(name, distance, address)
		class Date(year, month, day)
		class Person(name, age, gennder)
		class PaymentMethod(name, number)
		class Expense(amount, explanation, dicount, place, date, person, payment_method)


### search_persons 
this file contains a class, named SearchPerson  you can search for persons in a different ways with name or age or evern gender

