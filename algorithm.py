def search(text, pattern):
    M = len(pattern) 
    N = len(text)

    from hash_function import initial_hash_function
    from hash_function import hash_function
    from hash_function import get_hash_value

    h = get_hash_value(M)
    NEAREST_PRIME = 29

    value = initial_hash_function(pattern)
    remainder_pattern,quotient_pattern = [value % NEAREST_PRIME, value // NEAREST_PRIME]

    character_set = list(text[:M])
    value = initial_hash_function(character_set)
    remainder_text,quotient_text  = [value % NEAREST_PRIME, value // NEAREST_PRIME]

    for i in range(M,N):
        if remainder_pattern == remainder_text and quotient_pattern == quotient_text:
            return i - M
        else:
            # print(text[i])
            value = hash_function(value,text[i],character_set,h)
            remainder_text,quotient_text  = [value%NEAREST_PRIME,value//NEAREST_PRIME]

    if remainder_pattern == remainder_text and quotient_pattern == quotient_text:
        return N-M
    return None
