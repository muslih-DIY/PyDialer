import string
import secrets

alphabet = string.ascii_letters + string.digits + '!@#$%&*()=?'


def generate_token(user:str,uniq:str):
    return ''.join(secrets.choice(user+alphabet+str(uniq)) for i in range(20))
