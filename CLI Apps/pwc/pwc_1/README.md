
## Objective

This version of `pwc` and `pwc_threads` uses processes/threads and communication between processes/threads.

## Introduction

`pwc` `pwc_threads` counts, in parallel, the number of characters, words, and lines in multiple files, and indicates for each file the size of its longest line.

## Description
### Synopsis
```bash
  pwc [-c|-w|-l [-L]] [-p n] {files}
  pwc_threads [-c|-w|-l [-L]] [-p n] {files}
```

### Opcions 

- `-c`: Option that allows obtaining the number of characters in a file.
- `-w`: Option that allows obtaining the number of words in a file.
- `-l`: Option that allows obtaining the number of lines in a file.
- `-L`: Optional option that calculates the size of the longest line in the file. This option can only be combined with the -l option.
- `-p n`: Optional option that sets the level of parallelization of the command by n (i.e., the number of processes/threads used for counting). By default, only one process should be used for counting.

Zero or more files can be given, on which the counting is performed. If no files are provided in the command line, they should be read from stdin.

Initially, the parent process should create the processes/threads defined by the parallelization level of the command (value n). These processes/threads count the characters, words, or lines of a file and write the results to stdout. They continue counting until it has been performed on all files. The counting results are written to stdout in a non-interleaved manner.

Finally, the parent process should write to stdout the total number of characters, words, or lines, according to the specified counting option.

## Dependencies

- Python 3.XX
## Run Locally

#### Clone the project

```bash
  git clone https://github.com/AndreR10/Python-Projects.git
```

#### Go to the project directory

```bash
  cd Python-Projects/CLI\Apps/pwc/pwc_1
```

#### Sofware execution

```bash
  python pwc.py -c -w -p 2 file2.txt file3.txt
  python pwc_threads.py -c -w -p 2 file2.txt file3.txt
```


