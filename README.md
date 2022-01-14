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
## files 

### data.db 
this file is a main database file, I used sqlite3 as database 



### database_maker.py
this file is just to make tables in database if they don't exist.

it contains "run" function that makes tables, run it without any worried, if the tables exist it won't do anything 

### variable.py
this file contains the classes that used as datatype in the whole program 

	class Place
	class Date
	class Person
	class PaymentMethod
	class Expense
