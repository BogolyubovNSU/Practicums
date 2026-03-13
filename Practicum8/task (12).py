import re

def check_name(name: str) -> bool:
    """
    Function. Checks the entered string to see
    if it can be a name in the Python language.

    :param name: the line to check

    :return: True or False
    """
    KEYWORDS = 'and;as;assert;break;class;continue;def;del;elif;else;except;\
    ;False;finally;for;from;global;if;import;in;is;lambda;None;nonlocal;not;\
    ;or;pass;raise;return;True;try;while;with;yield'.split(';')
    acceptable_name = re.sub(r'(?:[^_a-zA-z0-9]|^\d)', '', name)
    if name not in KEYWORDS and len(acceptable_name) == len(name) and name:
        return True
    else:
        return False


if __name__ == '__main__':
    print(check_name(input('Enter a name: ')))