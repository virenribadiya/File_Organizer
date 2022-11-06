
import os as o
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
