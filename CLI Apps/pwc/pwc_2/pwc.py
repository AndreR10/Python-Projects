#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os, signal, time, struct, pickle
import subprocess
import datetime
from time import strftime 
from datetime import datetime
from multiprocessing import Process, Queue, Semaphore, Array, Value
from subprocess import Popen, PIPE

sem1 = Semaphore(1)
sem2 = Semaphore(1)



n_processes = 0
start = 0
arg_use = ""
option = ""

list_files = [] # Array that will store the files do use
process_list = [] # Array that will store the processes

files_to_divide = []
files_divided = []

position = Value("i", 0) # variable value that is going to be the position of file in list_files
result = Value("i", 0) # variable value that is going to have result from every process




global files_done 
files_done = []

global pid 
pid = []

global time_per_file 
time_per_file = []

global results
results = []




################################ USED FUNCTIONS #######################################

# Function used for signal (ctrl+c)
def control_C (sig, NULL):	
	"""
	Executes the function father_report
	Requires:
	- Requires a SIGNAL
	Ensures:
	- executes father_report and finish the program
	"""
	print("Número de " + arg_descr(arg_use) + str(result.value))
	sys.exit() 
	

def father_report(sig, NULL):	
	"""
	Runs every -a seconds
	Requires:
	- Requires a SIGNAL.
	"""
	
	print(arg_descr(arg_use) + str(result.value))
	print("\nNumber of files fineshed: " + str(len(files_done))) 
	print("Current execution time: " + str(time.time() - start_time) + " microsegundos")
	


signal.signal(signal.SIGINT, control_C)

def arg_descr(arg_use):
	"""
	Gives the description of the argument passed 
	Requires:
	- Requires a str arg
	Ensures:
	- returns the type of argument 
	"""
	type = ""
	if arg_use == "-c":
		type += "caracteres: "
	elif arg_use == "-w":
		type += "palavras: "
	elif arg_use == "-l":
		type += "linhas: "
	
	return type



def divide_file(files_to_divide):
	"""
	Splits the files in the files to divide in two  
	Requires:
	- Requires a list of the files to use
	Ensures:
	- split the file in two diferent files  
	"""
	for i in files_to_divide: # iterate throu the files in the list files_to_divide
		prefix = i.split(".txt")[0] # var with the perfix that has to be given to create files with the same name
		subprocess.Popen(['split','-n2', i, prefix]) # split command that will split the file in two pieces 
		
def add_file(l):
	"""
	Get the files from the working directory and add them to the given list with new names 
	Requires:
	- A list to where the files will be added 
	Ensures:
	- A list with new files   
	"""
	current_Directory = os.getcwd()
	files = os.listdir(current_Directory)
	remove_file(list_files, files_to_divide)
	for file in files:
		if "aa" in file or "ab" in file:
			l.append(change_file_name(str(file)))
	

def remove_file(list_files, files_to_divide):
	"""
	Checks the main list where the files will be processed to find if theres any original file that
	was divided and remove it from the main list  
	Requires:
	- Requires two lists one with the files to process and other with the files that have to be 
		removed from the first one 
	Ensures:
	- Remove the files that match  
	"""
	for i in files_to_divide:
			if i in list_files:
				list_files.remove(i)
	

def change_file_name(file_name):
	"""
	Changes the name of the given file and adds the extention .txt 
	Requires:
	- Requires a str
	Ensures:
	- A new str name  
	"""
	file_end = ".txt" 
	new_name = str(file_name[:5]) + file_end
	return new_name		
		
def run_task(arg):
	"""
    Executes the comand wc on a given file.

    Requires:
    - Requires a arg and option if given.
    Ensures:
    - a str with the result of the comand execution
    - a str with the process PID.
    """
	
	while position.value < len(list_files):
		sem1.acquire()
		use_file = list_files[position.value]
		position.value += 1
		processing_time = time.time() # initial time
		

		
		if option is not "":
			
			p = Popen(["wc", arg + " " + option, use_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
			output, errors = p.communicate()
			val = int(output.split(" ")[0])
			result.value += val
			results.append(val)
			files_done.append(use_file)
			pid.append(os.getpid())
			sem1.release()
			print("Chlid Process has finished, PID = " + str(os.getpid()) + " with the result = " + str(output))	 # total time processing the file
			
		else:
			
			p = Popen(["wc", arg_use, use_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
			output, errors = p.communicate()
			val = int(output.split(" ")[0])
			result.value += val
			results.append(val)
			files_done.append(use_file)
			pid.append(os.getpid())	
			sem1.release()
			print("Chlid Process has finished, PID = " + str(os.getpid()) + " with the result = " + str(output))
			
		
		
		sem1.acquire()
		processing_time = time.time() - processing_time
		time_per_file.append(str(processing_time)) 
		sem1.release()
		

def write_file():
	record = "Início da execução da pesquisa: " + str(current_time.strftime("%d/%m/%Y %H:%M:%S.%f"))
	record += "\nDuração da execução: " + str((datetime.now() - current_time)) + "\n"
	for i in range (0, len(pid)):
		record += "Processo: " + str(pid[i]) + "\n"
		record += "\tficheiro: " + str(files_done[i]) + "\n"
		record += "\t\ttempo de pesquisa: " + str(time_per_file[i]) + "\n" + "\t\tdimensão do ficheiro: " + str(results[i]) + "\n" + "\t\tnúmero de " + str(arg_descr(arg_use)) + str(results[i]) + "\n" 
	
	with open(record_file, "wb") as recordfile:
		pickle.dump(record,recordfile,pickle.HIGHEST_PROTOCOL)

############################### ARG VERIFICATION ################################
for i in range(1, len(sys.argv)):
	if(sys.argv[i] == "-c"):
		arg_use = "-c"
	elif(sys.argv[i] == "-w"):
		arg_use = "-w"
	elif(sys.argv[i] == "-w"):
		arg_use = "-w"
	elif(sys.argv[i] == "-l"):
		arg_use = "-l"
		if(sys.argv[sys.argv.index("-l") + 1] == "-L"):
			option = "-L"

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

if "-a" in sys.argv:
	warning_time = sys.argv[sys.argv.index("-a") + 1]
	if not warning_time.isdigit():
		raise("Time must be an number")
	else:
		warning_time = float(warning_time)
	start += 2
	
# SIGNAL that assigns warning time in which print_state function gets triggered
	signal.setitimer(signal.ITIMER_REAL, warning_time, warning_time)
# Assigns function to the alarm
	signal.signal(signal.SIGALRM, father_report)

if "-f" in sys.argv:
	record_file = sys.argv[sys.argv.index("-f") + 1]
	start += 2
else:
	record_file = "Record.bin" # record file name if user doesnt provide one


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


# SIGINT signal that triggers function ctrl 
signal.signal(signal.SIGINT, control_C)

############################### PROCESS CREATION ################################
start_time = time.time()

current_time = datetime.now()

if n_processes > 1:
	if n_processes > len(list_files):
		process_left = n_processes - len(list_files)
		# it will add files to the files_to_divide to match the number of processes 
		for i in range(process_left):
			files_to_divide.append(list_files[i])
		
		divide_file(files_to_divide)
		add_file(list_files)
	
		# Create processes within range of num of files, and start each process with 		target function run_task
		for i in range(n_processes):
			p = Process(target = run_task, args = (arg_use,))
			time.sleep(1)
			p.start()
			process_list.append(p)

		for process in process_list:		
			process.join()

	elif n_processes == len(list_files):
		# Create processes within range of n_processes, and start each process with 		target function run_task
		for i in range(n_processes):
			p = Process(target = run_task, args = (arg_use,))
			p.start()
			process_list.append(p)

		for process in process_list:		
			process.join()
	
	else: 
		# Create processes within range of n_processes, and start each process with 		target function run_task
		for i in range(n_processes):
			p = Process(target = run_task, args = (arg_use,))
			p.start()
			process_list.append(p)
			
		
		for process in process_list:		
			process.join()
		
else:
	# Will run if no num process to create were given
	
	processing_time = time.time() # initial time	
	for i in list_files:
		processing_time = time.time() # initial time
		p = Popen(["wc", arg_use, i], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
		output, errors = p.communicate()
		val = int(output.split(" ")[0])
		result.value += val
		results.append(val)
		files_done.append(i)
		pid.append(str(os.getpid()))
		processing_time = time.time() - processing_time
		time_per_file.append(processing_time)
		
		
		
	
	write_file()
	

print(files_done)


print(pid)

print(time_per_file)

print(results)

write_file()

print("Father Process, PID = " + str(os.getpid()) + " total = " + str(result.value))


