from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from generate_wordcloud import generate_wordcloud

app = Flask(__name__)
Bootstrap(app)

@app.route("/")
def hello():
    wordcloud = generate_wordcloud()
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
