import os
def renameFiles():
    file_path = os.getcwd();
    print file_path;
    os.chdir(r"C:\Users\rkrde\Atom Projects\prank");
    #1 get filenames from folder
    file_list = os.listdir(r"C:\Users\rkrde\Atom Projects\prank")
    print file_list
    #2 for  file rename filename
    for file_name in file_list:
        os.rename(file_name,file_name.translate(None,"0123456789"));
    os.chdir(file_path)
renameFiles()
