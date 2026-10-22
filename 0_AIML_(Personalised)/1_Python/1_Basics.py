# variables , Input and Output
print("===variables , Input and Output===")
count = 10
price = 99.5
language = "Python"
is_ready = True
result = None

print(type(count))      # <class 'int'>
print(type(price))      # <class 'float'>
print(type(language))   # <class 'str'>
print(type(is_ready))   # <class 'bool'>



#Operators
print("===Operators===")
print(7 / 2)    # 3.5
print(7 // 2)   # 3
print(7 % 2)    # 1
print(2 ** 4)   # 16
print(-7 // 2)  # -4


#Comparision operators
marks = 82
print(marks >= 40)  # True
print(marks == 100) # False
print(marks != 0)   # True


#Logical operators
age = 20
has_id = True

print(age >= 18 and has_id)  # True
print(age < 18 or has_id)    # True
print(not has_id)            # False


#Assignment operators
count = 10
count += 2   # same effect as count = count + 2
count -= 1
count *= 3
count /= 2


# ====== CONDITONAL STATEMENTS ========
print("=== CONDITONAL STATEMENTS ===")
marks = 76

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 40:
    grade = "D"
else:
    grade = "F"

print(grade)

# nested if else
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("Too young")


# Truthy and falsy values
name = ""

if name:
    print("Name supplied")
else:
    print("Name is empty")
    
    
    
# ===== LOOPS ====
print("=== LOOPS (while,for) ===")

#for loop
for name in ["Aman", "Riya", "Sam"]:
    print(name)

for i in range(0,20,2):
    print(i,end=" ")
    
print("---")
#while loop
count = 1
while(count < 5):
    print(count)
    count += 1
print(count)

print("---")
# break and continue 
for number in range(1, 8):
    if number == 5:
        break
    print(number)  # 1, 2, 3, 4

print("---")
for number in range(1, 6):
    if number == 3:
        continue
    print(number)  # 1, 2, 4, 5
    
    
    
    
# ====== STRINGS ======
print("=== STRINGS ===")

language = "Python"
message = 'Hello world'
description = """Python is widely used
for data analysis and machine learning."""

# indexing and slicing
word = "python"
print(word[0])   # P
print(word[2])   # t
print(word[-1])  # n

print(word[0:2])   # Py
print(word[2:])    # thon
print(word[:4])    # Pyth
print(word[::2])   # Pto
print(word[::-1])  # nohtyP

#String Methods
    #.join() , .split() , .lower() , .upper() , etc...
sentence = "  Learn Python for AI  "
cleaned = sentence.strip().lower()
words = cleaned.split()
joined = "_".join(words)

print(cleaned)  # learn python for ai
print(words)    # ['learn', 'python', 'for', 'ai']
print(joined)   # learn_python_for_ai

#String formatting
name = "Rahul"
score = 87
print(f"{name} scored {score} marks.")
print(f"Next score target: {score + 5}")










