This Project is to draw info out of a SQL database. The python functions are present it is a setup that is tested
Module 5 Lesson 3: Assignments | Applying SQL in Python
Remember to take your time and work through each question diligently! Test your code, make sure it works, and try to find ways to improve. Once you are happy and satisfied with your code, upload it to Github, then turn in your Github link at the bottom of the page!

Don't forget. Make sure this assignment is in it's own repository. Not mixed in with others!
1. Gym Database Management with Python and SQL

Objective: The aim of this assignment is to reinforce your understanding of Python's interaction with SQL databases, focusing on CRUD (Create, Read, Update, Delete) operations in the context of a gym's membership and workout session management system. You will work with two tables: 'Members' and 'WorkoutSessions'.

Problem Statement: You are tasked with developing a Python application to manage a gym's database. The database consists of 'Members' and 'WorkoutSessions' tables. Your role is to implement various functions to add, retrieve, update, and delete records in these tables, ensuring data integrity and efficient data handling.

Task 1: Add a Member

Write a Python function to add a new member to the 'Members' table in the gym's database.
    # Example code structure
    def add_member(id, name, age):
        # SQL query to add a new member
        # Error handling for duplicate IDs or other constraints
Expected Outcome: A Python function that successfully adds a new member to the 'Members' table in the gym's database. The function should handle errors gracefully, such as duplicate member IDs or violations of other constraints.
Task 2: Add a Workout Session

Develop a Python function to add a new workout session to the 'WorkoutSessions' table for a specific member.
    # Example code structure
    def add_workout_session(member_id, date, duration_minutes, calories_burned):
        # SQL query to add a new workout session
        # Error handling for invalid member ID or other constraints
Expected Outcome: A Python function that adds a new workout session to the 'WorkoutSessions' table in the gym's database for a specific member. The function should handle errors gracefully, such as invalid member IDs or violations of other constraints.
Task 3: Updating Member Information

Implement a function to update the age of a member. Ensure that your function checks if the member exists before attempting the update.
    # Example code structure
    def update_member_age(member_id, new_age):
        # SQL query to update age
        # Check if member exists
        # Error handling
Expected Outcome: A Python function that updates the age of a member and handles cases where the member does not exist.
Task 4: Delete a Workout Session

Create a Python function to delete a workout session based on its session ID. Include error handling for cases where the session ID does not exist.
    # Example code structure
    def delete_workout_session(session_id):
        # SQL query to delete a session
        # Error handling for non-existent session ID
Expected Outcome: A Python function that can delete a workout session using its session ID, with proper error handling for invalid IDs.
Submission Guidelines:

Submit a Python script (.py file) containing all the functions for the tasks.
Include comments in your code to explain your logic and SQL queries.
Ensure your script handles errors gracefully and provides meaningful output.


2. Advanced Data Analysis in Gym Management System

Objective: The goal of this assignment is to advance your SQL querying skills within Python, focusing on specific SQL functions and clauses like BETWEEN. You will be working with the same gym database as in the previous assignment, comprising the Members and WorkoutSessions tables.

Problem Statement: As a part of the gym's management team, you need to conduct an in-depth analysis of the membership data. Your task is to develop Python functions that execute advanced SQL queries for distinct department identification, employee count in each department, and age-based employee filtering.

Task 1: SQL BETWEEN Usage

Problem Statement: Retrieve the details of members whose ages fall between 25 and 30.
Expected Outcome: A list of members (including their names, ages, etc) who are between the ages of 25 and 30.
Example Code Structure:
    def get_members_in_age_range(start_age, end_age):
        # SQL query using BETWEEN
        # Execute and fetch results
Note: The database structure used for this assignment is the same as the previous one, consisting of the Members and WorkoutSessions tables.

Submission Guidelines:

Submit a Python script (.py file) containing the functions for the specified tasks.
Ensure your code is well-commented to explain the logic and SQL queries used.
Make sure your script includes error handling and provides clear output for each task.
NOTE: Ensure that all code in your file is ready to run. This means that if someone opens your file and clicks the run button at the top, all code executes as intended. For example, if there are if statements, print statements, or for loops, they should function correctly and display output in the console as expected. If you have a function, make sure the function is called and runs. If there are classes/objects, make sure they are instantiated and the methods are called.

The goal of this note is to ensure that all code in your Python file runs smoothly and that is has been tested.
