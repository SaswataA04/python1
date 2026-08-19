text = "Python programming"

# 1. Display the string
#print("1. String:", text)


# 2. Display Python and programming separately
print("Python")
print("programming")


if "Java" not in text:
    print("\n2. Java is not present in the string.")


if "Java" not in text.split():
    text = text.replace("Python programming", "Python Java programming")

print("\n3. After adding Java:")
print(text)


# 4. Find the length of the new string
print("\n4. Length of new string:", len(text))


# 5. number of words
words = text.split()
print("\n5. Number of words:", len(words))


# 6. Capitalize each word and find number of words
capitalized_text = text.title()

print("\n6. Capitalized string:", capitalized_text)
print("Number of words:", len(capitalized_text.split()))


# 7. Remove all spaces
no_spaces_text = text.replace(" ", "")

print("\n7. String without spaces:", no_spaces_text)


# 8. Frequency of A, P, R and M
original_text = "Python programming"

print("\n8. Frequency of A, P, R and M:")

for letter in ['A', 'P', 'R', 'M']:
    count = original_text.upper().count(letter)
    print(letter, ":", count)