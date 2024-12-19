from flask import Flask
from flask_marshmallow import Marshmallow
import mysql.connector
from mysql.connector import Error


conn = connect_database()

conn = connect_database()
if conn is not None: 
        try:
            cursor = conn.cursor()
            sql_query = "INSERT INTO Members (id, name, age) VALUES (%s, %s, %s)"
            cursor.execute(sql_query, (id, name, age))
            conn.commit()
            print(f"Member {name} added successfully.")
        except Exception as e:
            print(f"Error while adding member: {e}")
        finally:
            cursor.close()
            conn.close()
            print("MySQL connection is closed.")
cur = conn.cursor
#Add SQL Database
cur.execute("""CREATE TABLE Members (
    id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT,
);""")
conn.commit()
cur.execute("""CREATE TABLE WorkoutSessions (
    session_id INT PRIMARY KEY,
    member_id INT,
    session_date DATE,
    session_time VARCHAR(50),
    activity VARCHAR(255),
    FOREIGN KEY (member_id) REFERENCES Members(id)
);""")
conn.commit()
#Close connction
conn.close()

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the first page og this app'
if __name__ == '__main__':
    app.run(debug=True)

@app.route('/home')
def home():
    return 'Welcome to the Home Page'
if __name__ == '__main__':
    app.run(debug=True)

@app.route('/members', methods=['POST'])
def add_member(member_id,First_Name, Last_Name,age, Gender):
    cur.execute("INSERT INTO member_id,First_Name, Last_Name,age, Gender) VALUES(%s,%s,%s,%s,%s)", 
                (member_id,First_Name, Last_Name,age, Gender)
                )
    conn.commit()

@app.route('/members/<int:id>', methods=['GET'])
def get_member(start_age, end_age):
    cur.execute("SELECT * FROM Members WHERE Members BETWEEN %s AND %s)",
                (start_age, end_age)
                )
    conn.commit()
    
@app.route('/members/<int:id>', methods=['PUT'])
def put_member(id):
    #----
    pass

@app.route('/members', methods=['DELETE'])
def delete_members(id):
    cur.execute("DELETE FROM Members WHERE name = %s)"
                , (id)
                )
    conn.commit()
