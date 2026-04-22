students = [                                     
    {"name": "Ali", "marks":85},
    {"name": "Sara", "marks": 42},
    {"name": "Raj", "marks": 91},
    {"name": "Priya", "marks":8},
    {"name": "Kaif", "marks": 76},
]

total = 0
for i in students:
    total = i["marks"]+ total
print(total)

for i in students:
    if i["marks"]>50:
        print(i["marks"], i["name"])

best_m = 0
best_n = ""
for i in students:
    if i["marks"] >best_m:
        best_m= i["marks"]
        best_n = i["name"]
print(best_m)
print(best_n)
        
