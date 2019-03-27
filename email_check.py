import re


def email_check(email):
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
    if match is None:
        return False
    return True

"""
print email_check("email@mai.com")
print email_check("email.mai.com")
print email_check("email@maiddd.com")
"""