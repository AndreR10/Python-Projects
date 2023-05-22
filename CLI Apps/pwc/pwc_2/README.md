## Objective

This version of `pwc` uses process synchronization, file manipulation, and signal handling, timing, and alarms.

## Description

On file pwc.py, the program is executed with processes.

### NAME

`pwc` - print lines in given files matching the indicated text
`hpwc` - read history of pgrep program execution

### DESCRIPTION

`pwc` counts caracters | words | lines of the given files.
`hpwc` reads record of input files and presents information for a stdout.

### SYNOPSIS

```bash
    pwc [-c|-w|-l [-L]] [-p n] [-a s] [-f file] {files}
```

### OPTIONS

- `-p n` -`-p n`, is optional. -`n` = number.
  - Defines the number of parallel threads/processes that are used for searching.
  - If this command is not given, only one thread/process will be used.
- `a s`
  - `a s`, is optional.
  - `s` is microseconds.
  - Defines the time interval(micro-seconds) in which the parent process writes for stdout the state of research.
  - If this command is not given, the program will run normally with out time interval.
- `f file`
  - `f file`, is optinal.
  - `file` = file of output
  - Defines the file use to save the history of program implementation.
  - If this command is not given, the history will not be saved.

### NAME

`hpwc` - read history of pgrep program execution

### DESCRIPTION

`hpwc` reads record of input files and presents information for a stdout.

### SYNOPSIS

```bash
    hpwc file
```

### LIMITATIONS:

Option -l -L doens´t work properly, and the Record.bin doens´t get the process information.

## Dependencies

- Python 3.6
