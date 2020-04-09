import sqlite3
from urllib.request import urlopen

conn=sqlite3.connect('emaildb.sqlite')
cur=conn.cursor()
# cur.execute('DROP TABLE IF EXISTS Counts')
# cur.execute('''
# CREATE TABLE Counts (email TEXT, count INTEGER)''')

# fname=input('enter file name: ')
fname='mbox-short.txt'

if (len(fname) <1) : 
    fname='mbox-short.txt'

with open(fname,'r') as f:
    for line in f:
        if not line.startswith('From: '): continue
        pieces=line.split()
        email=pieces[1]
        print('->',email)
        # cur.execute('SELECT count FROM Counts WHERE email=?', (email,))
        row=cur.fetchone()
        if row is None:
            cur.execute('''
            INSERT INTO Counts (email, count) VALUES (?,1)''', (email,))
        else:
            cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
                    (email,))
        conn.commit()
sqlstr='SELECT email, count FROM Counts'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'
connection = urlopen(TWITTER_URL)
data=connection.read().decode()

