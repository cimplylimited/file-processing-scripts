import os
import linecache

dir_path = '/Users/johndoe/Git/LexDAO/LexDAO_Membership_Token'
file_name = '0.json'

def old_token_ID(dir_path, file_name):
    assert os.path.exists(dir_path) #throws an error if the path in the dir_path argument does not exist
    print(os.getcwd()) 
    os.chdir(str(dir_path)) #changes the working directory to the path in the dir_path argument
    try:
        line = linecache.getline(file_name, 3, module_globals=None) #grabs a line of code from the file
        return(line)
    except Exception as e:
        print(e)

def get_token_ID(dir_path, file_name):
    assert os.path.exists(dir_path) #throws an error if the path in the dir_path argument does not exist
    print(os.getcwd()) 
    os.chdir(str(dir_path)) #changes the working directory to the path in the dir_path argument
    try:
        line = linecache.getline(file_name, 3, module_globals=None) #grabs a line of code from the file
        formatted_line = line.replace(",", "") #fixes the syntax of the file

        return(formatted_line) #returns a formatted value for the line inside the file
            
    except Exception as e:
        print(e)

def new_token_ID(get_token_ID, dir_path, file_name):
    TokenID = get_token_ID(dir_path, file_name)
    key, value = TokenID.split(':', 1)
    new_token_value = str(int(value) + 1).zfill(6)    
    new_token = f"    \"TokenID\": {new_token_value},\n"
    return(new_token)

def write_new_token_ID(new_token_ID, dir_path, file_name):
    json_file_contents = []
    with open(file_name, 'r') as file:
        for line in file.readlines():
            json_file_contents.append(line)

    print(json_file_contents)
    print('\n'*2)    
    
    change_to_newtoken = []

    for token in json_file_contents:
        nexttoken = token.replace(b,c)
        change_to_newtoken.append(nexttoken)

    print(change_to_newtoken)

    with open(file_name, 'w') as f:
        for i in change_to_newtoken:
            f.write(i)


a = get_token_ID(dir_path, file_name)
b = old_token_ID(dir_path,file_name)
c = new_token_ID(get_token_ID, dir_path, file_name)
d = write_new_token_ID(new_token_ID, dir_path, file_name)
