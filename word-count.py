word = input("write something about your profile : ")
count = 0

for char in word:
    if char == ' ':
        count = count + 1
count = count + 1

print(count)