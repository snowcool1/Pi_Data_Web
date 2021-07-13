{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "hide_input": true,
    "inputHidden": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<span style=\"color:red; font-family:Helvetica Neue, Helvetica, Arial, sans-serif; font-size:2em;\">An Exception was encountered at 'In [6]'.</span>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "%%html\n",
    "<span style=\"color:red; font-family:Helvetica Neue, Helvetica, Arial, sans-serif; font-size:2em;\">An Exception was encountered at 'In [6]'.</span>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "papermill": {
     "duration": 0.025747,
     "end_time": "2020-09-08T10:07:05.698348",
     "exception": false,
     "start_time": "2020-09-08T10:07:05.672601",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "- Delete file image .BMP\n",
    "1. Login PC\n",
    "2. Auto search folder name with format: Month-Year\n",
    "3. Function: delete extention.BMP."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "papermill": {
     "duration": 0.05385,
     "end_time": "2020-09-08T10:07:05.800126",
     "exception": false,
     "start_time": "2020-09-08T10:07:05.746276",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "import os\n",
    "import sys\n",
    "import getpass\n",
    "import shutil, os\n",
    "import datetime\n",
    "\n",
    "\n",
    "#f = open(\"Test_Call_A_File.ipynb\", \"r\")\n",
    "#print(f.read())\n",
    "##Doan note:  os.remove(\"D:/16_128_02_ProCamData/2019-12/2.CSV\")\n",
    "##Doan note: print(\"File Removed\")\n",
    "#todo list looop\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "papermill": {
     "duration": 14.856732,
     "end_time": "2020-09-08T10:07:20.680748",
     "exception": false,
     "start_time": "2020-09-08T10:07:05.824016",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2020-09\n",
      "TRI05465\n",
      "net use \"\\\\TRI05465\\D$\" Prod1234 /user:dl\\production\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "System error 5 has occurred.\n",
      "\n",
      "Access is denied.\n",
      "\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "TRI04782\n",
      "net use \"\\\\TRI04782\\D$\" Prod1234 /user:dl\\production\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "System error 86 has occurred.\n",
      "\n",
      "The specified network password is not correct.\n",
      "\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "System error 5 has occurred.\n",
      "\n",
      "Access is denied.\n",
      "\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "System error 86 has occurred.\n",
      "\n",
      "The specified network password is not correct.\n",
      "\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "import sys\n",
    "import getpass\n",
    "import shutil, os\n",
    "import datetime\n",
    "dt = datetime.datetime.today()\n",
    "folder_day=str(f\"{dt:%d}\")\n",
    "folder_month=str(f\"{dt:%m}\")\n",
    "folder_year=str(dt.year)\n",
    "format_folder=str(folder_year+'-'+folder_month)\n",
    "print(format_folder)\n",
    "\n",
    "### ---------------  login to computer--------------- \n",
    "\n",
    "\n",
    "\n",
    "\"\"\"\n",
    "for m in listmachine:\n",
    "    print(f\"todo  with {m}\")\n",
    "    \n",
    "mylist ={\n",
    "    \"TRI05465\":\"\",\n",
    "    \"TRI0xxx5\"\n",
    "}\n",
    "\"\"\"\n",
    "\n",
    "mylist=[\"TRI05465\", \"TRI04782\"]\n",
    "def grant_access(mylist):\n",
    "    for i  in range(len(mylist)):\n",
    "        print(mylist[i])\n",
    "        try:\n",
    "            command= fr'net use \"\\\\{mylist[i]}\\D$\" Prod1234 /user:dl\\production'\n",
    "#             command= fr'net use \"\\\\{mylist[i]}\\D$\" 6Turtl3$ /user:{mylist[i]}\\Administrator'\n",
    "            print(command)\n",
    "            !{command}\n",
    "        except:\n",
    "            command= fr'net use \"\\\\{mylist[i]}\\D$\" stark300 /user:dl\\fixture'\n",
    "#             print(command)\n",
    "            !{command}\n",
    "        else:\n",
    "             command= fr'net use \"\\\\{mylist[i]}\\D$\" 6Turtl3$ /user:{mylist[i]}\\Administrator'\n",
    " #            print(command)\n",
    "             !{command}\n",
    "  #          pass\n",
    "\n",
    "grant_access(mylist)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "papermill": {
     "duration": 0.011968,
     "end_time": "2020-09-08T10:07:20.717600",
     "exception": false,
     "start_time": "2020-09-08T10:07:20.705632",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "papermill": {
     "duration": 0.031922,
     "end_time": "2020-09-08T10:07:20.762518",
     "exception": false,
     "start_time": "2020-09-08T10:07:20.730596",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'\\ndef delete_extension_func():\\n    dir_name1 = f\"//TRI04782/d$/16_128_02_ProCamData/Reports/{format_folder}\"\\n    dir_name2 = f\"//TRI05465/D$/18-001373_Datalogic_Smart/Reports/{format_folder}\"\\n#     print(dir_name1)\\n#     print(dir_name2)\\n\\n    test = os.listdir(dir_name1)    \\n    for item in test:\\n        if item.endswith(\".BMP\"):\\n            os.remove(os.path.join(dir_name1, item))\\n    \\n    test1 = os.listdir(dir_name2)     \\n    for item in test1:\\n        if item.endswith(\".BMP\"):\\n            \\n            os.remove(os.path.join(dir_name2, item))\\ngrant_access(mylist)\\ndelete_extension_func()\\n\\n'"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#### function detete folder:\n",
    "\"\"\"\n",
    "def delete_extension_func():\n",
    "    dir_name1 = f\"//TRI04782/d$/16_128_02_ProCamData/Reports/{format_folder}\"\n",
    "    dir_name2 = f\"//TRI05465/D$/18-001373_Datalogic_Smart/Reports/{format_folder}\"\n",
    "#     print(dir_name1)\n",
    "#     print(dir_name2)\n",
    "\n",
    "    test = os.listdir(dir_name1)    \n",
    "    for item in test:\n",
    "        if item.endswith(\".BMP\"):\n",
    "            os.remove(os.path.join(dir_name1, item))\n",
    "    \n",
    "    test1 = os.listdir(dir_name2)     \n",
    "    for item in test1:\n",
    "        if item.endswith(\".BMP\"):\n",
    "            \n",
    "            os.remove(os.path.join(dir_name2, item))\n",
    "grant_access(mylist)\n",
    "delete_extension_func()\n",
    "\n",
    "\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "papermill": {
     "duration": 0.026927,
     "end_time": "2020-09-08T10:07:20.804367",
     "exception": false,
     "start_time": "2020-09-08T10:07:20.777440",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "\n",
    "def delete_extension_func():\n",
    "    dir_name1 = f\"//TRI04782/d$/16_128_02_ProCamData/Reports/\" + format_folder\n",
    "    dir_name2 = f\"//TRI05465/D$/18-001373_Datalogic_Smart/Reports/{format_folder}\"\n",
    "#     print(dir_name1)\n",
    "#     print(dir_name2)\n",
    "\n",
    "    dir_list =[dir_name1, dir_name2]\n",
    "    \n",
    "    \n",
    "    for dirItem in dir_list:\n",
    "#         print(dirItem)\n",
    "        test = os.listdir(dirItem)\n",
    "        for item in test:\n",
    "            if item.endswith(\".BMP\"):\n",
    "                \n",
    "                os.remove(os.path.join(dirItem,item))\n",
    "       \n",
    "       \n",
    "# grant_access(mylist)\n",
    "# delete_extension_func()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "papermill": {
     "duration": 0.033877,
     "end_time": "2020-09-08T10:07:20.854234",
     "exception": false,
     "start_time": "2020-09-08T10:07:20.820357",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "import os\n",
    "import sys\n",
    "import getpass\n",
    "import shutil, os\n",
    "import datetime\n",
    "#import os.path\n",
    "\n",
    "dt = datetime.datetime.today()\n",
    "folder_day=str(f\"{dt:%d}\")\n",
    "folder_month=str(f\"{dt:%m}\")\n",
    "folder_year=str(dt.year)\n",
    "format_folder=str(folder_year+'-'+folder_month)\n",
    "# print(dt)\n",
    "\n",
    "def create_log():\n",
    "\n",
    "# Link test local mycomputer:\n",
    "#     PATH= f\"d:/02.Python/01.Datalogic/01.Delete_Image_Log/log_delete_extension_function.txt\"\n",
    "    PATH_log1 = f\"//TRI04782/d$/16_128_02_ProCamData/Reports/\"\n",
    "    PATH_log2 = f\"//TRI05465/D$/18-001373_Datalogic_Smart/Reports/\"\n",
    "    filename=\"log_delete_extension_function.txt\"\n",
    "    PATH_list =[PATH_log1, PATH_log2]\n",
    "    for dirpath in PATH_list:\n",
    "        dirpath=dirpath+\"/\"+ filename                   \n",
    "    \n",
    "        if os.path.isfile(dirpath) and os.access(dirpath, os.R_OK):\n",
    "        #     print (\"File exists and is readable\")\n",
    "            log_delete_date = open(dirpath, \"a\", encoding='utf-8')\n",
    "            log_delete_date.write(\"Last deleting is: \" f\"{dt} \\n\")\n",
    "            log_delete_date.close()\n",
    "        else:\n",
    "        #     print (\"Either the file is missing or not readable\")\n",
    "            log_delete_date = open(dirpath, \"x\")\n",
    "            log_delete_date = open(\"log_delete_extension_function.txt\", \"a\", encoding='utf-8')\n",
    "            log_delete_date.write(\"Last deleting is: \" f\"{dt} \\n\")\n",
    "            log_delete_date.close()\n",
    "    print(\"done\")\n",
    "# create_log()      \n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "papermill": {
     "duration": 6.383409,
     "end_time": "2020-09-08T10:07:27.257593",
     "exception": true,
     "start_time": "2020-09-08T10:07:20.874184",
     "status": "failed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "TRI05465\n",
      "net use \"\\\\TRI05465\\D$\" Prod1234 /user:dl\\production\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "System error 5 has occurred.\n",
      "\n",
      "Access is denied.\n",
      "\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "TRI04782\n",
      "net use \"\\\\TRI04782\\D$\" Prod1234 /user:dl\\production\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "System error 86 has occurred.\n",
      "\n",
      "The specified network password is not correct.\n",
      "\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "System error 5 has occurred.\n",
      "\n",
      "Access is denied.\n",
      "\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "System error 86 has occurred.\n",
      "\n",
      "The specified network password is not correct.\n",
      "\n"
     ]
    },
    {
     "ename": "OSError",
     "evalue": "[Errno 22] Invalid argument: '//TRI04782/d$/16_128_02_ProCamData/Reports//log_delete_extension_function.txt'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mOSError\u001b[0m                                   Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-6-08b019866378>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[0mgrant_access\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmylist\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[0mcreate_log\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      3\u001b[0m \u001b[0mdelete_extension_func\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m<ipython-input-5-a23e2a395b30>\u001b[0m in \u001b[0;36mcreate_log\u001b[1;34m()\u001b[0m\n\u001b[0;32m     31\u001b[0m         \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     32\u001b[0m         \u001b[1;31m#     print (\"Either the file is missing or not readable\")\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 33\u001b[1;33m             \u001b[0mlog_delete_date\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mopen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mdirpath\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m\"x\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     34\u001b[0m             \u001b[0mlog_delete_date\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mopen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"log_delete_extension_function.txt\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m\"a\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mencoding\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m'utf-8'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     35\u001b[0m             \u001b[0mlog_delete_date\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mwrite\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Last deleting is: \"\u001b[0m \u001b[1;34mf\"{dt} \\n\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mOSError\u001b[0m: [Errno 22] Invalid argument: '//TRI04782/d$/16_128_02_ProCamData/Reports//log_delete_extension_function.txt'"
     ]
    }
   ],
   "source": [
    "grant_access(mylist)\n",
    "create_log()\n",
    "delete_extension_func()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "papermill": {
     "duration": null,
     "end_time": null,
     "exception": null,
     "start_time": null,
     "status": "pending"
    },
    "tags": []
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "papermill": {
     "duration": null,
     "end_time": null,
     "exception": null,
     "start_time": null,
     "status": "pending"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "\n",
    "#     if os.path.isfile(PATH) and os.access(PATH, os.R_OK):\n",
    "#             #     print (\"File exists and is readable\")\n",
    "#                 log_delete_date = open(PATH, \"a\", encoding='utf-8')\n",
    "#                 log_delete_date.write(\"Last deleting is: \" f\"{dt} \\n\")\n",
    "#                 log_delete_date.close()\n",
    "#             else:\n",
    "#             #     print (\"Either the file is missing or not readable\")\n",
    "#                 log_delete_date = open(PATH, \"x\")\n",
    "#                 log_delete_date = open(\"log_delete_extension_function.txt\", \"a\", encoding='utf-8')\n",
    "#                 log_delete_date.write(\"Last deleting is: \" f\"{dt} \\n\")\n",
    "#                 log_delete_date.close()\n",
    "\n",
    "# create_log() \n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  },
  "papermill": {
   "duration": 28.742753,
   "end_time": "2020-09-08T10:07:27.682468",
   "environment_variables": {},
   "exception": true,
   "input_path": "D:\\02.Python\\01.Datalogic\\01.Delete_Image_Log\\Delete_extension_function.ipynb",
   "output_path": "D:\\02.Python\\01.Datalogic\\01.Delete_Image_Log\\Delete_extension_function_output.ipynb",
   "parameters": {},
   "start_time": "2020-09-08T10:06:58.939715",
   "version": "1.2.1"
  },
  "toc": {
   "base_numbering": 1,
   "nav_menu": {},
   "number_sections": true,
   "sideBar": true,
   "skip_h1_title": false,
   "title_cell": "Table of Contents",
   "title_sidebar": "Contents",
   "toc_cell": false,
   "toc_position": {},
   "toc_section_display": true,
   "toc_window_display": false
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}