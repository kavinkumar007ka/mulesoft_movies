import sqlite3

data_base = "new.db"
s = sqlite3.connect(data_base)

try:
    s.execute("CREATE TABLE movies(name, actor, actress, director, year );")
except:
    pass

opt = ''
while(opt != '4'):
    print("""
    [1] Insert
    [2] search
    [3] show
    [4] quit
    """)
    opt = input("ENTER OPTION:")
    if(opt == '1'):
        name = input("Enter the name:")
        act = input("ACTOR:")
        acts = input("ACTRES:")
        director = input("Director:")
        year = input("Year:")
        s.execute(f'INSERT INTO movies values("{name}","{act}", "{acts}", "{director}", "{year}");')
        s.commit()
    elif(opt == '3'):
        print("(name, actor, actress, director, year )")
        for i in s.execute("SELECT * FROM movies;"):
            for j in i:
                print(j +" | ", end='')
            print()
    elif(opt == '2'):
        c = input("Column name:")
        v = input("Enter value:")
        print("(name, actor, actress, director, year )")
        for i in s.execute(f'SELECT * FROM movies where {c}="{v}";'):
            print(i)
