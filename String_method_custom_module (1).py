def upper_custom(string):
    if type(string)==str:
        empty_lst=[]
        for char in string:
        
            if 97<=ord(char)<=122:
                char=chr(ord(char)-32)
                empty_lst.append(char)
            else:
                empty_lst.append(char)
        return ''.join(empty_lst)
    else:
        return 'please enter string'
    
    
    
def lower_custom(string):
    if type(string)==str:
        empty_lst=[]
        for char in string:
        
            if 65<=ord(char)<=90:
                char=chr(ord(char)+32)
                empty_lst.append(char)
            else:
                empty_lst.append(char)
        return ''.join(empty_lst)
    else:
        return 'please enter string'
    
    
    
    
def capitalize_custom(string):
    if type(string)==str:
        empty_lst=[]
        if 97<=ord(string[0])<=122:
            empty_lst.append(chr(ord(string[0])-32))
            for char in string[1:]:
                if 65<=ord(char)<=90:
                    char=chr(ord(char)+32)
                    empty_lst.append(char)
                else:
                    empty_lst.append(char)
            return ''.join(empty_lst)
        
        
        

def isupper_custom(string):
    if type(string)==str:
        for char in string:
            if 97<=ord(char)<=122:
                return False
    else:        
        return 'please enter string'        
    return True



def islower_custom(string):
    if type(string)==str:
        for char in string:
            if 65<=ord(char)<=90:
                return False
    else:
        return 'please enter string'
    return True


def isalpha_custom(string):
    if type(string)==str:
        for char in string:
            if 0<=ord(char)<=64 or 91<=ord(char)<=96 or 123<=ord(char)<=127:
                return False
            else:
                continue
        return True
    else:
        return 'please enter string'
    
    
    
def isdigit_custom(string):
    if type(string)==str:
        for char in string:
            if 0<=ord(char)<=47 or 58<=ord(char)<=127:
                return False
            else:
                continue
        return True
    else:
        return 'please enter string'
    

    
    
def isalphanum_custom(string):
    if type(string)==str:
        for char in string:
            if 0<=ord(char)<=47 or 58<=ord(char)<=64  or 91<=ord(char)<=96 or 123<=ord(char)<=127:
                return False
            else:
                continue
        return True
    else:
        return 'please enter string'
    

def swapcase_custom(string):
    if type(string)==str:
        empty_lst=[]
        for char in string:
            if 97<=ord(char)<=122:
                empty_lst.append(chr(ord(char)-32))
            elif 65<=ord(char)<=90:
                empty_lst.append(chr(ord(char)+32))
            else:
                empty_lst.append(char)
    else:
        return 'please return string'
    return ''.join(empty_lst) 



def custom_title(string):
    lst = string.split(' ')
    for i in range(len(lst)):
        is_first_alphabet='no'
        x=lst[i]
        s=''
        for character in x:
            if is_first_alphabet=='no':
                if 97 <= ord(character) <= 122:
                    char = chr(ord(character)-32)
                    s=s+char
                    is_first_alphabet='yes'
                elif 65 <= ord(character) <= 90:
                    s=s+character
                    is_first_alphabet='yes'
                else:
                    s=s+character
            elif is_first_alphabet=='yes':
                if 97 <= ord(character) <= 122:
                    s=s+character
                elif 65 <= ord(character) <= 90:
                    char = chr(ord(character)+32)
                    s=s+char
                else:
                    s=s+character
        lst[i]=s
    return ' '.join(lst)