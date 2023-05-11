#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
from threading import Thread, Lock
import subprocess
from subprocess import Popen

mutex = Lock()
n_threads = 0
start = 0
arg_use = ""


list_files = [] 	# Array that will store the files do use
position = 0  		# variable value that is going to be the position of file in list_files  			# variable value that is going to have returning value
result = 0

def run_task(arg):
	"""
    Executes the comand wc on a given file.

    Requires:
    - Requires a arg that will be wc arg.
    Ensures:
    - a str reporting the status and result of the string.
    """
	
	global position
	global result
	
	
	while position < len(list_files):
		mutex.acquire()
		use_file = list_files[position]
		position += 1
		mutex.release()
		p = Popen(["wc", arg, use_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
		output, errors = p.communicate()
		mutex.acquire()
		val = int(output.split(" ")[0])
		result += val
		mutex.release()
		print("Chlid thread has finished, with the result = " + str(output))
		
		
############################### ARG VERIFICATION ################################
if "-p" in sys.argv:
	n_threads = sys.argv[sys.argv.index("-p") + 1]
	if not n_threads.isdigit():
		raise("Number of processes must be an integer")
	else:
		n_threads = int(n_threads)
	start = sys.argv.index("-p") + 2
else:
	n_threads = 1
	start = 2


files_args = sys.argv[start:len(sys.argv)]


for i in files_args:
	list_files.append(i) #Append files to use to the list
if len(files_args) == 0:
        valid = False
        while not valid:
            files = input("Insert the file(s): ").split(" ")   # Stdin files and splits each file between spaces
            valid = True
            for file in files_args:
                try:
                    test_file = open(file)
                    test_file.close()
                except:
                    print("File " + str(file) +" is not valid. Please try again")
                    valid = False
             
        for file in files_args:
            list_files.append(file)

if "-c" in sys.argv:
	arg_use = "-c"

elif "-w" in sys.argv:
	arg_use = "-w"

elif "-l" in sys.argv:
	arg_use = "-l"

elif "-L" in sys.argv:
	arg_use = "-L"
	

############################### PROCESS CREATION #################################

if n_threads > 1:
	if n_threads > len(list_files):
		threads_list = []
		# Create threads within range of num of files, and start each thread with 		target function run_task
		for i in range(len(list_files)):
			t = Thread(target = run_task, args = (arg_use,))
			t.start()
			threas_list.append(t)

		for thread in thread_list:		
			thread.join()

	elif n_threads == len(list_files):
		thread_list = []
		# Create threads within range of num of threads, and start each thread with 		target function run_task
		for i in range(n_threads):
			t = Thread(target = run_task, args = (arg_use,))
			t.start()
			thread_list.append(t)
	

		for thread in thread_list:		
			thread.join()
	
	else:
		thread_list = []
		for i in range(n_threads):
			t = Thread(target = run_task, args = (arg_use,))
			t.start()
			thread_list.append(t)
			
		
		for thread in thread_list:		
			thread.join()
		
else:
	for i in list_files:
		p = Popen(["wc", arg_use, i], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
		output, errors = p.communicate()
		val = int(output.split(" "))
		result += val
	
	
print("Process, PID = " + str(os.getpid()) + " total = " + str(result))


