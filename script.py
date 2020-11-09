from os import listdir
from os.path import isfile, join

# Insert the path to the directory in the variable below
# e.g = /home/matheus/Documentos/Workspace/Projects/read-files
mypath = 'Insert the path here'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

# You can change the name of the text file that will be generate by changing the first parameter of the code below
file_object = open('ListOfFiles', 'a')

for n in range(len(onlyfiles)):
    file_object.write(onlyfiles[n] + "\n")

print(onlyfiles)