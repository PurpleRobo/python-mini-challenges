# --------------
#Code starts here
def palindrome(num):
    i = num + 1
    while True:
        str_num = str(i)
        if str_num == str_num[::-1]:
            return i
        else:
            i+=1    


# --------------
#Code starts here
def a_scramble(str_1, str_2):

    str_1 = str_1.lower()
    str_2 = str_2.lower()
    
    for a in str_2:
        if a in str_1:
            str_1 = str_1.replace(a, '', 1)
            print(a)
        else:
            return False

    else:
        return True


# --------------
#Code starts here
def check_fib(num):
    a = -1
    b = 1
    sum1 = 0
    while sum1<=num:
        sum1 = a+b
        a = b
        b = sum1
        
        if sum1 == num:
            return True
    else:
        return False


# --------------
#Code starts here
def compress(word):
    a = word.lower()
    length = len(a)
    a += "  "
    main_count = 0
    return_str = ''

    while True:
        count = 0
        for i in range(main_count, length+1):
            if a[main_count] == a[i]:
                count += 1
            else:
                return_str += f'{a[main_count]}{count}'
                main_count = i
                break
        
        if main_count>=length:
            break
                
    return return_str


# --------------
#Code starts here
def k_distinct(string, k):
    a = string.lower()
    letter_list = []

    for c in a:
        if c not in letter_list:
            letter_list.append(c)
            
    length = len(letter_list)

    if length == k:
        return True
    else:
        return False


