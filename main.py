import camelcase, iptonum, calculator

def call_camelcase():
    print(f'Convert snake_case to CamelCase')
    print(f'Output algorithm: {camelcase.algo("_welcome__to-my_paradise_-")}')
    print(f'Output replace:   {camelcase.replace("_welcome__to-my_paradise_")}')
    print(f'Output regexp:    {camelcase.regexp("_welcome__to-my_paradise_")}')
    print(f'')

def call_iptonum():
    print(f'Convert IP to Num')
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
    print(f'Calculator')
    print(f'15 * 3: {calculator.calculator("15 * 3")}')
    print(f'80 / 4: {calculator.calculator("80 / 4")}')
    print(f'')



if __name__ == '__main__':

    #call_camelcase()
    #call_iptonum()
    call_calculator()

