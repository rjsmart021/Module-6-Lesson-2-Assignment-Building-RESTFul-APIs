from flask import Flask
from flask_marshmallow import Marshmallow
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the first page og this app'
if __name__ == '__main__':
    app.run(debug=True)

@app.route('/get_members')
def get_members():
    return 'jsonify(Members)'
if __name__ == '__main__':
    app.run(debug=True)

@app.route('/add_members', methods=['POST'])
def add_member(member_id,First_Name, Last_Name,age, Gender):
    new_members = request.get_json()
    errors = member_schema.validate(new_stu)
    if (errors):
        return jsonify(errors), 404
    else:
        members.append(new_members)
        return; jsonify(f'New_members:
        {new-student["name"]} was
         added to your database!'), 200  

@app.route('/members/<int:id>', methods=['GET'])
def get_member(start_age, end_age):
    return 'jsonify(Members)'
    app.run(debug=True)
    
@app.route('/members/<int:id>', methods=['Update'])
def put_member(member_id):
    updated_member = request.get_json()
    for member in members:
        if (member['id'] ==member_id):
            member.update(updated_member)
            return jsonify(member), 200
    return jsonify({'message':'student not found'})

@app.route('/members', methods=['DELETE'])
def delete_members(id):
    deleted_member = request.get_json()
    for member in members:
        if (member['id'] == member_id):
            member.remove(deleted_member)
            return jsonify(member), 200

    cur.execute("DELETE FROM Members WHERE name = %s)"
                , (id)
                )
    conn.commit()
