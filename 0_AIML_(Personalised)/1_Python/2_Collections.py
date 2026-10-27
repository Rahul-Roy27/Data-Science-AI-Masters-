# QUESTIONS - Beginner

# 1.
l1 = [10,20,30,40 ,50]
print(f"first = {l1[0]} , last = {l1[-1]}")

# 2.
l1.append(121)
l1.extend([1,2,3])

print(l1)

# 3
l2 = sorted(l1)
print(l2)

# 4
t1 = (10)

# 5
l2 = [1,2,2,3,3,4]
l2 = set(l2)
print(l2)

# 6
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print(s1|s2)
print(s1&s2)

# 7
student = {
    "A" : 22,
    "B" : 45,
    "C" : 56,
}

print(student.get("B"))

# 8 
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
counts = {}

for word in words:
    counts[word] = counts.get(word, 0) + 1

print(counts)

# 9 
l3 = [n for n in range(1,10)]
print(l3)

# 10
l4  = [n for n in range(1,31) if n%3==0]
print(l4)

