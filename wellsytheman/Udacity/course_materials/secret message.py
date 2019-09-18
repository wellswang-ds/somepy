import os

def rename_files2():
    file_list = os.listdir("/Users/wellswang/Documents/Python--Udacity/secret message")
    #print(file_list)
    saved_path = os.getcwd()
    print("Current Working directory" + saved_path)
    os.chdir("/Users/wellswang/Documents/Python--Udacity/secret message")
    for file_name in file_list:
        os.rename(file_name,file_name.translate(None,"0123456789"))
    os.chdir(saved_path)

rename_files2()
