Alfabeto = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
            'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
            'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
            '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'}


def codifcar(mensaje):
    traduccion = []
    for i in mensaje.upper():
        if i in Alfabeto:
            traduccion.append(Alfabeto[i] + ' ')
        elif i == ' ':
            traduccion.append('  ')
    return ''.join(traduccion)


def decodificar(mensaje):
    traduccion = []
    # invertir diccionario para buscar clave valor en codigo morse
    alfabeto_morse = {value: key for key, value in Alfabeto.items()}
    for i in mensaje.split(' '):
        if i in alfabeto_morse:
            traduccion.append(alfabeto_morse[i])
        else:
            traduccion.append(' ')
        
        
    return ''.join(traduccion)


msj = input('introduzca palabra a codificar/decodificar: ')

if msj[0] == '.' or msj[0] == '-':
    print(decodificar(msj))
else:
    print(codifcar(msj))
