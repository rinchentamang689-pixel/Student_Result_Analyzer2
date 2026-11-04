from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    error = None

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        subjects = ["English", "Mathematics", "Science",
                    "Computer", "Social Studies"]

        try:
            marks = [
                float(request.form.get(subject, ""))
                for subject in subjects
            ]

            if not name:
                raise ValueError("Please enter the student's name.")

            if any(mark < 0 or mark > 100 for mark in marks):
                raise ValueError("Marks must be between 0 and 100.")

            total = sum(marks)
            percentage = total / len(marks)

            # A subject pass mark is 35 out of 100
            passed = all(mark >= 35 for mark in marks)

            if not passed:
                grade = "F"
                status = "Fail"
            elif percentage >= 90:
                grade = "A+"
                status = "Pass"
            elif percentage >= 80:
                grade = "A"
                status = "Pass"
            elif percentage >= 70:
                grade = "B"
                status = "Pass"
            elif percentage >= 60:
                grade = "C"
                status = "Pass"
            elif percentage >= 50:
                grade = "D"
                status = "Pass"
            else:
                grade = "E"
                status = "Pass"

            result = {
                "name": name,
                "subjects": subjects,
                "marks": marks,
                "total": total,
                "percentage": percentage,
                "grade": grade,
                "status": status
            }

        except ValueError as e:
            error = str(e) or "Enter valid marks for every subject."

    return render_template(
        "index.html", result=result, error=error
    )


if __name__ == "__main__":
    app.run(debug=True)
