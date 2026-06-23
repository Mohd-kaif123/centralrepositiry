import argparse

parser = argparse.ArgumentParser()
parser.add_argument("name")
parser.add_argument("--age", type=int, help="Age of the user", default=0)
parser.add_argument("--salary",type=int,help="Salary of the user", default=0)
args = parser.parse_args()
print(f"Name: {args.name} ")
print(f"Age: {args.age}")
print(f"Salary: {args.salary}")