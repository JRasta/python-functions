def create_id(first, last):
    first = first[:1].lower()
    last = last[:3].capitalize()
    new_id = first + last
    print(new_id)


create_id("mary", "smith")  # "mSmi"
create_id("S", "WORKING")  # "sWor"
create_id("joHN", "wAShington")  # "jWas"
