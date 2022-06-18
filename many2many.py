import sqlite3

# create a database with many to many relationship tables
# student, class and linking table enrollment, then join them

con = sqlite3.connect('school.sqlite')
cursor = con.cursor()

# create tables 
cursor.executescript('''
Drop Table if exists STUDENT;
Drop table if exists CLASS;
Drop table if exists ENROLLMENT;

Create Table STUDENT (
    id integer primary key autoincrement not null unique,
    name text,
    email text
);
Create Table CLASS (
    id integer primary key autoincrement not null unique,
    title text
);
Create Table ENROLLMENT (
    sid integer,
    cid integer,
    registerDate numeric,
    Primary key (sid, cid)
);
''')

# add data into tables
cursor.executescript('''
INSERT INTO STUDENT (name, email) values 
('peter low','pl@email.com'), 
('alice smith', 'alices@yahoo.com'),
('joseph robertson', 'jorobert@yahoo.com'),
('tee mathew', 'teema@mail.com');

INSERT INTO CLASS (title) values ('cs'), ('music'), ('biochemistry');

INSERT INTO ENROLLMENT (sid, cid, registerDate) values 
(1,1,20200311),
(1,3,20210122),
(2,1,20220203),
(3,1,20200910),
(3,3,20211010),
(2,2,20220202),
(4,2,20211002),
(4,3,20210920);
''')

# JOIN tables
cursor.execute('''
SELECT STUDENT.name, CLASS.title 
FROM STUDENT
JOIN ENROLLMENT
JOIN CLASS
ON STUDENT.id = ENROLLMENT.sid
AND class.id = ENROLLMENT.cid
ORDER BY STUDENT.name;

''')

for entry in cursor:
    print(entry)

# output:
# ('alice smith', 'cs')
# ('alice smith', 'music')
# ('joseph robertson', 'cs')
# ('joseph robertson', 'biochemistry')
# ('peter low', 'cs')
# ('peter low', 'biochemistry')
# ('tee mathew', 'music')
# ('tee mathew', 'biochemistry')


con.commit()
con.close()

