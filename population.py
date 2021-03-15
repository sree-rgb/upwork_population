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

if __name__ == '__main__':

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
