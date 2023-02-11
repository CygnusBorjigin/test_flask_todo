# UserManagagement Class

The user management class is in the Main.py in the user_management folder. A UserManagement object will be able to add users to the database and list all the users. 
It is an interface meant to interact with the database 

## Imports

The class makes use of the json, bson, bcrypt, and ast packages. 
The json and bson packages are used to convert a Cursor object into json so it can be returned to the user. Cursors are just the type of data returned when using MongoDB .find method.
The ast package's literal eval method is used to convert data into a dictionary. 
The bcrypt package is used to encrypt passwords before storing them in the database. 
The class also makes use of database_connection package. This package's database_connect file has the function .connect() which allows the class to connect to the database and cluster.  

## Functions

### init
#### parameters: self
Every time a UserManagement object is initialized, it comes with the attribute _connection. This attribute is the connection to the database and allows the object to interact with the database in the following methods. 

### add_user
#### parameters: self, raw_data
This method adds a user to the database. The parameter raw_data is json data containing a new users information. 
The method first decodes and evaluates this data, converting and storing it into a dictionary. 
From there, a salt (cryptographically secure random string that is added to a password before it's hashed) is generated. Using this salt, the password in the dictionary is replaced by its encrypted version. Finally, the method will use the _connection attribute to insert the user dictionary into the database. Error management needs to be added. 

### list_user
This method returns all the users. 
It uses the _connection attribute to search (without a filter) the database and stores what it finds in a variable. That variable is then iterated through, appending each element to a new list. That list is then converted to json format and returned.

## How to use

#### First import the package and install dependencies
Example import:

`from .pkg.user_management.main import UserManagement`

#### Then create an object of the UserManagement Class
`u_m = UserManagement()`

#### Now the u_m object can manage users through the methods

` u_m.add_user(raw_data)`

`u_m.list_user()`


   
