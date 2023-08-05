#note that this is a Python script that requires a seed file called '0.[extension]'.  For this example
#the file uses a 0.json file

import os
import shutil

dir_path ='/Users/johndoe/Git/LexDAO/LexDAO_Membership_Token/Image_Files' 
n_times = 250



def do_copy(dir_path, n_times):
    assert os.path.exists(dir_path)
    os.chdir(os.path.join(os.getcwd(), dir_path))
    for file in os.listdir(os.curdir):
        if not os.path.isfile(file) or file [0] == ".":  # only change names if it's a file or not a .file
            continue
        name, ext = os.path.splitext(file)
        print("This is the original file name: ", name)
        start_ind = int(name)
        for n in range(1, n_times+1):
            new_file = os.path.join(os.getcwd(), f"{start_ind+n}{ext}") #may want to remove the extension bc of how things get minted
            shutil.copy(os.path.join(os.getcwd(), file), new_file)

do_copy(dir_path, n_times) 



