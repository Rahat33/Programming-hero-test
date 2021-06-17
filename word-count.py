word = input("write something about your profile : ")
count = 0

for char in word:
    if char == ' ':
        count += count
count += count

print(count)