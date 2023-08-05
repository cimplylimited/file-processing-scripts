import os
import shutil

dir_path = '/Users/johndoe/Git/LexDAO/LexDAO_Membership_Token/Token_Files' 
n_times = 10
file_name = '0.json'


def file_increment(dir_path, n_times, file_name='0.json'):
    new_files_list = [] # create empty list for new files
    if not os.path.exists(dir_path):
        raise ValueError(f"Directory '{dir_path}' does not exist.")
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
    return new_files_list

def new_token_ID(file_path):
    with open(file_path, 'r') as file:
        name = os.path.basename(file_path)
        name_noext, ext = os.path.splitext(name)
        new_token_num = str(int(name_noext)).zfill(6)  
        new_token = f"    \"TokenID\": {new_token_num},\n"
        data = file.readlines()
        data[2] = new_token
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(data)

new_files_list = file_increment(dir_path, n_times)
for file_path in new_files_list:
    new_token_ID(file_path)
