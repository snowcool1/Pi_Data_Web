#%%html
#<span style="color:red; font-family:Helvetica Neue, Helvetica, Arial, sans-serif; font-size:2em;">An Exception was encountered at 'In [6]'.</span>
#- Delete file image .BMP
#1. Login PC
#2. Auto search folder name with format: Month-Year
#3. Function: delete extention.BMP.
""" 
import os
import sys
import getpass
import shutil, os
import datetime
"""



#f = open("Test_Call_A_File.ipynb", "r")
#print(f.read())
##Doan note:  os.remove("D:/16_128_02_ProCamData/2019-12/2.CSV")
##Doan note: print("File Removed")
#todo list looop



import os
import sys
import getpass
import shutil, os
import datetime
dt = datetime.datetime.today()
folder_day=str(f"{dt:%d}")
folder_month=str(f"{dt:%m}")
folder_year=str(dt.year)
format_folder=str(folder_year+'-'+folder_month)
print(format_folder)

### ---------------  login to computer--------------- 



"""
for m in listmachine:
    print(f"todo  with {m}")
    
mylist ={
    "TRI05465":"",
    "TRI0xxx5"
}
"""

mylist=["TRI05465", "TRI04782"]
def grant_access(mylist):
    for i  in range(len(mylist)):
        print(mylist[i])
        try:
            command= fr'net use "\\{mylist[i]}\D$" Prod1234 /user:dl\production'
#             command= fr'net use "\\{mylist[i]}\D$" 6Turtl3$ /user:{mylist[i]}\Administrator'
            print(command)
            #!{command}
        except:
            command= fr'net use "\\{mylist[i]}\D$" stark300 /user:dl\fixture'
#             print(command)
            #!{command}
        else:
             command= fr'net use "\\{mylist[i]}\D$" 6Turtl3$ /user:{mylist[i]}\Administrator'
 #            print(command)
             #!{command}
  #          pass

grant_access(mylist)



#### function detete folder:


def delete_extension_func():
    dir_name1 = f"//TRI04782/d$/16_128_02_ProCamData/Reports/" + format_folder
    dir_name2 = f"//TRI05465/D$/18-001373_Datalogic_Smart/Reports/{format_folder}"
#     print(dir_name1)
#     print(dir_name2)

    dir_list =[dir_name1, dir_name2]
    
    
    for dirItem in dir_list:
#         print(dirItem)
        test = os.listdir(dirItem)
        for item in test:
            if item.endswith(".BMP"):
                
                os.remove(os.path.join(dirItem,item))
       
'''
# grant_access(mylist)
# delete_extension_func()
import os
import sys
import getpass
import shutil, os
import datetime
#import os.path

'''    


dt = datetime.datetime.today()
folder_day=str(f"{dt:%d}")
folder_month=str(f"{dt:%m}")
folder_year=str(dt.year)
format_folder=str(folder_year+'-'+folder_month)
# print(dt)

def create_log():

# Link test local mycomputer:
#     PATH= f"d:/02.Python/01.Datalogic/01.Delete_Image_Log/log_delete_extension_function.txt"
    PATH_log1 = f"//TRI04782/d$/16_128_02_ProCamData/Reports/"
    PATH_log2 = f"//TRI05465/D$/18-001373_Datalogic_Smart/Reports/"
    filename="log_delete_extension_function.txt"
    PATH_list =[PATH_log1, PATH_log2]
    for dirpath in PATH_list:
        dirpath=dirpath+"/"+ filename                   
    
        if os.path.isfile(dirpath) and os.access(dirpath, os.R_OK):
        #     print ("File exists and is readable")
            log_delete_date = open(dirpath, "a", encoding='utf-8')
            log_delete_date.write("Last deleting is: " f"{dt} \n")
            log_delete_date.close()
        else:
        #     print ("Either the file is missing or not readable")
            log_delete_date = open(dirpath, "x")
            log_delete_date = open("log_delete_extension_function.txt", "a", encoding='utf-8')
            log_delete_date.write("Last deleting is: " f"{dt} \n")
            log_delete_date.close()
    print("done")
# create_log()      


grant_access(mylist)
create_log()
delete_extension_func()

