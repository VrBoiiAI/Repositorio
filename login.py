users = {
    "alex99": "X9!vTp3@aR7#",
    "samantha_21": "Q7#zLk5hF2@",
    "david_j": "M3^pR8!wT1$",
    "maria88": "K6!fDn2@xV4%",
    "jason_smith": "R8$gH1!yQ5^",
    "chloe_17": "P2@tV9!kL6#",
    "ryan.miller": "T4^xC7#zB3!",
    "olivia2025": "H5!nQ8@rM2$",
    "ethan_lee": "Z1#sL4!tP9^",
    "grace_w": "C7!yV2^kJ5@"
}
def login():
    i = 1
    while i <= 3:
        user = input('Ingrese su usuario: ')
        passw = input('Ingrese su contraseña: ')
        if user in users and users[user] == passw:
            print('Acceso Permitido')
            break
        if i == 3:
            print('Limite de intentos alcanzado')
            break
        else:
            print('Acceso Denegado\n')
            i += 1

login()
