import matplotlib.pyplot as plt

class Planet:
	def __init__(self):
		self.population = 100
		self.birth_rate = 1.1
		self.death_rate = 1.02
		self.population_list = []
		self.total_resources = 1000
		self.total_resources_list = []
			
        
    # def step(self):
	# 	# self.population = self.population * self.population_growth_rate
	# 	self.total_resources -= self.population*0.01
	# 	self.birth_rate = self.total_resources/self.population
	# 	if self.birth_rate > 4:
	# 		self.birth_rate = 4
	# 	# self.death_rate = 1
	# 	self.population *= (self.birth_rate)/(self.death_rate)
	# 	self.population_list.append(self.population)

	def step(self):
		self.population *= self.birth_rate
		ratio = self.population/self.total_resources
		if ratio > 1.3:
			self.population /= ratio
		self.population_list.append(self.population)


	def render(self):
		plt.plot(self.population_list)
