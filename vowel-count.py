text = input("Enter Your Text : ")
count = 0
vowel = ['a', 'e', 'i', 'o', 'u']

for char in text:
    if char == vowel:
        count = count + 1
    
print(count)