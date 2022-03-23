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


