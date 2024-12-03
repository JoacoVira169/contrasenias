import random as r, string as s

characters = s.ascii_letters + s.ascii_lowercase + s.ascii_uppercase + s.digits + s.punctuation

pass_length = int(input('¿Qué tan larga será la contraseña?'))
password = ''

for i in range(pass_length):
    password += r.choice(characters)
print('Tu contraseña es: ', password)