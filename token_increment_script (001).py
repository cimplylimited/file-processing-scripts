
import os
import shutil

dir_path ='/Users/johndoe/Git/LexDAO/LexDAO_Membership_Token/Token_Files' 
n_times = 10
file_name = '0.json' #currently not used, but further enhancement will allow for this to be included as the start parameter

new_files_list = [] #place for the output of all the duplicated files to feed the new tokenID functions

def file_increment(dir_path, n_times):
    assert os.path.exists(dir_path)
    os.chdir(dir_path)
    for file in os.listdir(os.curdir):
        if not os.path.isfile(file) or file[0] == ".":  # only change names if it's not the named file or not a .file
            continue
        name, ext = os.path.splitext(file)
        start_ind = int(name)
        for n in range(1, n_times+1):
            new_file = os.path.join(os.getcwd(), f"{start_ind+n}{ext}") #may want to remove the extension bc of how things get minted
            shutil.copy(os.path.join(os.getcwd(), file), new_file)
            new_files_list.append(new_file)
            print(new_files_list)
            
        def new_token_ID(file_increment, new_files_list):
            for i in new_files_list:
                
                with open (i, 'r') as file:
                    name = os.path.basename(i)
                    name_noext, ext = os.path.splitext(name)
                    new_token_num = str(int(name_noext)).zfill(6)  
                    new_token = f"    \"TokenID\": {new_token_num},\n"
                    data = file.readlines()
                    data[2] = new_token

                    with open (i, 'w', encoding='utf-8') as file:
                        file.writelines(data)

                        

        new_token_ID(file_increment, new_files_list)
        
file_increment(dir_path, n_times) 

