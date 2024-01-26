import sqlite3

# Create the database
db = sqlite3.connect('python_programming_db')
cursor = db.cursor()

print('Database Created!\n')

# Create the table structure 
cursor.execute('''
                CREATE TABLE IF NOT EXISTS students(id INTEGER PRIMARY KEY,
                name VARCHAR,
                grade INTEGER);
''')

db.commit()
print('Table Created!\n')

# Create function that inserts data into a databse
def insert_data():
    student_grades = [
        (55, "Carl Davis", 61), 
        (66, "Dennis Fredrickson", 88), 
        (77, "Jane Richards", 78), 
        (12, "Peyton Sawyer", 45), 
        (2, "Lucas Brooke", 99)]
    
    cursor.executemany('''
                    INSERT OR REPLACE INTO students(id, name, grade)
                    VALUES(?,?,?)
    ''', student_grades)
        
    db.commit()
    print("Data successfully added!")
    

insert_data()

# Create a function that displays all data from the database 
def display_data():
    cursor.execute('''
        SELECT * FROM students
    ''')
    data_ = cursor.fetchall()
    print(data_)
    print('\n')
    
    
display_data()

# Selects all records with a grade between 60 and 80
cursor.execute('''
    SELECT id, name, grade FROM students WHERE grade >= 60 AND grade <= 80   
''')
student_range = cursor.fetchall()
print("The students with grades between 60 and 80 are: ")
print(student_range)
print('\n')

# Update statement used to change grade of 'Carl Davis'
grade = 65
id = 55

cursor.execute('''
    UPDATE students SET grade = ? WHERE id = ?
''', (grade, id,))
print("Database Updated successfully!")

display_data()

# Delete statement used to delete 'Dennis Fredricksons' row
id = 66

cursor.execute('''
    DELETE FROM students WHERE id = ?
''', (id,))

db.commit()
print("Data deleted successfully!")

display_data()

# Update grades for students with id's between 55 and 80
new_grade = 75

cursor.execute('''
    UPDATE students SET grade = ? WHERE id BETWEEN 55 AND 80
''', (new_grade,))

db.commit()
print("Data updated successfully for IDs 55 to 80!")

display_data()