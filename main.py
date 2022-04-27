import sqlite3

connection = sqlite3.connect("mydbfile.sl3", 5)
cur = connection.cursor()


# cur.execute(f"CREATE TABLE student (name TEXT);")
# cur.execute(f"ALTER TABLE student ADD age TEXT; ")
# cur.execute(f"ALTER TABLE student ADD school TEXT; ")

cur.execute("INSERT INTO student (name) VALUES ('john'), ('andrei');")
cur.execute("INSERT INTO student (age) VALUES ('Twenty'), ('Nineteen');")
cur.execute("INSERT INTO student (school) VALUES ('university N1'), ('university N6');")


choise = input("Choose the act:\nAdd: a \t\tDelete: d\t\tEdit: e\n")

if choise == "a":
    #cur.execute("INSERT INTO student (name) VALUE ('snickers');")
    #cur.execute("INSERT INTO student (age) VALUE ('from 1923 years');")
    #cur.execute("INSERT INTO student (school) VALUE ('factory');")
elif choise == "d":
    #cur.execute("DELETE FROM student WHERE name='john';")
    #cur.execute("DELETE FROM student WHERE age='Twenty';")
    #cur.execute("DELETE FROM student WHERE school='university N1';")
elif choise == "e":
    #cur.execute(f"ALTER TABLE student ADD name TEXT; ")
    #cur.execute(f"ALTER TABLE student ADD age TEXT; ")
    #cur.execute(f"ALTER TABLE student ADD school TEXT; ")


connection.close()
