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
list_args = []


list_files = [] 	# Array that will store the files do use
position = 0  		# variable value that is going to be the position of file in list_files  			# variable value that is going to have returning value
result = []

files_details = {}
total = []


def run_task(arg):
    """
    Executes the comand wc on a given file.

    Requires:
    - Requires a arg that will be wc arg.
    Ensures:
    - a str reporting the status and result of the string.
    """

    global position
    global total

    while position < len(list_files):
        mutex.acquire()

        use_file = list_files[position]
        position += 1
        mutex.release()
        p = Popen(["wc", arg, use_file], stdout=subprocess.PIPE,
                  stderr=subprocess.PIPE, universal_newlines=True)
        output, errors = p.communicate()
        mutex.acquire()

        stripped_output = [s for s in output.split(" ") if s]

        file_counts = stripped_output[:-1]

        files_details[use_file] = file_counts

        if len(total) != 0:
            total = [str(int(a) + int(b)) for a, b in zip(total, file_counts)]
        else:
            total = file_counts

        mutex.release()
        result_string = 'Chlid thread has finished, with the result for ' + use_file
        for value in file_counts:
            result_string += ' ' + value

        print(result_string)

############################### ARG VERIFICATION ################################


if "-p" in sys.argv:
    p_index = sys.argv.index("-p")
    n_threads = sys.argv[p_index + 1]

    if not n_threads.isdigit():
        raise ValueError("Number of processes must be an integer")

    n_threads = int(n_threads)
    start = p_index + 2
else:
    n_threads = 1
    start = 2


files_args = sys.argv[start:len(sys.argv)]


for i in files_args:
    list_files.append(i)  # Append files to use to the list
if len(files_args) == 0:
    valid = False
    while not valid:
        # Stdin files and splits each file between spaces
        files = input("Insert the file(s): ").split(" ")
        valid = True
        for file in files:
            try:
                with open(file, 'r', encoding='utf-8') as test_file:
                    pass
            except FileNotFoundError:
                print("File " + str(file) + " is not valid. Please try again")
                valid = False

    list_files.extend(files)

if "-c" in sys.argv:
    list_args.append("-c")

if "-w" in sys.argv:
    list_args.append("-w")

if "-l" in sys.argv:
    list_args.append("-l")

if "-L" in sys.argv:
    list_args.append("-L")

# Turns the list_args into a string where only the first element of the list keeps the dash
args = list_args[0] + "".join(element[1:] for element in list_args[1:])


############################### PROCESS CREATION #################################

if n_threads > 1:
    if n_threads > len(list_files):
        threads_list = []
        # Create threads within range of num of files, and start each thread with 		target function run_task
        for i in range(len(list_files)):
            t = Thread(target=run_task, args=(args,))
            t.start()
            threads_list.append(t)

        for thread in threads_list:
            thread.join()

    elif n_threads == len(list_files):
        thread_list = []
        # Create threads within range of num of threads, and start each thread with 		target function run_task
        for i in range(n_threads):
            t = Thread(target=run_task, args=(args,))
            t.start()
            thread_list.append(t)

        for thread in thread_list:
            thread.join()

    else:
        thread_list = []
        for i in range(n_threads):
            t = Thread(target=run_task, args=(args,))
            t.start()
            thread_list.append(t)

        for thread in thread_list:
            thread.join()

else:
    for i in list_files:
        p = Popen(["wc", args, i], stdout=subprocess.PIPE,
                  stderr=subprocess.PIPE, universal_newlines=True)
        output, errors = p.communicate()

        stripped_output = [s for s in output.split(" ") if s]

        file_counts = stripped_output[:-1]

        files_details[i] = file_counts

        if len(total) != 0:
            total = [str(int(a) + int(b)) for a, b in zip(total, file_counts)]
        else:
            total = file_counts

        result_string = "File " + i + " totals ="
        for value in file_counts:
            result_string += " " + value
        print(result_string)

    process_result_string = "Process, PID = " + str(os.getpid()) + " totals ="
    for value in total:
        process_result_string += " " + value

    print(process_result_string)
