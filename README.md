# BP_project
an app aims to manage families expenses, it's just a simple object-oriented program 

## how to run ?
its so simple just run the run.py file in the project 

## what is the structure of the program 
in program you can add or remove or search your family expenses 
,first of all you should add your family member to program (use add or remove person), then you should add your family cards to the program with add or remove payment method then you have to add some shops that your family buy things there 
then you can use add or remove expenses to add every thing you bought 

at the end you can see some diagrams buy click on diagrams  

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
## main files 

### data.DB 
this file is the main database file, I used sqlite3 as database 



### database_maker.py
this file is just to make tables in database if they don't exist.

it contains "run" function that makes tables, run it without any worried, if the tables exist it won't do anything 

### variable.py
this file contains the classes that used as datatype in the whole program 

		class Place(name, address, distance)
		class Date(year, month, day)
		class Person(name, age, gender)
		class PaymentMethod(name, number)
		class Expense(amount, explanation, discount, place, date, person, payment_method)


### search_persons 
this file contains a class, named SearchPerson  you can search for persons in a different ways with name or age or even gender

### search_date 
this file contains a class, named SearchDate your can search for different date with different methods

### search payment_methods 
this file contains a class, named SearchPaymentMethod you can search for different payment_methods with their name and number

### search_place 
this file is for search for different places with different methods

### search expenses
use all other searches to find expenses that we want
