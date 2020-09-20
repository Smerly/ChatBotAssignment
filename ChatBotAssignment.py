#This is just for the quiz, Have not actually started on the chatbot project yet




def get_animal(get_sound): 
    if get_sound == "meow":
        print("cat")

    elif get_sound == "woof":
        print("dog")

    elif get_sound == "quack":
        print("duck")

    else:
        print("I don't recognize that animal sound")
    return get_sound


get_animal(input("insert a sound"))
