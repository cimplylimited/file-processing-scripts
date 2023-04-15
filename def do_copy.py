def do_copy(root, n_times):
    os.chdir('/Users/johndoe/Git/LexDAO/LexDAO Membership Token')
    assert os.path.exists(root)
    for file in os.listdir(os.curdir):
        if not os.path.isfile(file):  # only change names if it's a file
            continue
        name, ext = os.path.splitext(file)
        start_ind = int(name)
        for n in range(1, n_times):
            new_file = os.path.join(os.getcwd(), f"{start_ind+n}{ext}")
            shutil.copy(os.path.join(os.getcwd(), file), new_file)


do_copy('/Users/johndoe/Git/LexDAO/LexDAO Membership Token/0', 2)