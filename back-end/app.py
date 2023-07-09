from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import os

app = Flask(__name__, static_folder="../front-end", static_url_path="", template_folder="../front-end")

@app.route("/")
def home():
    return render_template("index.html")

UPLOAD_FOLDER = 'resumes'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/getRecommendations", methods=["POST"])
def get_recommendations():
    # Get other form inputs
    location = request.form.get("location")
    job_title = request.form.get("jobTitle")
    salary = request.form.get("salary")
    seniority_level = request.form.get("seniorityLevel")

    # Handle uploaded resume
    resume_file = request.files["resume"]
    if resume_file:
        filename = secure_filename(resume_file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        resume_file.save(filepath)

        # Process the uploaded resume using LLM or Lang Chain
        parsed_resume = process_resume(filepath)

        # Further processing and recommendations based on parsed resume
        # ...

    return jsonify(recommendations)

if __name__ == "__main__":
    app.run(debug=True)
