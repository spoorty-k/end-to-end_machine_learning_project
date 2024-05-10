import os
# from .. import logger
from src.components import *
print("Parent directory is ")
print("\n")
cwd = os.getcwd()
print("Current Directory is: ", cwd)

# find the parent directory
print("Parent Directory is: ", 
os.path.abspath(os.path.join(cwd, os.pardir))) 
print('Absolute path of file:     ', 
      os.path.abspath(__file__))
print("end of parent directory")



print("\n finding path:")
import os
pythonfile = 'dataingestion.py'
 
# if the file is present in current directory,
# then no need to specify the whole location
print("Path of the file..", os.path.abspath(pythonfile))
 
for root, dirs, files in os.walk(r'c:\Users\Kalespo\Downloads\MLProjects\src'):
    for name in files:
       
          # As we need to get the provided python file, 
        # comparing here like this
        if name == pythonfile:  
            print(os.path.abspath(os.path.join(root, name)))