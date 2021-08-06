def is_isogram(string):
    lower_string = string.lower()
    my_string = lower_string.replace(' ','').replace('-','')
    
    if len(my_string) == len(set(my_string)):
        return True
    else:
        return False
