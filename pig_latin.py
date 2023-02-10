def is_consonant(ch): 
    if ch in "aeiou":
        return False
    else :
        return True

    

def first_condition(first_two_ch):
    return not is_consonant(first_two_ch[0]) or (first_two_ch == "xr" or first_two_ch == "yt") 

def translate(text):
    text_lower = text.lower()
    
    if(first_condition(text_lower[:2])):
        return text_lower + "ay"

    y_partition = text_lower.partition("y")
    qu_partition = text_lower.partition("qu")

    if is_consonant(text_lower[1]) and not text_lower[1] == "y" and not text_lower[1] == "u" and not text_lower[1] == "u":
        return text_lower[2:] + text_lower[:2] + "ay"
    
    if not (y_partition[0] == text_lower):
        if y_partition[0] == '':
            return "".join(y_partition[1:]) + y_partition[1] + "ay"
        return "".join(y_partition[1:]) + y_partition[0] + "ay"
    if not (qu_partition[0] == text_lower):
        if qu_partition[0] == '':
            return "".join(qu_partition[2:]) + qu_partition[1] + "ay"
        return "".join(qu_partition[2:]) + "".join(qu_partition[:2]) + "ay"
    
    return text_lower[1:] + text_lower[:1] + "ay"
    