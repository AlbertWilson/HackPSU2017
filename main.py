from flask import Flask, render_template, request, jsonify, send_file
from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method=='GET':
        return('<form action="/test" method="post"><input type="submit" value="Send" /></form>')

    elif request.method=='POST':
        return "OK this is a post method"
    else:
        return("ok")

@app.route('/generate_wordcloud', methods=['POST'])
def generate_wordcloud():
    d = path.dirname(__file__)

    # Read the whole text.
    text = open(path.join(d, "Patrick McDaniel.txt")).read()
    # Generate a word cloud image
    wordcloud = WordCloud().generate(text)

    # Display the generated image:
    # the matplotlib way:
    # plt.imshow(wordcloud, interpolation='bilinear')
    # plt.axis("off")

    # lower max_font_size
    wordcloud = WordCloud(max_font_size=40).generate(text)
    plt.figure()
    # # plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    # # plt.show()
    #
    # # The pil way (if you don't have matplotlib)
    image = wordcloud.to_image()
    return (image)
    # return "hello"

if __name__ == "__main__":
    app.run(debug=True)
