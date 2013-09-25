import sqlite3, sqlinterface

db_name = raw_input("Please enter name of database: ")
conn = sqlite3.connect(db_name)
print "**Database '%s' has been created..**\n" % (db_name)
c = conn.cursor()
table_name = raw_input("Please enter name of table: ")

values = []
x = 'NULL'
print "Enter values and type (type 'exit' when finished): "
print "Ex. 1. prod text"
while x != 'exit':
	x = raw_input("-> ")
	values.append(x)
values.pop()
c.execute(sqlinterface.create_table(table_name,values))

print "**Table '%s' has been created..**\n" % (table_name)

into_table = []
y = 'NULL'
print "Enter into table (type 'exit' when finished): "
print "Ex. Shoes"
while y != 'exit':
	y = raw_input("-> ")
	into_table.append(y)
into_table.pop()
columns = sqlinterface.parser(values)
print columns
c.execute(sqlinterface.insert_table(table_name,columns,into_table))

for row in c.execute('SELECT * FROM %s' % (table_name)):
	print row
