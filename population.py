import random
import pylab
class Individual:
	def __init__(self,generation_number=1):
		self.generation_number=0

	def survive(self):
		return random.choice([None,(Individual(self.generation_number+1),Individual(self.generation_number+1))])
class Population:
	def __init__(self):
		number_of_people=1 # IMPORTANT
		self.individuals=[]
		self.current_generation=1

		for x in range(number_of_people):
			self.individuals.append(Individual(1))
		self.total_survivors=number_of_people
	def __len__(self):
		return len(self.individuals)
	def get_Next_Generation(self):
		generation=[]
		for gn in self.individuals:
			temp=gn.survive()
			if temp:
				for x in [*temp]:
					generation.append(x)
		self.current_generation+=1
		self.individuals=generation
		return len(generation)
	def get_average_number_of_survivors_per_generation(self):
		return self.total_survivors/self.current_generation
def numberOfSurvivors(number_of_generations=100):
	'''
	1. the number of surviving (non-extinct) populations
	per generation.
	'''
	replicate_populations=[Population() for x in range(1000)]
	total_number_of_surviving_populations=[]
	for x in range(number_of_generations):
		number_of_surviving_populations=0
		for pop in replicate_populations:
			if (pop.get_Next_Generation()):
				number_of_surviving_populations+=1
		total_number_of_surviving_populations.append(number_of_surviving_populations)
	pylab.title('Number of Surviving Populations per generation')
	pylab.xlabel('Generation Number')
	pylab.ylabel('Number of surviving populations')
	pylab.plot([x for x in range(1,len(total_number_of_surviving_populations)+1)],total_number_of_surviving_populations)
	pylab.show()

def averageNumberOfSurvivors(number_of_generations=100):
	'''
	The average number of individuals per surviving population
	'''
	replicate_populations=[Population() for x in range(1000)]
	avg_individuals_survived=[]
	for x in range(number_of_generations):
		no_of_individuals_survived=0
		number_of_surviving_populations=0
		for pop in replicate_populations:
			temp=pop.get_Next_Generation()
			if temp:
				number_of_surviving_populations+=1
			no_of_individuals_survived+=temp
		avg_individuals_survived.append(no_of_individuals_survived/number_of_surviving_populations)
				

	pylab.title(f'Average no of Survivors for {number_of_generations} generations')
	pylab.xlabel('Generation Number')
	pylab.ylabel('Average Number of survivors')
	pylab.plot([x for x in range(1,len(avg_individuals_survived)+1)],avg_individuals_survived)
	pylab.show()
def total_number_of_individuals(number_of_generations=100):

	'''
	The total number of individuals summed over all surviving populations, all as functions of the number of elapsed generations
	'''
	replicate_populations=[Population() for x in range(1000)]
	total_individuals_survived=[1000]
	for x in range(number_of_generations):
		no_of_individuals_survived=0
		number_of_surviving_populations=0
		for pop in replicate_populations:
			temp=pop.get_Next_Generation()
			if temp:
				number_of_surviving_populations+=1
			no_of_individuals_survived+=temp
		total_individuals_survived.append(no_of_individuals_survived)

	pylab.title(f'Total no of Survivors for {number_of_generations} generations')
	pylab.xlabel('Generation Number')
	pylab.ylabel('Total Number of survivors summed')
	pylab.plot([x for x in range(len(total_individuals_survived))],total_individuals_survived)
	pylab.show()
		
if __name__ == '__main__':
	print(total_number_of_individuals())
