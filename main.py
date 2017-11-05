from flask import Flask, render_template, request, jsonify
from generate_wordcloud import generate_wordcloud
from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
