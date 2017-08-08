from time import sleep
from smbus import SMBus
import pymysql as SQL
import LIST as LIS

slaveADR = 0x18
bus = SMBus(1)

who_am_I = bus.read_byte_data(slaveADR, 0x0F)
print(who_am_I)
print(str(hex(who_am_I)))

if 5 > 2: 
	print("hello")

#if str(hex(who_am_I)) == str(0x33):
if 1 == 1:
	print("Sensor detected correctly")


# read a register to check 
interruptREG = bus.read_byte_data(slaveADR , LIS.INT1_SRC)
print (hex(interruptREG))

# set data registers
bus.write_byte_data(slaveADR, LIS.CTRL_REG1, 0b10010111)
bus.write_byte_data(slaveADR, LIS.CTRL_REG2, 0b00000000)
bus.write_byte_data(slaveADR, LIS.CTRL_REG3, 0b00000000)
bus.write_byte_data(slaveADR, LIS.CTRL_REG4, 0b00001000)
bus.write_byte_data(slaveADR, LIS.CTRL_REG5, 0b00000010)
bus.write_byte_data(slaveADR, LIS.CTRL_REG6, 0b10100000)


reg1_value  = bus.read_byte_data(slaveADR, LIS.CTRL_REG1)
print(hex(reg1_value))

for value in range(10): 
	LIS.z_output()


# open database connection
db =  SQL.connect(host="localhost",user="root",passwd="Thomas54!",db="vibrationData")

# prepare a cursor object usign the cursor method
db_object = db.cursor()

# execute SQL query usilgn execute() method.
db_object.execute("SELECT VERSION()")

# fetch a single row using fetchone() method.
data = db_object.fetchone()

print("Database version: %s " % data)


#---------- Creating a database table:
# Drop table if it already exists using execute() method.
# Tested this - functions. So can drop acceleration values inside.
db_object.execute("DROP TABLE IF EXISTS EMPLOYEE")

# create a table
table = """CREATE TABLE EMPLOYEE (
FIRST_NAME CHAR(20) NOT NULL,
LAST_NAME CHAR(20),
AGE INT,
SEX CHAR(1),
INCOME FLOAT)"""

db_object.execute(table)

# insert values into the Employees Table:
console = """INSERT INTO EMPLOYEE(FIRST_NAME,
LAST_NAME, AGE, SEX, INCOME)
VALUES ("Max", "Cox", 26, "M", 65000)"""

# sneak a change in here to test git. 
try:
# execute the concole command:
    db_object.execute(console)
# commit changes to the database:
    db.commit()
except:
# roolback incase there is any error
    db.rollback()


#---------------------------------------- read operations:
console = "SELECT * FROM EMPLOYEE WHERE INCOME > '%d'" % (1000)

#try:
    # execute the SQL command
db_object.execute(console)
    # fetch all the rows in a list of lists.
results = db_object.fetchall()
for row in results:
    fname = row[0]
    lname = row[1]
    age = row[2]
    sex = row[3]
    income = row[4]
        # now print fetched result
    print ("fname = %s, lname = %s, age = %d, sex = %s, income = %d" % (fname, lname, age, sex, income))
#except:
 #   print ("Error: unable to fetch data")

#disconnect from server
db.close()

