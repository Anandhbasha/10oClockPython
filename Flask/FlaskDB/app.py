from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Database configuration dictionary
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "123456",
    "database": "flaskcrud"
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

# Create -> POST
@app.route("/addStu", methods=["POST"])
def createUser():
    data = request.json
    
    # 1. Validate that the incoming request actually has the required data
    if not data or "name" not in data or "age" not in data:
        return jsonify({"Error": "Missing 'name' or 'age' in request body"}), 400

    # 2. Open connection and cursor safely inside the request context
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    
    try:
        sql = "INSERT INTO students (name, age) VALUES (%s, %s)"
        values = (data["name"], data["age"])
        
        cursor.execute(sql, values)
        db.commit()
        
        # Grab the auto-incremented ID of the new student
        new_id = cursor.lastrowid
        
        return jsonify({
            "Message": "Student added successfully", 
            "id": new_id,
            "name": data["name"]
        }), 201
        
    except mysql.connector.Error as err:
        return jsonify({"Error": f"Database error: {err}"}), 500
        
    finally:
        # 3. Always close the cursor and connection when done!
        cursor.close()
        db.close()


@app.route("/",methods=["GET"])
def readStudents():
    try:
        db = get_db_connection()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM students")
        data = cursor.fetchall()
        return jsonify(data)
    except mysql.connector.Error as err:
        return jsonify({"error":"str(err)"})


# read one
@app.route("/std/<int:id>",methods=["GET"])
def readOneStu(id):
    try:
        db = get_db_connection()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM students where id =%s",(id,))
        data = cursor.fetchone()
        if data :
            return jsonify(data)
        return jsonify({"message":"Not found"}),404
    except mysql.connector.Error as err:
        return jsonify({"error":str(err)})
    


@app.route("/updateStd/<int:id>",methods=["PUT"])
def updateOneStu(id):
    data = request.json
    try:       
        db = get_db_connection()
        cursor = db.cursor()
        sql = """UPDATE students SET name=%s,age=%s WHERE id=%s  """
        
        values = (
             data["name"],data["age"],id
        )
        cursor.execute(sql,values)
        db.commit()

        return jsonify({"Mesage":"Updated succesfully"})
    except mysql.connector.Error as err:
        return jsonify({"error":str(err)})
    


@app.route("/delStd/<int:id>",methods=["DELETE"])
def deleteOneStu(id):
    try:       
        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute("DELETE FROM students WHERE id=%s" ,(id,))        
        db.commit()

        return jsonify({"Message":"Delete succesfully"})
    except mysql.connector.Error as err:
        return jsonify({"error":str(err)})



if __name__ == "__main__":
    app.run(debug=True)