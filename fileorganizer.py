import os  
import shutil  
import easygui as e 

title="FILE ORGANIZER"
e_msg="Enter Path"
exit="EXIT"
heading="Error"
path=e.enterbox(e_msg,title)   # user input for path of the folder.
if path=="":
	e.msgbox("Please! Try Again!",heading,exit)
else:		
    ls=os.listdir(path)
    for i in ls:
	name,ext=os.path.splitext(i)
	ext=ext[1:] #for example .pdf----->pdf
	if ext=="": #skipping a folder.
	    continue
	elif os.path.exists(path+"/"+ext):
	    shutil.move(path+"/"+i,path+"/"+ext+"/"+i)
	else:
	    os.makedirs(path+"/"+ext)
	    shutil.move(path+"/"+i,path+"/"+ext+"/"+i)
    but="Good Job!"
    e.msgbox("Excecution Successful!!","",but)
	
