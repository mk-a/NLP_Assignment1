#!/home/adrien/anaconda3/bin/python
import sys
import nltk
import signal

signal.signal(signal.SIGPIPE, signal.SIG_DFL)
for line in sys.stdin:
	sys.stdout.write(line.lower())
