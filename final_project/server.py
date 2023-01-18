from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/english_to_french")
def english_to_french():
    textToTranslate = request.args.get('Hello world')
    return translator.englishToFrench(textToTranslate)

@app.route("/french_to_english")
def french_to_english():
    textToTranslate = request.args.get('Bonjour le monde')
    return translator.frenchToEnglish(textToTranslate)

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
