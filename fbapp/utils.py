import random
import os
import textwrap
from PIL import Image, ImageDraw, ImageFont
from fbapp.models import Content, Gender

def find_content(gender):
	contents = Content.query.filter(Content.gender == Gender[gender]).all()
	return random.choice(contents)

class OpenGraphImage:
	colors = ['#C0392B', '#4A235A', '#1A5276', '#21618C', '#117864', '#0E6655', '#196F3D', '#1D8348', '#9A7D0A', '#9C640C', '#935116', '#BA4A00', '#212F3C', '#212F3D', '#424949']

	def __init__(self, uid,  first_name, description):
		self.location = self._location(uid)
		background = self.base()
		self.print_on_img(background, first_name.capitalize(), 70, 50)
		sentences = textwrap.wrap(description, width=60)
		current_h, pad = 180, 10
		for sentence in sentences:
			w, h = self.print_on_img(background, sentence, 40, current_h)
			current_h += h + pad

		background.save(self._path(uid), quality=90)

	def base(self):
		img = Image.new('RGB',(1200,630), random.choice(self.colors))
		return img


	def print_on_img(self, img, text, size, height):
		font = ImageFont.truetype(os.path.join('fbapp', 'static', 'fonts', 'Arcon-Regular.otf'), size)
		draw = ImageDraw.Draw(img)
		w,h = draw.textsize(text,font)
		position = ((img.width - w) / 2 , height)
		draw.text(position, text, (255,255,255), font=font)
		return (w, h)

	def _path(self, uid):
		return os.path.join('fbapp', 'static', 'tmp', '{}.jpg'.format(uid))

	def _location(self, uid):
		return 'tmp/{}.jpg'.format(uid)