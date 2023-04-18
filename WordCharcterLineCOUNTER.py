import tkinter as tk
from tkinter import filedialog
import re

root = tk.Tk()
root.withdraw()

word_count = 0
line_count = 0

file_path = filedialog.askopenfilename()
print("Selected file:", file_path)

with open(file_path, "rt") as f:
    text = f.read()

words = re.findall(r'\S+', text)
word_count = len(words)

for i in text.split("\n"):
    line_count += 1
    
BigBoyWord = "".join(words)

character_count = len(BigBoyWord)

print("")
print(text)
print("")
print("Words :", word_count)
print("Lines :", line_count)
print("Characters :", character_count)
