import os, inspect, sys
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
print currentdir
parentdir = os.path.dirname(currentdir)
print parentdir
sys.path.insert(0,parentdir)