from flask import Flask, render_template, request, redirect

app = Flask(__name__)

students = {}


# Home Page
@app.route("/")
def home():
    return render_template("index.html", students=students)


# Add Student
@app.route("/add", methods=["POST"])
def add_student():

    roll = request.form["roll"]

    if roll in students:
        return "Student already exists!"

    name = request.form["name"]
    age = int(request.form["age"])

    python = float(request.form["python"])
    maths = float(request.form["maths"])
    english = float(request.form["english"])

    students[roll] = {
        "name": name,
        "age": age,
        "python": python,
        "maths": maths,
        "english": english
    }

    return redirect("/")


# Search Student
@app.route("/search", methods=["POST"])
def search_student():

    roll = request.form["search_roll"]

    if roll in students:
        student = students[roll]

        total = (
            student["python"]
            + student["maths"]
            + student["english"]
        )

        percentage = (total / 300) * 100
        average = total / 3

        return render_template(
            "index.html",
            students=students,
            result=student,
            roll=roll,
            total=total,
            percentage=percentage,
            average=average
        )

    return render_template(
        "index.html",
        students=students,
        message="Student not found!"
    )


# Delete Student
@app.route("/delete/<roll>")
def delete_student(roll):

    if roll in students:
        del students[roll]

    return redirect("/")


# Update Student
@app.route("/update/<roll>", methods=["POST"])
def update_student(roll):

    if roll in students:

        students[roll]["name"] = request.form["name"]
        students[roll]["age"] = int(request.form["age"])

        students[roll]["python"] = float(
            request.form["python"]
        )

        students[roll]["maths"] = float(
            request.form["maths"]
        )

        students[roll]["english"] = float(
            request.form["english"]
        )

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)