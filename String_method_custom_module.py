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



def title_custom(string):
    if type(string)==str:
        empty_lst=[]
        if 97<=ord(string[0])<=122:
            empty_lst.append(chr(ord(string[0])-32))
        else:
            empty_lst.append(string[0])
        for char in range(1,len(string)):
            if string[char-1]==' ':
                if 97<=ord(string[char])<=122:
                    empty_lst.append(chr(ord(string[char])-32))
                else:
                    empty_lst.append(string[char])
            else:
                if 65<=ord(string[char])<=90:
                    empty_lst.append(chr(ord(string[char])+32))
                else:
                    empty_lst.append(string[char])
    else:
        return 'please enter string'
    return ''.join(empty_lst)