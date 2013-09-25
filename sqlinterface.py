from collections import deque

def create_table(name, values):
	assembler = parser(values)
	t = "CREATE TABLE %s (%s)" % (name, assembler)
	return t

def insert_table(tb_name, columns, values):
	assembler = parser(values)
	t = "INSERT INTO %s (%s) VALUES (%s)" % (tb_name, columns, assembler)
	print t
	return t

def select(name, tb_name):
	t = "SELECT %s FROM %s" % (name, tb_name)
	return t

def delete(tb_name, column, value):
	assembler = '%s=%s' % (column, value)
	t = "DELETE FROM %s WHERE %s" (tb_name, assembler)
	return t

def parser(values):
	assembler = ''
	for x in values:
		temp1 = assembler
		assembler = x
		assembler = temp1 + ', ' + assembler
	convert = deque(list(assembler))
	convert.popleft()
	convert.popleft()
	assembler = "".join(convert)
	return assembler

def remove_type(values):
	