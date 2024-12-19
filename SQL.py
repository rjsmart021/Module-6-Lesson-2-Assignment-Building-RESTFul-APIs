import mysql.connector
from mysql.connector import Error
DB_NAME_DEFAULT = "SQL_1"
DB_USER = "root"
DB_PASSWORD = "HHappiness0621#"
#Connect to default database
def connect_database():
    """ Connect to the MySQL database and return the connection object """
    #Database connection parameters 
    db_name = "e_commerce_db"
    user = "user"
    password = "password"
    host = "localhost"

    try:
        conn = mysql.connector.connect(
            database = db_name,
            user = user,
            password = password,
            host = host
        )

        # Check if the connection si sucessful
        print("Connected to MySQL database successfully")
        return conn

    except Error as e:
        # Handling any connection errors
        print(f"Error: {e}")
        return None
# Create a database in your MySQL Workbench and fill the db_name, user and password with yours, then use that function to create a connection like:"
conn = connect_database()
# And use it inside the functions to perform the different operations, for example, this is a function to inser a member:
def add_member(id, name, age):
    """
    Adds a new member to the 'Members' table.
    This will also handle duplicate ID and constraint violations.
    """
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
def add_workout_session(member_id, date, duration_minutes, calories_burned):
    cur.execute("INSERT INTO WorkoutSessions member_id, date, duration_minutes, calories_burned) VALUES(%s,%s,%s,%s)", 
                (member_id, date, duration_minutes, calories_burned)
                )
    conn.commit()

def add_member(member_id,First_Name, Last_Name,age, Gender):
    cur.execute("INSERT INTO member_id,First_Name, Last_Name,age, Gender) VALUES(%s,%s,%s,%s,%s)", 
                (member_id,First_Name, Last_Name,age, Gender)
                )
    conn.commit()
    
def update_member_age(member_id, new_age):
    cur.execute( "UPDATE WorkoutSessions SET age = %s WHERE member_id = %s;)", 
                    (member_id, new_age)
                    )
    conn.commit()

 # Example code structure
def delete_workout_session(session_id):
    cur.execute("DELETE FROM WorkoutSessions WHERE name = %s)"
                , (session_id,)
                )
    conn.commit()
    

def get_members_in_age_range(start_age, end_age):
    cur.execute("SELECT * FROM Members WHERE Members BETWEEN %s AND %s)",
                (start_age, end_age)
                )
    conn.commit()

#Test 1
add_member('Sz678','Fitzgera', 'Kangory', 24, 'Male')
add_workout_session('Sz678',10/20/2024,70,130)
update_member_age('Sz678',67)
delete_workout_session(554567)
get_members_in_age_range((45, 55))
