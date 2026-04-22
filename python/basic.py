#Problem 1: Add list Number
'''number = [3, 4, 5, 6, 7, 8, 9]
total = 0 
for i in number:
    
    total = total+i
print(total)
'''
#...........................................

#Problem 2 :- Sirf odd number ka Total nikalo

'''num = [3, 4, 5, 6, 7, 8, 9]
total = 0
for i in num:
    if i %2 == 1:
        total = i+total
print(total)
'''

#............................................

#Problem 3 :- print karo jo 5 letter se bada ho

'''fruit = ["apple", "banana", "fig", "Anannass"]
for i in fruit:
    if len(i)>5:
        print(i)
'''
'''kisi bhi character ka lsit ke andar ka lenth count karne ke liye
    use: len(andar list ka nam)'''

#Problem 4 :- sabse lamba word print karo
'''animal = ["cat", "elephant", "dog", "butterfly", "ant"]
sabse_lamba = ""
for i in animal:
    
    if len(i)>len(sabse_lamba):
        sabse_lamba = i
print(sabse_lamba)'''

#.................................................

#Problem 5:- Even numbers print karo, aur unko total bhi batao
''' = [10, 25, 3, 47, 8, 52, 19, 33]
total = 0
for i in num:
    if i%2 == 0:
        print(i)
        total = i+total
print(total)
'''

#.................................................

# Problem 6:- find repeated words

'''eat= ["mango", "apple", "banana", "mango", "kiwi", "apple", "mango"]
count = {}
for i in repeat:
    if i in count:
        count[i] = count[i] + 1
    else:
        count[i] = 1
print(count)
'''

#..................................................

# Combination problems from 1 to 6
'''
students = [                                     
    {"name": "Ali", "marks":85},
    {"name": "Sara", "marks": 42},
    {"name": "Raj", "marks": 91},
    {"name": "Priya", "marks":8},
    {"name": "Kaif", "marks": 76},
]
total = 0
for i in students:
    print(i["marks"])
    total =i["marks"] + total
print(total)

for i in students:
    if i["marks"]>50:
        print(i["name"], i["marks"])

best_marks = 0
best_name =""
for i in students:
    if i["marks"]>best_marks:
        best_marks = i["marks"]
        best_name = i["name"]
print(best_marks)
print(best_name)'''

#.................................................

#Combination problems:
#practise 1:-
'''
words = ["hi", "hello", "hey", "namaste", "bye", "welcome"]
count = 0
for i in words:
    if len(i)>4:
        count = count+1
        print(i)
print(count)
'''
# Practise 2:-

numbers = [12, 7, 3, 18, 5, 22, 9, 14]
print("This is even no.")
total = 0
for i in numbers:
    if i % 2 ==0:
        if i > total:
            total = i
        print(i)
print("This is big even no.")
print(total)
    