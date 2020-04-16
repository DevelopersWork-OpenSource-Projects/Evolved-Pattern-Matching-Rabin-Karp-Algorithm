CHARACTER_VALUE = lambda x: ord(x) - 64
TOTAL_CHARACTERS = 26
NEAREST_PRIME = 29

def get_hash_value(m):
    return ((TOTAL_CHARACTERS)**(m-1))

def initial_hash_function(string):
    # print(string)
    value = 0
    for i in string:
        value = value * TOTAL_CHARACTERS + CHARACTER_VALUE(i)
    # print(string," - value:",value)
    return value

def hash_function(pre_value,post,character_set,h):

    prev = CHARACTER_VALUE(character_set[0]) * h

    pre_value = (pre_value - prev) 

    pre_value = pre_value * TOTAL_CHARACTERS

    character_set.pop(0)
    
    character_set.append(post)
    
    pre_value = pre_value + CHARACTER_VALUE(post)

    return pre_value
