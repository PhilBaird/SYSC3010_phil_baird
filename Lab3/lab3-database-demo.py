#!/usr/bin/env python3
import sqlite3
#some initial data
id = 4;
temperature = 0.0;
date = '2014-01-05';
#connect to database file
dbconnect = sqlite3.connect("mydatabase.db");
#If we want to access columns by name we need to set
#row_factory to sqlite3.Row class
dbconnect.row_factory = sqlite3.Row;
#now we create a cursor to work with db
cursor = dbconnect.cursor();
for i in range(10):
    #execute insert statement
    id += 1;
    temperature += 1.1;
    cursor.execute('''insert into temps values (?, ?, ?, ?)''',
    (date, '00:00', id, temperature));
dbconnect.commit();
#execute simple select statement
cursor.execute('SELECT * FROM temps');
#print data
for row in cursor:
    print(row['tdate'],row['ttime'],row['zone'],row['temperature'] );
    
    
#cursor.execute("CREATE TABLE temps2 (sensorID DATE, type TIME, zone TEXT)")
dbconnect.commit()
data = [('1','door','kitchen'),('2','temperature','kitchen'),('3','door','garage'),('4','motion','garage'),('5','temperature','garage')]
#cursor.executemany("INSERT INTO temps2 VALUES (?, ?, ?)", data)
#dbconnect.commit()
cursor.execute("SELECT * FROM temps2 WHERE zone='kitchen'")
print('\nsenors in kitchen')
for row in cursor:
    print(row['sensorID'],row['type'],row['zone'] )
cursor.execute("SELECT * FROM temps2 WHERE type='door'")
print('\ndoor sensors')
for row in cursor:
    print(row['sensorID'],row['type'],row['zone'] )
dbconnect.close()
