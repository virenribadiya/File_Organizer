// The OS module in Python provides functions for interacting with the operating system. OS comes under Python's standard utility modules.
import os as o 
// The shutil module offers a number of high-level operations on files and collections of files.
import shutil as s

path=input('Enter Your Path:')
list_dir=o.listdir(path)
print(list_dir)
for i in list_dir:
	name,ext=o.path.splitext(i)
	ext=ext[1:]
	if o.path.exists(path+"/"+ext):
		s.move(path+"/"+i,path+"/"+ext+"/"+i)
	else:
		o.makedirs(path+"/"+ext)
		s.move(path+"/"+i,path+"/"+ext+"/"+i)
