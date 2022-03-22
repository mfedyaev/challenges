import camelcase, iptonum, calculator, recursion_factorial
import two_nums_add_to_k

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

def call_calculator():
    print(f'### Calculator')
    print(f'15 * 3: {calculator.calculator("15 * 3")}')
    print(f'80 / 4: {calculator.calculator("80 / 4")}')
    print(f'')

def call_factorial():
    print(f'### Factorial')
    print(f'Factorial of 5:  {recursion_factorial.factorial(5)}')
    print(f'Factorial of 15: {recursion_factorial.factorial(15)}')
    print(f'')

def call_find_sum():
    print(f'### Factorial')
    print(f'Two number add to k, [1, 2, 3, 4], 5):      {two_nums_add_to_k.find_sum([1, 2, 3, 4], 5)}')
    print(f'Two number add to k, [16, 2, 33, -4], 29):  {two_nums_add_to_k.find_sum([16, 2, 33, 4], 37)}')
    print(f'Two number add to k, [100, 2, 7, 14], 5):   {two_nums_add_to_k.find_sum([100, 2, 7, 14], 5)}')
    print(f'')


if __name__ == '__main__':

    call_camelcase()
    call_iptonum()
    call_calculator()
    call_factorial()
    call_find_sum()

