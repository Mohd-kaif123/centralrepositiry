import sys
import argparse

#1. reading arguments from command line
# name=sys.argv[1] # first argument passed
# print(f"Hello, {name}!")

#2. using argparse for advance argument parsing
parser=argparse.ArgumentParser(description="Greet the user.")
parser.add_argument("name",help="Name of the user to greet.")
parser.add_argument("--age",type=int,help="Age of the user.",default=0)
parser.add_argument("--empid",type=int,help="Employee ID of the user.",default=1)

args=parser.parse_args()
print(f"Hello, {args.name}! You are {args.age} years Old. Your employee ID is {args.empid}.")
# open wsl cli=> python3 05.cliArg.py nikunj --age 45 --empid 12345
# open cmd cli=> python 05.cliArg.py nikunj --age 45 --empid 12345