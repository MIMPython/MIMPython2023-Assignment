import argparse
parser = argparse.ArgumentParser(
    description = "Assignment namer."
)

parser.add_argument("name", type = str, help = "Student's name")
parser.add_argument("indices", type = int, nargs = 3, 
                    help = "Indices for Week, Assignment, Student ID")

results = parser.parse_args()
message = (f"week{results.indices[0]:02d}_"
           f"assignment{results.indices[1]:02d}_"
           f"student{results.indices[2]:02d}_"
           f"{results.name}.py")
print(message)