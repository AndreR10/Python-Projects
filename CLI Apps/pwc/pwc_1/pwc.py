#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import subprocess
from multiprocessing import Process, Array, Value
from subprocess import Popen


n_processes = 0
start = 0
arg_use = ""
option = ""

list_files = [] # Array that will store the files do use
position = Value("i", 0) # variable value that is going to be the position of file in list_files
result = Value("i", 0) # variable value that is going to have result from every process


def run_task(arg):
	"""
    Executes the comand wc on a given file.

    Requires:
    - Requires a arg.
    Ensures:
    - a str with the result of the comand execution
    - a str with the process PID.
    """
	while position.value < len(list_files):
		use_file = list_files[position.value]
		position.value += 1
	
		p = Popen(["wc", arg, use_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
		output, errors = p.communicate()
		val = int(output.split(" ")[0])
		result.value += val
		print("Chlid Process has finished, PID = " + str(os.getpid()) + " with the result = " + str(output))
		
############################### ARG VERIFICATION ################################

if "-p" in sys.argv:
	n_processes = sys.argv[sys.argv.index("-p") + 1]
	if not n_processes.isdigit():
		raise("Number of processes must be an integer")
	else:
		n_processes = int(n_processes)
	
	start = sys.argv.index("-p") + 2

else:
	n_processes = 1
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


############################### PROCESS CREATION ################################

if n_processes > 1:
	if n_processes > len(list_files):
		process_list = []
	# Create processes within range of num of files, and start each process with 		target function run_task
		for i in range(len(list_files)):
			p = Process(target = run_task, args = (arg_use,))
			p.start()
			process_list.append(p)

		for process in process_list:		
			process.join()

	elif n_processes == len(list_files):
		process_list = []
		# Create processes within range of n_processes, and start each process with 		target function run_task
		for i in range(n_processes):
			p = Process(target = run_task, args = (arg_use,))
			p.start()
			process_list.append(p)
	

		for process in process_list:		
			process.join()
	
	else: 
		process_list = []
		# Create processes within range of n_processes, and start each process with 		target function run_task
		for i in range(n_processes):
			p = Process(target = run_task, args = (arg_use,))
			p.start()
			process_list.append(p)
			
		
		for process in process_list:		
			process.join()
		
else:
	# Will run if no num process to create were given
	for i in list_files:
		p = Popen(["wc", arg_use, i], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
		output, errors = p.communicate()
		val = int(output.split(" ")[0])
		result.value += val
	
	
print("Father Process, PID = " + str(os.getpid()) + " total = " + str(result.value))


