#!/usr/bin/env python
# -*- coding: utf-8 -*-

#imports
import sys, os, pickle
import os.path


if os.path.exists(sys.argv[1]):
	with open(sys.argv[1], "rb") as export:
			report = pickle.load(export)

	print(report)
else:
	print("File not find")

	
