
Alfabeto={'A': '.-', 'B':'-...','C':'-.-.', 'D':'-..','E':'.','F':'..-.','G':'--.','H':'....',
          'I':'..','J':'.---','K':'-.-','L':'.-..','M':'--','N':'-.','O':'---','P':'.--.',
          'Q':'--.-','R':'.-.','S':'...','T':'-','U':'..-','V':'...-','W':'.--','X':'-..-',
          'Y':'-.--','Z':'--..','1':'.----','2':'..---','3':'...--','4':'....-','5':'.....',
          '6':'-....','7':'--...','8':'---..','9':'----.','0':'-----'}


def codifcar(mensaje):
    traduccion=[]
    for i in mensaje.upper():
        if i in Alfabeto:
            traduccion.append(Alfabeto[i]+ ' ')
        elif i == ' ':
            traduccion.append('  ')
    return ''.join(traduccion)     

#.... --- .-.. .-   -- ..- -. -.. ---   . -.   -- --- .-. ... .   ... --- -.--   . -- .- -. ..- . .-..
def decodificar(mensaje):
    traduccion=[]
    a= mensaje.split(' ')
    espacios=[]
    conta=0
    #invertir diccionario para buscar clave valor en codigo morse
    alfabeto_morse={v: k for k,v in Alfabeto.items()}
    for l in mensaje:
        if l==' ':
           espacios.append(conta)
        conta+=1 
    
    print(espacios)
    
    for i in a:
        if i in alfabeto_morse:
            traduccion.append(alfabeto_morse[i])
        
        
    return ' '.join(traduccion)

        
    
msj= input('introduzca palabra a codificar/decodificar: ')

if msj[0]=='.' or msj[0]=='-':
    print(decodificar(msj))
else:
    
    print(codifcar(msj))    

        

    
    
    
    

