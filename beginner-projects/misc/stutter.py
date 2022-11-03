def stutter(word):
    stutter_letters = word[0:2]
    new_word = stutter_letters + '...' + stutter_letters + '...' + word + '?'
    print(new_word)


stutter("incredible")
stutter("enthusiastic")
stutter("outstanding")
