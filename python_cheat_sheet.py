################################################################

''' Creating a string '''
str_1 = 'Python Bootcamp'


################################################################

''' Built-in String Functions'''

str_1    = 'Python Bootcamp'

### str.find()

# position_1 will contain the value 7 as the string 'Boot' begins
# at the index 7 in the string
position_1 = str_1.find('Boot')
print position_1

# position_2 will contain the value -1 as the string 'Gemini' is
# not present in the string
position_2 = str_1.find('Gemini')
print position_2

### lower() and upper()

# str_upper will contain the string 'PYTHON BOOTCAMP'
str_upper = str_1.upper()
print str_upper

# str_upper will contain the string 'python bootcamp'
str_lower = str_1.lower()
print str_lower

################################################################

''' Creating an integer '''
int_1 = 4


################################################################

''' if/else conditionals '''

if (int_1 == 4):
    print 'int_1 is equal to 4'

if (int_1 == '4'):
    print 'int_1 is equal to 4'
else:
    print "int_1 is NOT equal to the string '4'"

# To check if an element exists in a container
list_of_numbers = [1,2,3,4,5]
# *NOTE* This syntax works for any type of container
if (5 in list_of_numbers):
    print('5 is in list_of_numbers')

print("")


################################################################

''' Print formatting '''
# Output to stdout: 'It is week 4 for the Python Bootcamp'
print('It is week %d for the %s\n' % (int_1, str_1))

################################################################

''' Creating a list '''
list_1 = [1,2]

# Appending to a list
# list_1 will now be [1,2,'New Element']
list_1.append('New Element')

# Indexing a list
# This will return the element in index 2 ('New Element')
list_1[2]

# Length of a list
len(list_1)

# Iterating over a list
# This will print each element in the list
for element in list_1:
    print element

print("")

################################################################

''' Creating a tuple '''
# Tuples are immutable (they can't be changed)
tuple_1 = ('a', 5, 2)

# Indexing a tuple
# This will return the element in index 1 (5)
tuple_1[1]

# Length of a tuple
len(tuple_1)

# Iterating through a tuple
for element in tuple_1:
    print element

print("")



################################################################

''' Creating a dictionary '''
key_to_value = {}

# Adding an element to a dictionary
key_to_value['key_1'] = 'value_1'
key_to_value['key_2'] = 2

# Indexing a dictionary
# This will return 'value_1'
key_to_value['key_1']

# Length of a dictionary
len(key_to_value)

# Returns a list of the keys in the dictionary
key_to_value.keys()

# Returns a list of the values in the dictionary
key_to_value.values()

# Returns a list of tuples (the tuples will be each key/value pair)
key_to_value.items()

# Iterating over a dictionary
# When iterating over a dictionary, the for loop iterates over a list of the dictionary's keys
for key in key_to_value:
    value = key_to_value[key]
    print key, value


# To check if a key exists in the dictionary
if ('key_1' in key_to_value):
    print ('key_1 is in key_to_value!')


print("")


################################################################

''' Opening a File '''
# FileName.txt - The file we are opening
# 'r' - This means we are opening the file for reading (use 'w' for writing or 'wr' for read/writing)
file_1 = open('FileName.txt', 'r')

# Iterating over a file
# The variable 'line' will be assigned to each successive line in the file
for line in file_1:
    # rstrip will removed trailing characters including '\n' (new line characters)
    line = line.rstrip()
    print line

print("")

################################################################

''' Defining a Function '''

# Function definition
def add_two_numbers(parameter_1, parameter_2=10):
    # The values passed in by the user are assigned to parameter_1 and parameter 2
    # if the user does not pass in a value for parameter_2, the value 10 will be assigned to by default
    sum = parameter_1 + parameter_2
    
    # This value will be returned to the caller
    return sum
    
# Calling a function
result = add_two_numbers(15,12)
# result will contain the sum of the values passed in: 15 and 12, which is 27
print result
    
################################################################

''' Regular Expressions '''

# Import the regular expression module
import re

# Create a regular expression pattern and assign it to a string
# *NOTE* the parentheses are used to capture those parts of the regular expression
regex_address = '(\d+)\s([a-zA-Z]+\s[a-zA-Z]+)'
address_str = '60 Broad Street'

# Create a match object
# re.search(REGEX,STRING)
match_obj = re.search(regex_address, address_str)
address_number = match_obj.group(1) # <-- Assigned to what is captured from (\d+)
street_name = match_obj.group(2) # <-- Assigned to what is captured from ([a-zA-Z]+\s[a-zA-Z]+)
print ('The address number is: %s' % address_number)
print ('The street is: %s' % street_name)

################################################################

''' File Compression '''

# The ZIP file format is a common archive and compression standard. 
# This module provides tools to create, read, write, append, and list a ZIP file
import zipfile

# For applications that require data compression, the functions in this module allow compression and decompression, using the zlib library
# The zipfile module uses zlib to compress files
import zlib

# Create zip file in write mode ("w")
zip_file = zipfile.ZipFile(file="compressed_file.zip", mode="w")

# This is the type of compression the zipfile module will use to compress files
# When zipfile sees ZIP_DEFLATED as the compression type, it will compress the file using the zlib module internally
# This is why we MUST import zlib in addition to zipfile when compressing files
compression_type = zipfile.ZIP_DEFLATED

# Add 'MatchingEngine.log' to the zipfile using the defined compression type above (zipfile.ZIP_DEFLATED)
zip_file.write('MatchingEngine.log', compress_type=compression_type)

# Close zipfile
zip_file.close()

################################################################

''' os Module - Miscellaneous operating system interfaces '''

# This module provides a portable way of using operating system dependent functionality
import os

# Returns a list of the contents of the specified directory
# Each element is represented by as a string
file_list = os.listdir('/home/python_bootcamp/')

# Iterate over list and print each filename
for file_name in file_list:
    print file_name

# This method will take a file name and return a tuple
# The first element will contain the file name without the file extension
# The second element will contain the file extension
file_details_tuple = os.path.splitext('MatchingEngine.log')

file_name = file_details_tuple[0]
extension = file_details_tuple[1]

# This will print 'MatchingEngine'
print file_name

# This will print '.log'
print extension

# You can also assign both values of the tuple at the same time
file_name, extension = os.path.splitext('MatchingEngine.log')

# This will print 'MatchingEngine'
print file_name

# This will print '.log'
print extension

################################################################

''' MySQL Module '''

# imports the MySQL module
import MySQLdb

# Connection object used to connect to the database
conn = MySQLdb.connect(host="tc-pat201", port=13800, user="gtsdbadmin", passwd="gtsdbadmin", db="viewdb")

# Cursor object used to execute queries and store/retrieve data from the database
cursr = conn.cursor()

# SQL query
sql = 'SELECT * FROM MatcherProductStateParameters M;'

# Executing the SQL query
cursr.execute(sql)

# Stores all the rows returned by the query.  'data' will be a single tuple
# containing a tuple for each row returned from the query
data = cursr.fetchall()

# Iterating through data to print each row returned by the query
for row in data:
    print(row)

# Create a Dictionary Cursor Object
dict_cursr = conn.cursor(MySQLdb.cursors.DictCursor)

# Execute a second query    
dict_cursr.execute('SELECT * FROM MatcherProductStateParameters where productID=12506;')

# data2 contains all the rows returned by the MOST RECENT query
# executed by the Cursor object
data2 = dict_cursr.fetchall()

# This will print the first row:
# {'currentBusinessDate': datetime.date(2014, 7, 29), 'artificialID': 1L, 'partitionProductID': 1L, 'partitionNumber': 1L, 'productStateID': 1059L, 'lastTriggeredEventTime': datetime.datetime(2014, 7, 29, 14, 30), 'currentState': 3, 'productID': 2355L}
print data2[0]

# To print a specific field
# This is indexing the first element (0) in the tuple which is a dictionary
# Afterwards we are indexing the dictionary using the key 'currentBusinessData'
print data2[0]['currentBusinessData']

# Displaying that the length of data2 is different from the original 'data'
print(len(data2))

# Commits any changes that have been made to the database
conn.commit()

# Closes the cursor object
cursr.close()

# Closes the connection object
conn.close()

################################################################

''' GtsEnvConfig - This is a module used to retrieve information from the current information '''

# import the module
import sys
import MySQLdb
sys.path.append("/home/bautcar/SVN_TestAutomation/RobotFramework/GtsEnvConfig")
from GtsEnvConfig.GtsEnvConfig import GtsEnvConfig

# Create the GtsEnvConfig object
gec = GtsEnvConfig()

# Connect to viewdb and return a connection object
viewdb_conn = gec.dbConnect(database='viewdb')

# Create a Dictionary Cursor Object
viewdb_cursr = viewdb_conn.cursor(MySQLdb.cursors.DictCursor)

# Execute a second query    
viewdb_cursr.execute('SELECT * FROM MatcherProductStateParameters where productID=12506;')

# data2 contains all the rows returned by the MOST RECENT query
# executed by the Cursor object
data2 = viewdb_cursr.fetchall()

# This will print the first row:# {'currentBusinessDate': datetime.date(2014, 7, 29), 'artificialID': 1L, 'partitionProductID': 1L, 'partitionNumber': 1L, 'productStateID': 1059L, 'lastTriggeredEventTime': datetime.datetime(2014, 7, 29, 14, 30), 'currentState': 3, 'productID': 2355L}
print data2[0]

# To print a specific field
# This is indexing the first element (0) in the tuple which is a dictionary
# Afterwards we are indexing the dictionary using the key 'currentBusinessData'
print data2[0]['currentBusinessData']

# Connect to obsdb11 and return a connection object
obsdb_conn = gec.dbConnect(partition=1, database='obsdb', tier=1)

# Create Dictionary cursor object for obsdb connection
obsdb_cursr = obsdb_conn.cursor(MySQLdb.cursors.DictCursor)

# Execute query on obsdb database
obsdb_cursr.execute('SELECT * FROM obsdb11.transactioninfos t;')

# Retrieve resultset
result_set = obsdb_cursr.fetchall()

# Print each row in the result set
for row in result_set:
    print row

################################################################

''' pyodbc Module - SQL Module used to connect and execute queries on MsSQL Databases '''

# Import the pyodbcmodule
import pyodbc

# Create variables for database connection
driver      = '{SQL Server}'
server_port = 'DC-SQL01\SQM1,59897'
database    = 'iors_gts_oat_gts01'
user_name   = 'iors_gts_oat_gts01'
user_pw     = 'iors_gts_oat_gts01'

# Create connection object by using the 'connect()' function
iors_conn = pyodbc.connect(driver=driver, server=server_port, database=database, uid=user_name, pwd=user_pw)

# Create cursor object by using the 'cursor()' method on the connection object
iors_cursor = iors_conn.cursor()

# Create query
sql_query = 'SELECT buName, orderId FROM [iors_gts_oat_gts01].[dbo].[core_multiday_orders]'

# Execute query on database using the 'execute()' method
iors_cursor.execute(sql_query)

# Retrieve results from query using the 'fetchall()' method
# fetchall() returns a tuple of tuples
# There will be one tuple and each element will be a row represented by a tuple
# The row tuples have elements for each row value.  In this example, the first element of the row tuple will
# contain the buName value and the second element of the row tuple will contain the orderId value
result_set = iors_cursor.fetchall()

# Iterate over the result_set and print the buName and orderID for each order
for row in result_set:
    buName       = row[0]
    orderID      = row[1]
    print 'BU:%s orderID:%s' % (buName, orderID)


# Commit any changes you may have made (none in this example)
iors_conn.commit()

# Close cursor
iors_cursor.close()

# Close database connection
iors_conn.close()

################################################################

''' 
    Classes - Classes allow users to encapsulate data in a organized/user friendly manner
        and allow specific methods (functions) to be performed using this data
'''

# Defining a class called Calculator
# Classes are always uppercase
class Calculator:

    # The __init__ method is called upon creation (instantiation) of the class object.
    # This is also where arguments are passed into the object (first_num, second_num).
    # The __init__ method is used to setup initial variables and call any other methods
    # that are required upon initial creation of the object
    #
    # The first argument of every method requires 'self' to be passed in.
    # 'self' is what represents the object.  To retrieve variables (data members)
    # of the object or call methods, the self object must be used.
    def __init__(self, first_num, second_num):

        # These are variables local to the class object
        # These variables can also be referred to as data members
        # In order to make them available throughout the class, it is necessary to use self.VARIABLENAME
        self.first_num  = first_num
        self.second_num = second_num

        self.sum        = None
        self.product    = None
        
    # This is a method that can be called in order to add the two numbers given by the user
    # After the class object is created, we can now call this object's method
    # The data member 'self.sum' is updated after this method call
    def add_numbers(self):
        self.sum = self.first_num + self.second_num
        print "The sum of '%s' and '%s' is: %s" % (self.first_num,
                                                    self.second_num,
                                                    self.sum)
        return self.sum

    # This is a method that can be called in order to multiply the two numbers given by the user
    # After the class object is created, we can now call this object's method
    # The data member 'self.product is updated after this method call
    def multiply_numbers(self):
        self.product = self.first_num * self.second_num
        print "The sum of '%s' and '%s' is: %s" % (self.first_num,
                                                    self.second_num,
                                                    self.product)
        return self.product


# Create (instantiate) Calculator object
calc = Calculator(5,10)

# Add 5 and 10 by calling the add_numbers method
sum = calc.add_numbers()

# Multiply 5 and 10 by calling the multiply_numbers method
product = calc.multiply_numbers()

# Printing the sum and product using the return values
print 'Return values - sum: %s product: %s' % (sum, product)

# Printing the sum and product using the object's data members
print 'Data members  - calc.sum: %s calc.product: %s' % (calc.sum, calc.product)
