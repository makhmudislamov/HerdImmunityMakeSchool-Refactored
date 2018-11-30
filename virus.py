#!/usr/bin/env python
import pytest


class Virus(object):
    '''Properties and attributes of the virus used in Simulation.'''

    def __init__(self, name, repro_rate, mortality_rate):
        self.name = name
        self.repro_rate = repro_rate
        self.mortality_rate = mortality_rate

# ERIK's test
def test_virus_instantiation():
    '''Check to make sure that the virus instantiator is working.'''
    virus = Virus("Ebola", 0.22, 0.7)
    assert virus.name == "Ebola"
    assert virus.repro_rate == 0.22
    assert virus.mortality_rate == 0.7

# MAKHMUD's test
def test_virus_tuberculosis():
    virus = Virus("Tuberculosis", 0.55, 0.67)
    assert virus.name == "Tuberculosis"
    assert virus.repro_rate == 0.55
    assert virus.mortality_rate == 0.67
