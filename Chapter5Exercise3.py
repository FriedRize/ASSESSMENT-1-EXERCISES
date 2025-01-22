glossary = {
    "variable": "A named storage for data that can be changed during program execution.",
    "function": "A block of reusable code that performs a specific task.",
    "loop": "A structure that repeats a block of code as long as a condition is met.",
    "list": "An ordered collection of items that can be of different data types.",
    "dictionary": "A collection of key-value pairs, used to store data with unique keys.",
    "tuple": "An immutable ordered collection of items.",
    "set": "An unordered collection of unique items.",
    "if-statement": "A conditional structure that executes a block of code if a condition is true.",
    "elif": "Used to test additional conditions if the previous ones are false.",
    "class": "A blueprint for creating objects in object-oriented programming."
}

for word, meaning in glossary.items():
    print(f"{word.title()}:\n{meaning}\n")
