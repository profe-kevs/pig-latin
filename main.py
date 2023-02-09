def is_consonant(ch): 
    if ch in "aeiou":
        return False
    else :
        return True

def is_consonant_cluster(possible_cluster):
    if(is_consonant(possible_cluster[1])):
        return True
    else:
        return False

def first_condition(first_two_ch):
    return not is_consonant(first_two_ch[0]) or (first_two_ch == "xr" or first_two_ch == "yt") 

def translate(text):
    text_lower = text.lower()
    if(first_condition(text_lower[0:2])):
        return text + "ay"
