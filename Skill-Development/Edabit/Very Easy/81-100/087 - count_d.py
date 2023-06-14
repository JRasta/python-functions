def count_d(sentence):
    sentence = sentence.lower()
    return sentence.count('d')


count_d("My friend Dylan got distracted at school")  # 4
count_d("Debris was scattered all over the place.")  # 2
count_d("The rodents hibernated in their den.")  # 3
