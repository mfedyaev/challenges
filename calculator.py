operation = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '/': lambda a, b: a / b,
    '*': lambda a, b: a * b
}

# This version is supposed to be faster because dict is not created every time - ?
def calculator2(expression):
    allowed = "+-/*"
    if not any(sign in expression for sign in allowed):
        raise ValueError(f'Expression must contain at least one of: {allowed}')
    for sign in allowed:
        if sign in expression:
            try:
                left, right = expression.split(sign)
                left, right = int(left), int(right)
                return operation.get(sign)(left,right)
            except(ValueError, TypeError):
                raise ValueError(f'Expression must contain two integers and operation ({allowed})')


def calculator1(expression):
    allowed = "+-/*"
    if not any(sign in expression for sign in allowed):
        raise ValueError(f'Expression must contain at least one of: {allowed}')
    for sign in allowed:
        if sign in expression:
            try:
                left, right = expression.split(sign)
                left, right = int(left), int(right)
                return {
                    '+': lambda a, b: a + b,
                    '-': lambda a, b: a - b,
                    '/': lambda a, b: a / b,
                    '*': lambda a, b: a * b
                }[sign](left, right)
            except(ValueError, TypeError):
                raise ValueError(f'Expression must contain two integers and operation ({allowed})')


