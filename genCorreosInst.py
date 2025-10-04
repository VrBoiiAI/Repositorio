name = input('Ingrese su nombre completo: ').lower().split()
nombre = ''
while True:
    conf = False
    matricula = input('Ingrese su matricula (I-SOFT-XXXXXX): ').replace(' ', '').upper()
    if matricula[0:7] != 'I-SOFT-':
        print('Solo se pueden registrar alumnos de software...')

    elif len(matricula) != 13:
        print('Ingrese una matricula valida...')

    else:
        try:
            int(matricula[7:])
            conf = True

        except:
            print('Ingrese una matricula valida...')

    if conf == True:
        for i in name:
            nombre += i + ' '

        print(f'{matricula} | {nombre.title()}| {name[0]}.{name[-2]}@upnay.edu.mx')
        break
