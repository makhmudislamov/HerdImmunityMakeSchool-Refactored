#!/usr/bin/env python
import pytest
import os



class Logger(object):
    ''' Utility class responsible for logging all interactions during the simulation. '''
    # TODO: Write a test suite for this class to make sure each method is working
    # as expected.

    # PROTIP: Write your tests before you solve each function, that way you can
    # test them one by one as you write your class.



    def __init__(self, file_name):
        self.file_name = file_name


    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate,
                       basic_repro_num):
       
        if os.path.exists(self.file_name):
            writeMode = 'a'
        else:
            writeMode = 'w'

        myLogFile = open(self.file_name, writeMode)
        myString = "pop_size: {0}\t \nvacc_percentage: {1}\t \nvirus_name: {2}\t \nmortality_rate: {3}\t \nbasic_repro_num: {4}\n".format(
            pop_size, vacc_percentage, virus_name, mortality_rate, basic_repro_num)
        myLogFile.write(myString)

        myLogFile.close()


    def log_interaction(self, person, random_person, random_person_sick=None,
                        random_person_vacc=None, did_infect=None):
        '''
        The Simulation object should use this method to log every interaction
        a sick person has during each time step.
        The format of the log should be: "{person.ID} infects {random_person.ID} \n"
        or the other edge cases:
            "{person.ID} didn't infect {random_person.ID} because {'vaccinated' or 'already sick'} \n"
        '''
        # TODO: Finish this method. Think about how the booleans passed (or not passed)
        # represent all the possible edge cases. Use the values passed along with each person,
        # along with whether they are sick or vaccinated when they interact to determine
        # exactly what happened in the interaction and create a String, and write to your logfile.
        outFile = open(self.file_name, "a")

        if random_person_vacc is True:
            outFile.write("{0} is vaccinated, nothing happened!\n".format(random_person._id))
        elif random_person_sick is True:
            outFile.write("{0} is already infected, nothing happened!\n".format(random_person._id))
        elif random_person_vacc is False and random_person_sick is None:
            outFile.write("{0} infected {1}\n!".format(person._id, random_person._id))
        else:
            outFile.write("No interaction logged\n")

    def log_infection_survival(self, person, did_die_from_infection):
        ''' The Simulation object uses this method to log the results of every
        call of a Person object's .resolve_infection() method.
        The format of the log should be:
            "{person.ID} died from infection\n" or "{person.ID} survived infection.\n"
        '''
        # TODO: Finish this method. If the person survives, did_die_from_infection
        # should be False.  Otherwise, did_die_from_infection should be True.
        # Append the results of the infection to the logfile
        outFile = open(self.file_name, "a")

        if did_die_from_infection is False:
            outFile.write("{0} survived!\n".format(person._id))
        elif did_die_from_infection is True:
            outFile.write("AHHH {0} DIED!\n".format(person._id))

    def log_time_step(self, time_step_number):
        ''' STRETCH CHALLENGE DETAILS:
        If you choose to extend this method, the format of the summary statistics logged
        are up to you.
        At minimum, it should contain:
            The number of people that were infected during this specific time step.
            The number of people that died on this specific time step.
            The total number of people infected in the population, including the newly infected
            The total number of dead, including those that died during this time step.
        The format of this log should be:
            "Time step {time_step_number} ended, beginning {time_step_number + 1}\n"
        '''
        # TODO: Finish this method. This method should log when a time step ends, and a
        # new one begins.
        # NOTE: Here is an opportunity for a stretch challenge!
        outFile = open(self.file_name, "a")

        outFile.write("Time step: {0} ended...beginning {1}\n".format(time_step_number, time_step_number + 1))

# TODO: comback and fix this test
def test_logger_instantiation():

    logger = Logger("simulation.txt")
    assert logger.file_name == "simulation.txt"
   

def test_write_metadata():
    logger = Logger("simulation.txt")
    logger.write_metadata(200, 0.45, "HIV", 0.88, 0.23)
       
    file = open("simulation.txt", "r")
    data = file.read()

    # TODO: get this test checked with TA. 
    print(data)
    # here checking the file has 5 lines,
    assert len(data.split(' ')) == 20

    # testing if the file is created >>> it failed, then I wrote logger_file = open(self.file_name, 'w') on line 27, then test passed
    assert file is not None
  

    
