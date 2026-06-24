import sys

#1. reading arguments from command line
script=sys.argv[0] # script name
name=sys.argv[1] # first argument passed

print(f"Hello, {name}!")
print(f"Script name: {script}")