# Find if a number is a palindrome: number that reads the same backward or forward
# Reverse and compare
# Optimize - reverse half and compare to the other half - expect even and odd numbers

def is_palindrome_full(num):
    result = "no"
    i = 0
    str_num = str(num)
    j = len(str_num)
    rev_str_num = ""
    for i in range(j):
        rev_str_num += str_num[j-1-i]
    if rev_str_num == str_num:
        result = "yes"
    return result

def is_palindrome_reverse_slice(num):
    result = "no"
    str_num = str(num)
    rev_str_num = str_num[::-1]
    if rev_str_num == str_num:
        result = "yes"
    return result

def is_palindrome_short(num):
    str_num = str(num)
    return ["yes" if str_num[::-1] == str_num else "no"]

def is_palindrome_half(num):
    str_half_len = int(len(str(num))/2)
    str_half_rev = str(num)[:str_half_len:-1]
    if str_half_len % 2 == 0 or str_half_len == 1:
        str_half_num = str(num)[:str_half_len]
    else:
        str_half_num = str(num)[:str_half_len-1]
    #print(f'str_half_num, str_half_rev: {str_half_num, str_half_rev}')
    return ["yes" if str_half_rev == str_half_num else "no"]
