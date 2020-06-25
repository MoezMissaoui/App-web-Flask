import random
import os
import textwrap
from PIL import Image, ImageDraw, ImageFont
from fbapp.models import Content, Gender

def find_content():
	contents = Content.query.all()
	return random.choice(contents)

def find_color(gender):
	colors = Colors.query.filter(Colors.gender == Gender[gender]).all()
	return random.choice(colors)

class OpenGraphImage:
	PATH_imgs = os.path.join('fbapp', 'static', 'tmp')

	def __init__(self , first_name, description, color):
		# Take the image name
		image_name = self.get_image_name()
		self.img_name = image_name
		self.location = self._location(image_name)
		background = self.base()
		self.print_on_img(background, first_name.capitalize(), 70, 50)
		sentences = textwrap.wrap(description, width=60)
		current_h, pad = 180, 10
		for sentence in sentences:
			w, h = self.print_on_img(background, sentence, 40, current_h)
			current_h += h + pad

		background.save(self._path(image_name), quality=90)

	def base(self, color):
		img = Image.new('RGB',(1200,630), color)
		return img


	def print_on_img(self, img, text, size, height):
		font = ImageFont.truetype(os.path.join('fbapp', 'static', 'fonts', 'Arcon-Regular.otf'), size)
		draw = ImageDraw.Draw(img)
		w,h = draw.textsize(text,font)
		position = ((img.width - w) / 2 , height)
		draw.text(position, text, (255,255,255), font=font)
		return (w, h)

	def _path(self, image_name):
		return os.path.join('fbapp', 'static', 'tmp', '{}.jpg'.format(image_name))

	def _location(self, image_name):
		return 'tmp/{}.jpg'.format(image_name)

	# The get_image_name() function check the existance of random name (sequence of 15 digits) in the directory of saving. If existe take an other random name
	def get_image_name(self):

		# existfiles = list(filter(lambda file : os.path.isfile(os.path.join(self.PATH_imgs, file)) , os.listdir(self.PATH_imgs) ))
		existfiles = [file for file in os.listdir(self.PATH_imgs) if os.path.isfile(os.path.join(self.PATH_imgs, file)) ]
		
		# existfiles = list(map(lambda file : os.path.splitext(file)[0] , existfiles ))
		existfiles = [os.path.splitext(file)[0] for file in existfiles]

		image_name = str(random.randrange(100000000000000,999999999999999))
		while image_name in existfiles  :
			image_name = str(random.randrange(100000000000000,999999999999999))

		return image_name
