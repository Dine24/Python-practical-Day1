def valid_number(str):
    i = 0
    j = len(str) - 1
    while i<len(str) and str[i] == ' ':
        i += 1
    while j >= 0 and str[j] == ' ':
        j -= 1
 
    if i > j:
        return False
    if (i == j and not(str[i] >= '0' and
                       str[i] <= '9')):
        return False
    if (str[i] != '.' and str[i] != '+' and
        str[i] != '-' and not(str[i] >= '0' and
        str[i] <= '9')):
        return False
    flagDotOrE = False
 
    for i in range(j + 1):
        if (str[i] != 'e' and str[i] != '.' and
            str[i] != '+' and str[i] != '-' and not
           (str[i] >= '0' and str[i] <= '9')):
            return False
 
        if str[i] == '.':
            if flagDotOrE:
                return False
            if i + 1 > len(str):
                return False
            if (not(str[i + 1] >= '0' and
                    str[i + 1] <= '9')):
                return False
        elif str[i] == 'e':
            flagDotOrE = True
            if (not(str[i - 1] >= '0' and
                    str[i - 1] <= '9')):
                return False
            if i + 1 > len(str):
                return False
            if (str[i + 1] != '+' and str[i + 1] != '-' and
               (str[i + 1] >= '0' and str[i] <= '9')):
                return False
    return True
if __name__ == '__main__':
    str = input("enter a string")
    if valid_number(str):
        print('true')
    else:
        print('false')
