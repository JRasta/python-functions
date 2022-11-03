import sys, keyword

print('Python Version:', sys.version)
print('Python Interpreter Location:', sys.executable)
print('\nPython Module Path: ')
for directory in sys.path:
    print(directory)

print('\nPython keywords: ')
for word in keyword.kwlist:
    print(word)
