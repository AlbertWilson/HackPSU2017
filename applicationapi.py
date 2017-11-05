from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 as Features

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

@application.route('/classifyText')
def classifyText():

	try:

		print "classifyText() is called."

		filename = request.args.get('filename')
		textfilename = filename + '.txt'
		print(filename)
		d = path.dirname(__file__)

		natural_language_understanding = NaturalLanguageUnderstandingV1(
	  	username="0cd3961f-df67-403b-8c6f-0921bc01c569",
	  	password="wQQjKUkjp2Kp",
	  	version="2017-02-27")

		fp = open(textfilename, "r")
		text = fp.read()

		response = natural_language_understanding.analyze(
		  text=text,
		  features=[
		    Features.Entities(
		      emotion=True,
		      sentiment=True,
		      limit=2
		    ),
		    Features.Keywords(
		      emotion=True,
		      sentiment=True,
		      limit=2
		    )
		  ]
		)
		json_response = response
		print json_response
		final_string = json.dumps(response)
		# return jsonify(result = str(final_string))
		# return jsonify(result = str(final_string))
		return jsonify({
			'classified_text': final_string
			})

	except:
		return jsonify({
			'response_code': 'error'
			})




	# try:
	# 	filename = request.args.get('filename')
	# 	textfilename = filename + '.txt'
	# 	print(filename)
	# 	d = path.dirname(__file__)
	#
	# 	natural_language_understanding = NaturalLanguageUnderstandingV1(
	# 	  username="0cd3961f-df67-403b-8c6f-0921bc01c569",
	# 	  password="wQQjKUkjp2Kp",
	# 	  version="2017-02-27")
	#
	# 	fp = open(textfilename, "r")
	# 	text = fp.read()
	#
	# 	response = natural_language_understanding.analyze(
	# 	  text=text,
	# 	  features=[
	# 	    Features.Entities(
	# 	      emotion=True,
	# 	      sentiment=True,
	# 	      limit=2
	# 	    ),
	# 	    Features.Keywords(
	# 	      emotion=True,
	# 	      sentiment=True,
	# 	      limit=2
	# 	    )
	# 	  ]
	# 	)
	# 	json_response = response
	# 	print json_response.keys()
	# 	final_string = json.dumps(response)
	# 	# return jsonify(result = str(final_string))
	# 	# return jsonify(result = str(final_string))
	# 	return jsonify({
	# 		'classified_text': final_string
	# 		})
	#
	# except:
	# 	return jsonify({
	# 		'response_code': 'error'
	# 		})







if __name__ == '__main__':
	application.run(debug=True)
