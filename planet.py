class Planet:
	def __init__(self):
		self.population = 1
		self.population_growth = 1.1
		self.population_list = []
		
	def step(self):
		self.population = self.population * self.population_growth
		
	def run(self, iterations):
		self.step(iterations)
		self.population_list.append(self.population)
