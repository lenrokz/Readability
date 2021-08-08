import cs50
text = cs50.get_string("Text: ")


numbers = sum(c.isdigit() for c in text)
letters = sum(c.isalpha() for c in text)
words  = (sum(c.isspace() for c in text)) + 1
i = 0
sentences = 0
for i in range(len(text)):
    if (text[i] == '?' or text[i] == '!' or text[i] == '.'):
                sentences += 1
# source:
# https://stackoverflow.com/questions/24878174/how-to-count-digits-letters-spaces-for-a-string-in-python

L = (letters / words) * 100
S = (sentences / words) * 100
grade = round(0.0588 * L - 0.296 * S - 15.8)

if grade < 1:
    print("Before Grade 1")
elif grade >= 16:
    print("Grade 16+")
else:
    print(f"Grade {grade}")