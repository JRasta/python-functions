def add(char, string):
    x = string.replace(' ', char)
    print(x)


add("#", "hello world")  # "hello#world"
add("R", "python is fun")  # "pythonRisRfun"
add("*", "use .join() for this challenge")  # "use*.join()*for*this*challenge"
add("#", " ")  # "#"
