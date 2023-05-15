#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import subprocess
from multiprocessing import Process, Array, Value
from subprocess import Popen


def run_task(args, position, result, list_files):
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

        p = Popen(["wc", args, use_file], stdout=subprocess.PIPE,
                  stderr=subprocess.PIPE, universal_newlines=True)
        output, errors = p.communicate()

        val = int(output.split(" ", maxsplit=2)[1])

        result.value += val
        print("Child Process has finished, PID = " +
              str(os.getpid()) + " with the result = " + str(output))


if __name__ == '__main__':
    n_processes = 0
    start = 0
    list_args = []
    option = ""
    files_details = {}

    list_files = []  # Array that will store the files do use
    # variable value that is going to be the position of file in list_files
    position = Value("i", 0)
    # variable value that is going to have result from every process
    result = Value("i", 0)

    ############################### ARG VERIFICATION ################################

    if "-p" in sys.argv:
        p_index = sys.argv.index("-p")
        n_processes = sys.argv[p_index + 1]

        if not n_processes.isdigit():
            raise ValueError("Number of processes must be an integer")

        n_processes = int(n_processes)
        start = p_index + 2
    else:
        n_processes = 1
        start = 2

    files_args = sys.argv[start:len(sys.argv)]

    list_files.extend(files_args)  # Append files to use to the list

    if len(files_args) == 0:
        valid = False
        while not valid:
            # Stdin files and split each file between spaces
            files = input("Insert the file(s): ").split(" ")
            valid = True
            for file in files:
                try:
                    with open(file, 'r', encoding='utf-8') as test_file:
                        pass
                except FileNotFoundError:
                    print("File " + str(file) +
                          " is not valid. Please try again")
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

    ############################### PROCESS CREATION ################################

    if n_processes > 1:
        if n_processes > len(list_files):
            process_list = []
        # Create processes within range of num of files, and start each process with target function run_task
            for i in range(len(list_files)):
                p = Process(target=run_task, args=(
                    args, position, result, list_files))
                p.start()
                process_list.append(p)

            for process in process_list:
                process.join()

        elif n_processes == len(list_files):
            process_list = []
            # Create processes within range of list_files, and start each process with target function run_task
            for i in range(n_processes):

                p = Process(target=run_task, args=(
                    args, position, result, list_files))
                p.start()
                process_list.append(p)

            for process in process_list:
                process.join()

        else:
            process_list = []
            # Create processes within range of n_processes, and start each process with target function run_task
            for i in range(n_processes):
                p = Process(target=run_task, args=(
                    args, position, result, list_files))
                p.start()
                process_list.append(p)

            for process in process_list:
                process.join()

    else:
        # Will run if no num process to create were given
        for i in list_files:

            p = Popen(["wc", args, i], stdout=subprocess.PIPE,
                      stderr=subprocess.PIPE, universal_newlines=True)

            output, errors = p.communicate()

            files_details[i] = output.split(
                " ", maxsplit=len(list_args)+1)[1:-1]

            val = int(output.split(" ", maxsplit=2)[1])
            result.value += val

    print("Father Process, PID = " + str(os.getpid()) +
          " with the result = " + str(files_details))
