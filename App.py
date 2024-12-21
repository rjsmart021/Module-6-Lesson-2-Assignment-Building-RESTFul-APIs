from flask import Flask, jsonify, request
from flask_marshmallow import Marshmallow
from marshmallow import fields
from marshmallow import ValidationError
import mysql.connector
from mysql.connector import Error
from SQL import connect_database

app = Flask(__name__)
ma = Marshmallow(app)
class CustomerSchema(ma.Schema):
    name = fields.String(required=True)
    email = fields.String(required=True)
    phone = fields.String(required=True)

class Meta:
    fields = ("name", "email", "phone")
customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)

@app.route('/')
def home():
    return 'Welcome to the first page og this app'

@app.route("/members", methods=["POST"])
def add_member():
    try:
        customer = customer_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    conn = connect_database()
    if conn is None:
        return jsonify({"ERROR": "Database connection failed."}), 500

    try:
        cursor = conn.cursor()
        query = "INSERT INTO Members (name, age, phone, email) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (customer["name"], customer["age"], customer["phone"], customer["email"]))
        conn.commit()
        return jsonify({"MESSAGE": "Member added successfully."}), 201
    except Error as e:
        return jsonify({"ERROR": str(e)}), 500
    finally:
        cursor.close()
        conn.close()


@app.route('/members/<int:id>', methods=['GET'])
def get_member(member_id):
    conn = connect_database()
    try:
        cursor = conn.cursor()
        query = "Select * from Members where id = %s"
        cursor.execute(query, (member_id,))
        member = cursor.fetchone()
        if member: 
            return customer_schema.jsonify(member),201
        else:
            return jsonify({"error": "member not found"}),404
    
    except Error as e:
        return jsonify({"ERROR": str(e)}), 500
    finally:
        cursor.close()
        conn.close()
    
@app.route('/members/<int:id>', methods=['PUT'])
def put_member(member_id):
    try:
        customer = customer_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    conn = connect_database()
    if conn is None:
        return jsonify({"ERROR": "Database connection failed."}), 500

    try:
        cursor = conn.cursor()
        query = "Update Members set name = %s, age = %s, phone = %s, email = %s where id = %s"
        cursor.execute(query, (customer["name"], customer["age"], customer["phone"], customer["email"], member_id))
        conn.commit()
        return jsonify({"MESSAGE": "Member updated successfully."}), 201
    except Error as e:
        return jsonify({"ERROR": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

@app.route('/members <int:id>', methods=['DELETE'])
def delete_members(members_id):
    try:
        cursor = conn.cursor()
        query = "Select * from Members where id = %s"
        cursor.execute(query, (members_id))
        member = cursor.fetchone()
        if member: 
            return customer_schema.jsonify(member),201
        else:
            return jsonify({"error": "member not found"}),404
    
    except Error as e:
        return jsonify({"ERROR": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)
