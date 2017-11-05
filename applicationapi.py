from flask import Flask, request, jsonify

application = Flask(__name__)

@application.route('/')
def index():
	return "Hello World!"

from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from tempfile import NamedTemporaryFile
from shutil import copyfileobj

@application.route('/generateWordCloud')
def generate_wordcloud():
	try:
		# filename = request.args.get('filename')
		filename = 'mcdaniel_review.txt'
		d = path.dirname(__file__)
	    # Read the whole text.
		text = open(path.join(d, filename), 'r').read()
		# Generate a word cloud image
		wordcloud = WordCloud().generate(text)

		# Display the generated image:
		# the matplotlib way:
		# plt.imshow(wordcloud, interpolation='bilinear')
		# plt.axis("off")
		print("open file")
		# lower max_font_size
		wordcloud = WordCloud(max_font_size=40).generate(text)
		print("get wordcloud")
		plt.figure()
		# plt.imshow(wordcloud, interpolation="bilinear")
		plt.axis("off")
		# plt.show()

		# The pil way (if you don't have matplotlib)
		image = wordcloud.to_file("mcDaniels.jpg")

		# response = send_file(tempFileObj, as_attachment=True, attachment_filename='mcDaniels.jpg')
		return jsonify({
			'image_name': 'mcDaniels.jpg'
			})

	except:
		return jsonify({
			'response_code': 'error'
			})







if __name__ == '__main__':
	application.run(debug=True)