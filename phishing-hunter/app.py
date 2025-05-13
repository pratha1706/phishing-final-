from flask import Flask, render_template, request
import os
from detector import model, ocr_analysis, utils
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        if 'screenshot' not in request.files:
            return render_template("index.html", result="No file uploaded")

        file = request.files['screenshot']
        if file.filename == '':
            return render_template("index.html", result="No selected file")

        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        image_result = model.predict_image(filepath)
        text = ocr_analysis.extract_text(filepath)
        ocr_result = ocr_analysis.analyze_text(text)
        domain_result = utils.check_domain_similarity(filename)

        result = {
            "image_result": image_result,
            "ocr_score": ocr_result['score'],
            "ocr_findings": ocr_result['findings'],
            "domain_similarity": domain_result
        }

    return render_template("index.html", result=result)

if __name__ == '__main__':
    app.run(debug=True)
