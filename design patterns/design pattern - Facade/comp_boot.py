class ProcessingUnit:
    '''Subsystem #1'''

    def process(self):
        print("Processing...")

class DisplayUnit:
    '''Subsystem #2'''

    def display(self):
        print("Displaying...")

class Memory:
    '''Subsystem #3'''

    def ioOperation(self):
        print("Reading and writing to memory...")

class Computer:
    '''Facade'''
    def __init__(self):
        self.processingUnit = ProcessingUnit()
        self.displayUnit = DisplayUnit()
        self.memory = Memory()

    def bootUp(self):
        self.processingUnit.process()
        self.memory.ioOperation()
        self.displayUnit.display()

computer = Computer()
computer.bootUp()