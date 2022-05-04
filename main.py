import random


def pass_generator(size: int = 9, string: str = None):
    """
    simple password generator
    :param size:
    :param string:
    :return:
    """
    characters = '!@#$%&*+=-123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    password = ''

    if not string:
        for i in range(size):
            password += random.choice(characters)
        return password
    else:
        if len(string) < size:
            password = string
            for i in range(size - len(string)):
                password += random.choice(characters)
            return password
        else:
            return 'Error: size incompatible'


print(pass_generator())
print(pass_generator(7, 'haha'))
print(pass_generator(2, 'haha'))
print(pass_generator())
