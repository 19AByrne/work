def has_digit(s):
    if len(s) == 0:
        return False
    else:
        if s[0] in ['0','1','2','3','4','5','6','7','8','9']:
            return True
        else:
            if has_digit(s[1:]):
                return True

print(has_digit('a1'))