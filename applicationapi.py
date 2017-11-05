from flask import Flask, request, jsonify
from flask_cors import CORS

application = Flask(__name__)
CORS(application)

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
		filename = request.args.get('filename')
		textfilename = filename + '.txt'
		print(filename)
		d = path.dirname(__file__)
	    # Read the whole text.
		text = open(path.join(d, textfilename), 'r').read()
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
		imagename = filename + '.jpg'
		image = wordcloud.to_file(imagename)

		# response = send_file(tempFileObj, as_attachment=True, attachment_filename='mcDaniels.jpg')
		return jsonify({
			'image_name': imagename
			})

	except:
		return jsonify({
			'response_code': 'error'
			})







if __name__ == '__main__':
	application.run(debug=True)