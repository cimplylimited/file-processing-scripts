import os

#This is getting the current working directory
print(os.getcwd())


#This is changing the directory from above
os.chdir('/Users/johndoe/Git/LexDAO/LexDAO Membership Token')

'''
#trying to copy file and then increment the name by +1 each copy and run for a specified range
for file in os.listdir():
    name, ext = os.path.splitext(file)
    value = int(name)
    for i in range (0, 10):
            i += 1
    new_name = f"{i}{ext}"
    
    print(new_name)
''' 





#Shows all the files in the Directory
'''
print(os.listdir())
'''

#helps clean the list of the files vs. above
'''
for file in os.listdir():
    print(file)
'''


#This splits the text of the extension and the file name
'''
for file in os.listdir():
    name, ext = os.path.splitext(file)
    print(name)
    print(ext)
'''

#this is to reformat the file to move the names around
'''
for file in os.listdir():
    name, ext = os.path.splitext(file)
    splitted = name.split("-")
    splitted = [s.strip() for s in splitted]
    new_name = f"{splitted[3].zfill(5)}-{splitted[1]}-{splitted[0]}-{splitted[2]}{ext}"
    print(new_name)
'''

'''
#this will expand on the above code and rename the files
for file in os.listdir():
    name, ext = os.path.splitext(file)
    splitted = name.split("-")
    splitted = [s.strip() for s in splitted]
    new_name = f"{splitted[3].zfill(5)}_{splitted[2]}_{splitted[0]}_{splitted[1]}{ext}"
    os.rename(file, new_name)
'''


            
#for value in range (10):
#    print(value)





#checks if an object is iterable
'''
file_name = os.listdir()

def is_iterable(file_name):
    try:
        iter(file_name)
        return True
    except TypeError:
        return False

print(is_iterable(2))    
'''



'''
for file in os.listdir():
    name, ext = os.path.splitext(file)
        for name in os.path.splitext(file):


print(file_name)
print(name)
print(ext)
'''

#for file in os.listdir():
#   name, ext = os.path.splitext(file)
    
        