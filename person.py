import random
random.seed(42)
from virus import Virus


class Person(object):
    ''' Person objects will populate the simulation. '''

    def __init__(self, _id, is_alive, is_vaccinated, infection=None):
        ''' We start out with is_alive = True, because we don't make vampires or zombies.
        All other values will be set by the simulation when it makes each Person object.
        If person is chosen to be infected when the population is created, the simulation
        should instantiate a Virus object and set it as the value
        self.infection. Otherwise, self.infection should be set to None.
        '''
        self._id = _id  # int
        self.is_alive = is_alive  # boolean
        self.is_vaccinated = is_vaccinated  # boolean
        self.infection = infection  # Virus object or None

    def did_survive_infection(self):
        ''' Generate a random number and compare to virus's mortality_rate.
        If random number is smaller, person dies from the disease.
        If Person survives, they become vaccinated and they have no infection.
        Return a boolean value indicating whether they survived the infection.
        '''
        # Only called if infection attribute is not None.
        # TODO:  Finish this method. Should return a Boolean
        # if self.infection is not None:



# simple unit tests to ensure your Person class initializer works correctly
def test_vacc_person_instantiation():
    # create some people to test if our init method works as expected
    person = Person(1, True, True)
    assert person._id == 1
    assert person.is_alive == True
    assert person.is_vaccinated == True
    assert person.infection == None


def test_not_vacc_person_instantiation():
    person = Person(2, True, False)
    # TODO: complete your own assert statements that test
    # the values at each attribute
    assert person._id == 2
    assert person.is_alive is True
    assert person.is_vaccinated is False
    assert person.infection is None


def test_sick_person_instantiation():
    # Create a Virus object to give a Person object an infection
    virus = Virus("Dysentery", 0.7, 0.2)
    assert virus.name == "Dysentery"
    assert virus.repro_rate == 0.7
    assert virus.mortality_rate == 0.2
    # Create a Person object and give them the virus infection
    person = Person(3, False, False, virus)
    # TODO: complete your own assert statements that test
    # the values at each attribute
    assert person._id == 3
    assert person.is_alive is False
    assert person.is_vaccinated is False
    assert person.infection == virus

def test_did_survive_infection():
    # TODO: Create a Virus object to give a Person object an infection
    virus = Virus("Dysentery", 0.7, 0.2)
    # TODO: Create a Person object and give them the virus infection
    person = Person(4, False, virus)

    # Resolve whether the Person survives the infection or not
    survived = person.did_survive_infection()
    # Check if the Person survived or not
    if survived:
        # MAKHMUD is coding

        # TODO: Write your own assert statements that test
        # the values of each attribute for a Person who survived
        assert person.is_vaccinated == True
        assert person.infection == virus
        assert person.is_alive is True
    else:

        # TODO: Write your own assert statements that test
        # the values of each attribute for a Person who did not survive
        # assert person.is_vaccinated == False
        # assert person.infection == virus
        assert person.is_alive is False
