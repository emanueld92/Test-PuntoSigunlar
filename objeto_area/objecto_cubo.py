
class Cuadrado:

    def __init__(self, lado):
        self.lado = lado

    def CalcularArea(self):
        area = self.lado**2
        return area

    def CalcularPerimetro(self):
        perimetroCuadrado = self.lado*4

        return perimetroCuadrado


class Cubo(Cuadrado):

    def CalcularVolumen(self):
        volumen = self.lado**3
        return volumen

    def CalcularPerimetro(self):
        PerimetroCubo = self.lado*12
        return PerimetroCubo


while True:
    print("""
          SELECCIONE UNA OPCION DE CALCULO:
          ---------CALCULOS DE UN CUADRADO--------
          [1]CALCULO DEL AREA DE UN CUADRADO
          [2]CALCULO DEL PERIMETRO DE UN AREA
          ---------CALCULO DE UN CUBO-------------
          [3]CALCULO DEL AREA DE UN CUBO
          [4]CALCULO DEL PERIMETRO DE UN CUBO
          ----------OPCIONES DE MENU--------------
          [R] REGRESAR AL MENU DE CALCULOS
          [Q] SALIR 
          
          """)
    opcion = input('Introduzca opcion del menu: ')
    if opcion.upper() == 'Q':
        break
    elif int(opcion) > 4 or int(opcion) < 1:
        print("OPCION INVALIDA")
        
    else:

        lado = float(input('Introduzca valor del lado: '))
        c = Cuadrado(lado)
        cu = Cubo(lado)

        menu = {
            '1': c.CalcularArea(),
            '2': c.CalcularPerimetro(),
            '3': cu.CalcularVolumen(),
            '4': cu.CalcularPerimetro()
        }
        print('Resultado', menu.get(opcion))
        print("Valor introducido", lado)
    continuar = input("""
    [R] REGRESAR AL MENU DE CALCULOS
    [Q] SALIR 
                        """)

    if (continuar.upper() == 'Q'):
        break
