import os
def rename_files():
    # (1) get files name from the folder
    file_list = os.listdir("/Users/wellswang/Documents/Python/Udacity/prank")
    #print(file_list)
    saved_path = os.getcwd()
    print("Current Working Directory is" + saved_path)
    os.chdir("/Users/wellswang/Documents/Python/Udacity/prank")

    # (2) for each files, rename filename
    for file_name in file_list:
        os.rename(file_name,file_name.translate(None,"0123456789"))
    os.chdir(saved_path)              
rename_files()

