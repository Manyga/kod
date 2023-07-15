def is_anagram(str1, str2):
    str1 = str1.lower().replace(" ", "")
    str2 = str2.lower().replace(" ", "")
    if len(str1) != len(str2):
        return False
    
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)
    if sorted_str1 != sorted_str2:
        return False

    set_str1 = set(str1)
    set_str2 = set(str2)
    if set_str1 != set_str2:
        return False

    return True

str1 = "обезьянство"
str2 = "светобоязнь"
if is_anagram(str1, str2):
    print('кайф')
else:
    print("не кайф")

