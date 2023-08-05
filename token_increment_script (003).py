import os
import shutil

dir_path = '/Users/johndoe/Git/LexDAO/LexDAO_Membership_Token/Token_Files' # directory path
n_times = 20 # number of times to copy files
file_name = '0.json' # name of file to start processing from

new_files_list = [] # list to store names of newly created files

def file_increment(dir_path, n_times, file_name):
    assert os.path.exists(dir_path) # check if the directory exists
    os.chdir(dir_path) # change current working directory to specified path
    start_processing = False # flag to determine when to start processing files
    for file in os.listdir(os.curdir): # iterate through all files in the current directory
        if not os.path.isfile(file) or file[0] == ".": # skip non-file and hidden files
            continue
        if file == file_name: # check if the current file is the one specified as file_name
            start_processing = True # set flag to start processing from this file
        if not start_processing: # if flag is not set, continue to next file
            continue
        name, ext = os.path.splitext(file) # get file name and extension
        start_ind = int(name) # get starting index from file name
        for n in range(1, n_times+1): # iterate through number of times specified to copy file
            new_file = os.path.join(os.getcwd(), f"{start_ind+n}{ext}") # create new file name
            shutil.copy(os.path.join(os.getcwd(), file), new_file) # copy current file to new file
            new_files_list.append(new_file) # add new file name to list

    return new_files_list

def new_token_ID(file_increment, new_files_list):
    success = True # flag to track success of function
    for i in new_files_list: # iterate through list of new files
        try:
            with open(i, 'r') as file: # open file for reading
                name = os.path.basename(i) # get base name of file
                name_noext, ext = os.path.splitext(name) # get file name without extension
                new_token_num = str(int(name_noext)).zfill(6) # generate new token number
                new_token = f"    \"TokenID\": {new_token_num},\n" # generate new token string
                data = file.readlines() # read lines of file
                data[2] = new_token # replace third line with new token string
                with open(i, 'w', encoding='utf-8') as file: # open file for writing
                    file.writelines(data) # write updated lines to file
        except Exception as e: # catch any exceptions that occur while processing files
            print(f"An error occurred while processing {i}: {e}") # print error message
            success = False # set flag to False if there is an error
    return success

new_files_list = file_increment(dir_path, n_times, file_name) # call file_increment function and assign output to new_files_list
success = new_token_ID(file_increment, new_files_list) # call new_token_ID function and assign output to success

if success: # check if all functions completed successfully
    print("All functions completed successfully.")
else:
    print("One or more functions did not complete successfully.") # print error message if one or more functions did not complete successfully
