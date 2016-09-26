# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 12:48:12 2016

@author: RAVI TEJA
"""
from shutil import copyfile
import sys
import os.path

print "Enter your choice. 1. Create a destination file. 2.Copy the whole file. 3.Only Few Lines. 4. Whole file with few corrections. 5.Insert few additional data"
x = int(raw_input("Enter your Choice number:"))

#For creation of new target file.
if x == 1:
    def create():
        print "Create a new output file"
        print("creating new destination file")
        name=raw_input ("Enter the name of file:")
        extension=raw_input ("Enter (valid) extension of file:")
        try:
            name2=name+"."+extension
            file=open(name2,'a')

            file.close()
        except:
            print("Error occured")
            sys.exit(0)

    create()
    
#Copying the whole file to the new traget file
if x == 2:
    
    #from shutil import copyfile
    src = raw_input("Enter Source File name(Mention Path if it is in different folder)")
    dest = raw_input("Enter Destination File name(Mention Path if it is in different folder)")
    if os.path.exists(src):
        if os.path.exists(dest):
            copyfile(src, dest)
        else:
            print "destination path doesn't exist"
    else:
        print "Source Path Doesn't exist"

#Copying only specific lines to the new target file      
elif x ==3:
    
    src = raw_input("Enter Source File name(Mention Path if it is different)")
    dest = raw_input("Enter Destination File name(Mention Path if it is different)")
    if os.path.exists(src):
        if os.path.exists(dest) and (src != dest):
            f1 = open(src, "r+")
            f2 = open(dest, "w")            #Use "a" (append) mode if you want to append data to existing file
            l1 = int(raw_input("Enter the starting line number:"))
            l2 = int(raw_input("Enter the ending line number:"))
            if l2 > l1:
                for i in range (l2+1):
                    buf = f1.readline()
                    if i >=l1:
                        f2.write(str(buf))
            
            elif l2 == l1:
                for i in range (l2+1):
                    buf = f1.readline()
                    if i == l1:
                        f2.write(str(buf))                
             
            else:
                 pass
            f2.close()
            f1.close()
        else:
            print "Destination path doesn't exist or Source and destination are same"
    else:
        print "Source Path Doesn't exist"

#Replacement of old data with new data
elif x == 4:
    src = raw_input("Enter Source File name(Mention Path if it is in different folder)")
    dest = raw_input("Enter Destination File name(Mention Path if it is in different folder)")
    if os.path.exists(src):
        if os.path.exists(dest):
            
            f = open(src,'r')
            filedata = f.read()
            f.close()
            old_data = str(raw_input("Enter the old data to get replaced:"))
            new_data = str(raw_input("Enter the new data to be replaced in:" ))
            data = filedata.replace(old_data,new_data)

            f = open(dest,'w')
            f.write(data)
            f.close()
        else:
            print "Destination path doesn't exist"
    else:
        print "Source Path Doesn't exist"

#Inserting Data at specific lines.
elif x == 5:
    src = raw_input("Enter Source File name(Mention Path if it is in different folder)")
    dest = raw_input("Enter Destination File name(Mention Path if it is in different folder)")
    if os.path.exists(src):
        if os.path.exists(dest):
            f = open(src, "r")
            contents = f.readlines()
            f.close()
            position = int(raw_input("Enter the line number/position for insertion:"))
            data = str(raw_input("Enter the data to be inserted at this position:"))
            contents.insert(position, data + '\n') # '\n' used to move current line to next line. It can be removed if expected, the new data appended to data at old line

            f = open(dest, "w")
            contents = "".join(contents)
            f.write(contents)
            f.close()
            
        else:
            print "Destination path doesn't exist"
    else:
        print "Source Path Doesn't exist"
    

else:
    print "You have entered a wrong choice"


#Copy only few lines
#Re-wrte few words
#Append the new data