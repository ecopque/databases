import sqlite3

var_connection = sqlite3.Connection('sqlite.sbppro')
var_cursor = var_connection.cursor()

var_cursor.execute('DROP TABLE IF EXISTS Counts') #1:
var_cursor.execute('CREATE TABLE Counts (email TEXT, count INTEGER)') #2:

var_fname = input('Enter file name: ') #3:
if len(var_fname) < 1: #4:
    var_fname = 'mbox-short.txt'

var_fh = open(var_fname)
for var_line in var_fh: #5:
    if not var_line.startswith('From: '): continue #6:
    var_pieces = var_line.split() #7:
    var_email = var_pieces[1] #8:
    var_cursor.execute('SELECT count FROM Counts WHERE email=?', (var_email,)) #9:
    var_row = var_cursor.fetchone() #10:

    if var_row is None: #11:
        var_cursor.execute('INSERT INTO Counts (email, count) VALUES (?, 1)', (var_email,))
    else:
        var_cursor.execute('UPDATE Counts SET count=count + 1 WHERE email=?', (var_email,)) #12:

    var_connection.commit()

var_sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10' #13:

for var_row in var_cursor.execute(var_sqlstr): #14:
    print(str(var_row[0], var_row[1]))
