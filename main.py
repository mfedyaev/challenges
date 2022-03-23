import camelcase, iptonum, calculator, recursion_factorial
import palindrome, two_nums_add_to_k, timeit

def call_camelcase():
    print(f'### Convert snake_case to CamelCase')
    print(f'Output algorithm: {camelcase.algo("_welcome__to-my_paradise_-")}')
    print(f'Output replace:   {camelcase.replace("_welcome__to-my_paradise_")}')
    print(f'Output regexp:    {camelcase.regexp("_welcome__to-my_paradise_")}')
    print(f'')

def call_iptonum():
    print(f'### Convert IP to Num')
    print(f'172.0.10.20: {iptonum.iptonum("172.0.10.20")}')
    print(f'192.168.1.1: {iptonum.iptonum("192.168.1.1")}')
    print(f'Convert Num to IP')
    print(f'2885683732:   {iptonum.numtoip(2885683732)}')
    print(f'3232235777:   {iptonum.numtoip(3232235777)}')
    print(f'')
    print(f'### Using ipaddress')
    print(f'Convert IP to Num')
    print(f'172.0.10.20: {iptonum.iptonum_ipaddr("172.0.10.20")}')
    print(f'192.168.1.1: {iptonum.iptonum_ipaddr("192.168.1.1")}')
    print(f'Convert Num to IP')
    print(f'2885683732:   {iptonum.numtoip_ipaddr(2885683732)}')
    print(f'3232235777:   {iptonum.numtoip_ipaddr(3232235777)}')
    print(f'')

def call_calculator1():
    print(f'### Calculator 1')
    print(f'15 * 3: {calculator.calculator1("15 * 3")}')
    print(f'80 / 4: {calculator.calculator1("80 / 4")}')
    print(f'')

def call_calculator2():
    print(f'### Calculator 2')
    print(f'15 * 3: {calculator.calculator2("15 * 3")}')
    print(f'80 / 4: {calculator.calculator2("80 / 4")}')
    print(f'')

def call_factorial():
    print(f'### Factorial')
    print(f'Factorial of 5:  {recursion_factorial.factorial(5)}')
    print(f'Factorial of 15: {recursion_factorial.factorial(15)}')
    print(f'')

def call_find_sum():
    print(f'### two number that add up to k')
    print(f'Two number add to k, [1, 2, 3, 4], 5):      {two_nums_add_to_k.find_sum([1, 2, 3, 4], 5)}')
    print(f'Two number add to k, [16, 2, 33, -4], 29):  {two_nums_add_to_k.find_sum([16, 2, 33, 4], 37)}')
    print(f'Two number add to k, [100, 2, 7, 14], 5):   {two_nums_add_to_k.find_sum([100, 2, 7, 14], 5)}')
    print(f'')

def call_palindrome_full():
    print(f'### Palindrome - full')
    print(f'Is 313 a palindrome: {palindrome.is_palindrome_full(313)}')
    print(f'Is 4422552244 a palindrome: {palindrome.is_palindrome_full(4422552244)}')
    print(f'Is 442252244 a palindrome: {palindrome.is_palindrome_full(442252244)}')
    print(f'Is 442552244 a palindrome: {palindrome.is_palindrome_full(4425552244)}')
    print(f'')

def call_palindrome_reverse_slice():
    print(f'### Palindrome - reverse slice')
    print(f'Is 313 a palindrome: {palindrome.is_palindrome_reverse_slice(313)}')
    print(f'Is 4422552244 a palindrome: {palindrome.is_palindrome_reverse_slice(4422552244)}')
    print(f'Is 442252244 a palindrome: {palindrome.is_palindrome_reverse_slice(442252244)}')
    print(f'Is 442552244 a palindrome: {palindrome.is_palindrome_reverse_slice(4425552244)}')
    print(f'')


if __name__ == '__main__':

    call_camelcase()
    call_iptonum()
    call_factorial()
    call_find_sum()
    call_palindrome_full()
    call_palindrome_reverse_slice()
    call_calculator1()
    call_calculator2()
    #print(f' Timeit Calc1: {timeit.timeit("call_calculator1()", "from __main__ import call_calculator1", number=10000)}')
    #print(f' Timeit Calc2: {timeit.timeit("call_calculator2()", "from __main__ import call_calculator2", number=10000)}')
