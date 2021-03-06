#!/usr/bin/env python
# import pytest
import os
from person import Person

class Logger(object):
  
    # checked
    def __init__(self, file_name):
        self.file_name = file_name


    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate,
                       basic_repro_num):

        if os.path.exists(self.file_name):
            writeMode = 'a'
        else:
            writeMode = 'w'

        myLogFile = open(self.file_name, writeMode)
        myString = "pop_size: {0} \nvacc_percentage: {1} \nvirus_name: {2} \nmortality_rate: {3} \nbasic_repro_num: {4}\n".format(
            pop_size, vacc_percentage, virus_name, mortality_rate, basic_repro_num)
        myLogFile.write(myString)

        myLogFile.close()


    def log_interaction(self, person, random_person, random_person_sick,
                        random_person_vacc, did_infect):
       
        outFile = open(self.file_name, "a")

        if random_person_vacc is True:
            outFile.write("{0} is vaccinated, nothing happened!\n".format(random_person._id))
        elif random_person_sick is True:
            outFile.write("{0} is already infected, nothing happened!\n".format(random_person._id))
        elif random_person_vacc is False and random_person_sick is None:
            outFile.write("{0} infected {1}!\n".format(person._id, random_person._id))
        else:
            outFile.write("No interaction logged\n")

    def log_infection_survival(self, person, did_die_from_infection):
      
        outFile = open(self.file_name, "a")

        if did_die_from_infection is False:
            outFile.write("{0} survived!\n".format(person._id))
        elif did_die_from_infection is True:
            outFile.write("AHHH {0} DIED!\n".format(person._id))

    def log_time_step(self, time_step_number):
        
        outFile = open(self.file_name, "a")
        outFile.write("Time step: {0} ended...beginning {1}\n".format(time_step_number, time_step_number + 1))
        

def test_logger_instantiation():


    logger = Logger("simulation.txt")
    assert logger.file_name == "simulation.txt"


    logger = Logger("logger_file.txt")
    assert logger.file_name == "logger_file.txt"



def test_write_metadata():
    logger = Logger("simulation.txt")
    logger.write_metadata(200, 0.45, "HIV", 0.88, 0.23)


    file = open("simulation.txt", "r")
    assert file is not None
    linesInFile = file.readlines()
    lastFiveLinesInFile = linesInFile[-5:]

    for i, line in enumerate(lastFiveLinesInFile):
        splitLine = line.split(" ")
        if i == 0: # current line == 1,
            if "200" in line:
                lineOneArray = splitLine
                assert lineOneArray[1] == "200"
        if i == 1:
            if "0.45" in line:
                lineTwoArray = splitLine
                assert lineTwoArray[1] == "0.45"
        if i == 2:
            if "HIV" in line:
                lineThreeArray = splitLine
                assert lineThreeArray[1] == "HIV"
        if i == 3:
            if "0.88" in line:
                lineFourArray = splitLine
                assert lineFourArray[1] == "0.88"
        if i == 4:
            if "0.23" in line:
                lineFiveArray = splitLine
                assert lineFiveArray[1] == "0.23\n"

def test_log_interaction_():

    logger = Logger("simulation.txt")

    person1 = Person("sam", True, True) # is alive & vaccinated
    person2 = Person("bob", False, False) # is alive & not vaccinated

    logger.log_interaction(person1, person2, False, True)

    logger.log_interaction(person1, person2, True)


    file = open("logger_file.txt", "r")
    data = file.read()

    print(data)


    logger.log_interaction(person1, person2, None, False)

    file = open("simulation.txt", "r")
    assert file is not None

    linesInFile = file.readlines()

