"""
Written by: Jinesh Parakh

This is a checker script which compiles and runs the C++ code that you have written and checks it's accuracy with all the sample inputs and outputs scrapped using the main.py script
"""
#import necessary ibraries or modules
import os
import filecmp
import sys
from termcolor import colored, cprint
from colorama import Fore, Back, Style
import shutil
# The next two functions are used to format text for increasing the user experience
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def returnNumberofFiles(): #function to return number of files in that folder
    path = os.getcwd()
    numFiles = (
        len(
            [
                f
                for f in os.listdir(path)
                if os.path.isfile(os.path.join(path, f))
            ]
        )
        - 2
    )

    numFiles //= 2
    return numFiles
    

numFiles=returnNumberofFiles()
print("Compiling Code........")
if os.system("g++ soln.cpp")!=0:    #Compiling the C++ code (soln.cpp)
    cprint('Compilation Error', 'red',attrs=['bold'])
    sys.exit()
cprint('Code successfully Compiled!!!!', 'green',attrs=['bold'])
flag=0
for i in range(numFiles):
    os.system(f"./a.out<input{str(i)}.txt>myoutput{str(i)}.txt")
    file1 = f"output{str(i)}.txt"
    file2 = f"myoutput{str(i)}.txt"
    file3 = f"myoutputt{str(i)}.txt"
    shutil.copy(file2,file3)
    with open(file3,"a+") as f:
        f.write("\n")
    Style.RESET_ALL
    if filecmp.cmp(file1,file2) or filecmp.cmp(file1,file3):  #Checking if the expected output matches with your output
        print(f'{Fore.GREEN}✔', end=' ')
        prGreen(f"Sample Test Case {str(i)} PASS")
    else: #if the expected output does not match
        flag=1
        print(f'{Fore.RED}✘', end=' ')
        prRed(f"Sample Test Case {str(i)}  FAIL")
        print("Expected Output: ")
        x=open(file1,"r+")
        print(x.read())
        print("Your Output: ")
        y=open(file2,"r+")
        print(y.read())
    print()
    os.remove(file2)
    os.remove(file3)


os.remove("a.out")


if flag==0: #if all test cases pass, give OK VERDICT
    cprint('All sample inputs passed!! VERDICT OK', 'green',attrs=['bold'])
else: #if some test cases do not pass, give NOT OK VERICT
    cprint('Some or all sample inputs failed!! VERDICT NOT OK', 'red',attrs=['bold'])

            
