text = input("Enter Your Text : ")
count = 0
vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

for char in text:
    for n in vowel:
        if n == char:
            count = count + 1
    
print(count)