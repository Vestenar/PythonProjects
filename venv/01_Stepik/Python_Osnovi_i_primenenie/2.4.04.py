import os
import os.path
import shutil  #  библиотека методов работы с файлами:  shutil.copy(), shutil.copytree() и т.д


print(os.getcwd())  #  this directory
print(os.listdir(r"c:\adb"))    #  list of files
print(os.path.exists("2.2_1.py"))   #       is file in dir

print(os.path.abspath("2.2_1.py"))  # absolute path
os.chdir(r"E:\PythonProjects\venv\01_Stepik")
print(os.getcwd())


for current_dir, dirs, files in os.walk("."):
    print(current_dir, dirs,files)
    print()