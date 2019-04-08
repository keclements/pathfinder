from PIL import image, ImageDraw

class Map:

	def __init__(self, filename):
		self.elevations = self.get_elevations(filename)
        self.max_elevation = self.get_max_elevation()
        self.min_elevation = self.get_min_elevation()
		with open(filename) as file:
			self.elevations = [[int(e) for 

