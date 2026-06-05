#pip install flask
# restApi
# get -> get a data from database
# post -> add a newdata to Database
# put -> already existing info going to edit
# delete -> already existing info will delete


from flask import Flask,request,jsonify

app = Flask(__name__)

students =[
    {
    "id":1,
    "name":"raja",
    "age":30
},{
    "id":2,
    "name":"Karthick",
    "age":30
}
]

print(students)
@app.route("/addStudent",methods=["POST"])
def createStudents():
    data = request.json
    student = {
        "id":len(students)+1,
        "name":data["name"],
        "age":data["age"]
    }
    students.append(student)
    return jsonify({
        "message":"Student Added Succesfully",
        "data":student
    })

@app.route("/readStudents",methods=["GET"])
def getStudents():
    return jsonify(students)
        
@app.route("/readStudent/<int:id>",methods=["GET"])
def getStudent(id):
    for stu in students:
        if stu["id"] ==id:
            return jsonify(stu)
    return jsonify({"Message":"Student Not found"})


@app.route("/stuEdit/<int:id>",methods =["PUT"])
def updateStudent(id):
    for stu in students:
        if stu["id"] == id:
            data = request.json
            stu["name"] = data ["name"]
            stu["age"] = data ["age"]
            return jsonify({
                "message":"Student Updated",
                "data":stu
            })
    return jsonify({"message":"Student no found"})


@app.route("/stuDelete/<int:id>",methods =["DELETE"])
def deleteStudent(id):
    for stu in students:
        if stu["id"] == id:
            students.remove(stu)
            return jsonify({
                "message":"Student Deleted",
            })
    return jsonify({"message":"Student no found"})

if __name__ =="__main__":
    app.run(debug=True)
    