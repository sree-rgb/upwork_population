import random
import pylab
class Individual:
	def __init__(self,generation_number=1):
		self.generation_number=0

	def survive(self):
		return random.choice([None,(Individual(self.generation_number+1),Individual(self.generation_number+1))])
class Population:
	def __init__(self,number_of_people=1000):
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
		self.total_survivors=self.total_survivors+len(generation)
		return len(generation)
	def get_average_number_of_survivors_per_generation(self):
		return self.total_survivors/self.current_generation
def numberOfSurvivors():
	'''
	1. the number of surviving (non-extinct) populations
	For 10 generations.
	'''
	pop=Population(1000)
	new_pop=[]
	for x in range(10):

		new_pop.append(len(pop))
		pop.get_Next_Generation()
	pylab.title('Survivors')
	pylab.xlabel('Generation Number')
	pylab.ylabel('Number of survivors')
	pylab.plot([x for x in range(1,len(new_pop)+1)],new_pop)
	pylab.show()

def averageNumberOfSurvivors(samplesize=10):
	populations = [Population() for x in range(samplesize)]
	number_of_generations=10
	avg_number_of_survivors=[]
	for pop in populations:
		for x in range(number_of_generations):
			pop.get_Next_Generation()
		avg_number_of_survivors.append(pop.get_average_number_of_survivors_per_generation())
	pylab.title('Average no of Survivors for 10 generations')
	pylab.xlabel('Population Sample Number')
	pylab.ylabel('Average Number of survivors')
	pylab.plot([x for x in range(1,len(avg_number_of_survivors)+1)],avg_number_of_survivors)
	pylab.show()
def total_number_of_individuals(samplesize=100,number_of_generations=10):
	populations = [Population() for x in range(samplesize)]
	
	survivors_per_generation=[]
	for generation in range(number_of_generations):
		number_of_survivors=[]
		for pop in populations:
			number_of_survivors.append(pop.get_Next_Generation())
		survivors_per_generation.append(sum(number_of_survivors))
	pylab.title(f'Total number of individuals summed over all surviving populations,for {number_of_generations} generations for a sample size {samplesize}')
	pylab.xlabel('Generation Number')
	pylab.ylabel('Total Number of Survivors')
	pylab.plot([x for x in range(1,number_of_generations+1)],survivors_per_generation)
	pylab.show()

		
if __name__ == '__main__':
	print(total_number_of_individuals(100,50))
