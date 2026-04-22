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

repeat = ["mango", "apple", "banana", "mango", "kiwi", "apple", "mango"]
for i in repeat:
    count = { "mango", "apple", "banana", "kiwi" }
    print(count)
