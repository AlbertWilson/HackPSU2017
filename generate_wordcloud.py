#!/usr/bin/env python
"""
Generate a square wordcloud from a text file containing professor reviews.
"""

from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def generate_wordcloud(filename):
    d = path.dirname(__file__)

    # Read the whole text.
    text = open(path.join(d, filename)).read()
    # Generate a word cloud image
    wordcloud = WordCloud().generate(text)

    # Display the generated image:
    # the matplotlib way:
    # plt.imshow(wordcloud, interpolation='bilinear')
    # plt.axis("off")

    # lower max_font_size
    # wordcloud = WordCloud(max_font_size=40).generate(text)
    # plt.figure()
    # # plt.imshow(wordcloud, interpolation="bilinear")
    # plt.axis("off")
    # # plt.show()

    # # The pil way (if you don't have matplotlib)
    # image = wordcloud.to_image()
    # return image

    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")

    # lower max_font_size
    wordcloud = WordCloud(max_font_size=40).generate(text)
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    print("here")
    plt.show()

generate_wordcloud("mcdaniel_review.txt")
