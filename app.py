from flask import Flask, render_template, request
import qrcode


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        text = request.form.get("input_text")
        qrcode.make(text).save("static/.svg")
        return render_template("index.html", image_avilable=True)
    return render_template("index.html", image_avilable=False)


if __name__ == "__main__":
    app.run(debug=True)
