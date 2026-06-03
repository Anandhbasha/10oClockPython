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
if __name__ =="__main__":
    app.run(debug=True)
    