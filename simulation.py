import random
import sys
random.seed(42)
from person import Person
from logger import Logger
from virus import Virus


class Simulation(object):
  
# init finished
    def __init__(self, pop_size, vacc_percentage, initial_infected, virus):
       
        
        self.population = []  # List of Person objects
        self.pop_size = pop_size  # Int
        self.next_person_id = 0  # Int
        self.virus = virus  # Virus object
        self.initial_infected = initial_infected  # Int
        self.total_infected = 0  # Int
        self.current_infected = 0  # Int
        self.vacc_percentage = vacc_percentage  # float between 0 and 1
        self.total_dead = 0  # Int
        self.file_name = "{}_simulation_pop_{}_vp_{}_infected_{}.txt".format(virus, pop_size, vacc_percentage, initial_infected)
        self.newly_infected = []
        # added this
        self.vacc_int = 0
        self.logger = Logger(self.file_name)
        self.logger.write_metadata(self.pop_size, self.vacc_percentage, virus.name, virus.mortality_rate, virus.repro_rate)

    def _create_population(self, initial_infected):

        infected = 0
        
        while len(self.population) < self.pop_size:
            id = len(self.population) + 1
            if infected < self.initial_infected:

                new_person = Person(id, False, True, virus)
                self.total_infected += 1
                infected += 1
                self.population.append(new_person)
            else:
                if random.random() > self.vacc_percentage:
                    new_person = Person(id, False, False, virus)
                    self.population.append(new_person)
                else:
                    new_person = Person(id, True, False, virus)
                    self.population.append(new_person)

# this method is finished
    def _simulation_should_continue(self):
       
        deadPeople = []
        continueSimulation = True
        for person in self.population:
            if person.is_alive == False:
                deadPeople.append(person)

        if len(deadPeople) == self.pop_size:  # the entire pop. is dead
            continueSimulation = False
        elif self.current_infected == 0:  # no infected people left
            continueSimulation = False
        else:  # otherwise continue simulation
            continueSimulation = True

#  revisit run 
    def run(self):
        
        self._create_population(23)  # this should be empty?
        should_continue = self._simulation_should_continue()
        step_counter = 0    
        while should_continue == True:
            self.time_step()
            step_counter += 1
            should_continue = self._simulation_should_continue()

        print("Stopped the simulation after {} turns.".format(step_counter))
        print("Total infected: {}".format(self.total_infected),
              "Total Dead: {}".format(self.total_dead))
        print("Interactions where indidual as safe from vacciation {}".format(
            self.vacc_int))

        self.logger.log_time_step(self.total_dead, step_counter)


    def time_step(self):
       
        for person in self.population:
            if person.is_alive == True and person.is_infected == True:
                i = 0
                while i < 99:
                    random_person = self.population[random.randint(
                        0, self.population_size - 1)]
                    if random_person.is_alive == True:
                        self.interaction(person, random_person)
                        i += 1
                        # work on the following funcs
        self.person_dies()
        self.person_infected()

    def interaction(self, person, random_person):
      
        if random.random() <= virus.repro_rate and random_person.is_vaccinated == False:
            if random_person.is_infected == False:
                self.total_infected += 1
                self.newly_infected.append(random_person._id)
                self.logger.log_interaction(
                    person, random_person, random_person.is_infected, random_person.is_vaccinated, True)
            else:
                self.logger.log_interaction(
                    person, random_person, random_person.is_infected, random_person.is_vaccinated, True)
        else:
            self.vacc_int += 1
            self.logger.log_interaction(
                person, random_person, random_person.is_infected, random_person.is_vaccinated, False)

    def person_infected(self):
        if len(self.newly_infected) > 0:
            for id in self.newly_infected:
                newid = id-1
                person = self.population[newid]
                person.is_infected = True
        self.newly_infected = []

    def person_dies(self):
        for person in self.population:
            if person.is_infected == True:
                if person.did_survive_infection() == True:
                    self.logger.log_infection_survival(person, False)
                else:
                    self.logger.log_infection_survival(person, True)
                    self.total_dead += 1


    def record_person(self):
        for person in self.population:
            print(person._id, "Alive", person.is_alive, "Vac",person.is_vaccinated, "Inf", person.is_infected)


if __name__ == "__main__":
    
    params = sys.argv[1:]

    virus_name = str(params[0])
    repro_num = float(params[1])
    mortality_rate = float(params[2])

    pop_size = int(params[3])
    vacc_percentage = float(params[4])

    if len(params) == 6:
        initial_infected = int(params[5])

    virus = Virus(virus_name, repro_num, mortality_rate)
    sim = Simulation(pop_size, vacc_percentage, initial_infected, virus)
    sim.run()

virus = Virus("HIV", 0.4, 0.8)
sim = Simulation(30000, 0.1, 23, virus)


# Simulation._create_population(1, initial_infected=10)

# Testing Simulation class inst
def test_class_inst():
    simulation = Simulation(200, 0.75, "Ebola", 1)
    assert simulation.pop_size == 200
    assert simulation.vacc_percentage == 0.75
    assert simulation.initial_infected == 1
    assert simulation.virus == "Ebola"
    assert simulation.total_infected == 0
    assert simulation.logger == None
    assert simulation.population == []
    assert simulation.next_person_id == 0
    assert simulation.total_infected ==0
    assert simulation.total_dead == 0
    assert simulation.file_name == "{}_simulation_pop_{}_vp_{}_infected_{}.txt".format("Ebola", 200, 0.75, 1)
    assert simulation.newly_infected == []


