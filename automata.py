from Operacion import Operacion
from Token import Token

class Automata:
    letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s", "t", "u","v","w","x","y","z", "-"]
    numeros = ["1","2","3","4","5","6","7","8","9","0", "."]
    tabla_tokens = []
    cadena = ''
    fila = 0
    columna = 0
    estado_actual = 0
    estado_anterior = 0
    estados_aceptacion = [9]

    def analizar(self, cadena, operacion:Operacion):
        operandos = []
        token = ''
        tipo_operacion = ''
        # error = False

        while len(cadena) > 0:
            char = cadena[0]

            # ignorar espacios en blanco o saltos de linea
            if char == '\n':
                self.fila += 1
                self.columna = 0
                cadena = cadena[1:] #abaab -> #baab
                continue
            elif char == '\t':
                self.columna += 4
                cadena = cadena[1:]
                continue
            elif char == ' ':
                self.columna += 1
                cadena = cadena[1:] #abaab -> #baab
                continue

            if self.estado_actual == 0:
                if char == '{':
                    self.guardar_token(char)
                    self.estado_anterior = 0
                    self.estado_actual = 1
                #else:
                    #error = True
                    #nuevoError = Error(fila, columna, char)

            elif self.estado_actual == 1:
                if char == '"':
                    self.guardar_token(char)
                    self.estado_anterior = 1
                    self.estado_actual = 2
                elif char == '{':
                    self.guardar_token(char)
                    self.estado_anterior = 1
                    self.estado_actual = 10

            elif self.estado_actual == 2:
                if char.lower() in self.letras:
                    token += char
                    self.estado_anterior = 2
                    self.estado_actual = 3
            
            elif self.estado_actual == 3:
                if char.lower() in self.letras:
                    token += char
                    self.estado_anterior = 3
                    self.estado_actual = 3
                elif char == '"':
                    self.guardar_token(token)
                    token = ''
                    self.guardar_token(char)
                    self.estado_anterior = 3
                    self.estado_actual = 4

            elif self.estado_actual == 4:
                if char == ':':
                    self.guardar_token(char)
                    self.estado_anterior = 4
                    self.estado_actual = 5

            elif self.estado_actual == 5:
                if char == '"':
                    self.guardar_token(char)
                    self.estado_anterior = 5
                    self.estado_actual = 6

            elif self.estado_actual == 6:
                if char.lower() in self.letras:
                    token += char
                    self.estado_anterior = 6
                    self.estado_actual = 7
            
            elif self.estado_actual == 7:
                if char.lower() in self.letras:
                    token += char
                    self.estado_anterior = 7
                    self.estado_actual = 7
                elif char == '"':
                    self.guardar_token(token)
                    token = ''
                    self.guardar_token(char)
                    self.estado_anterior = 7
                    self.estado_actual = 8
            
            elif self.estado_actual == 8:
                if char == '}':
                    self.guardar_token(char)
                    self.estado_anterior = 8
                    self.estado_actual = 9
                elif char == ',':
                    self.guardar_token(char)
                    self.estado_anterior = 8
                    self.estado_actual = 1
                    #error = False
                
            elif self.estado_actual == 10:
                if char == '"':
                    self.guardar_token(char)
                    self.estado_anterior = 10
                    self.estado_actual = 11

            elif self.estado_actual == 11:
                if char.lower() in self.letras:
                    token += char
                    self.estado_anterior = 11
                    self.estado_actual = 12
                
            elif self.estado_actual == 12:
                if char.lower() in self.letras:
                    token += char
                    self.estado_anterior = 12
                    self.estado_actual = 12
                elif char == '"':
                    self.guardar_token(token)
                    token = ''
                    self.guardar_token(char)
                    self.estado_anterior = 12
                    self.estado_actual = 13

            elif self.estado_actual == 13:
                if char == ':':
                    self.guardar_token(char)
                    self.estado_anterior = 13
                    self.estado_actual = 14
            
            elif self.estado_actual == 14:
                if char == '"':
                    self.guardar_token(char)
                    self.estado_anterior = 14
                    self.estado_actual = 15
                elif char in self.numeros:
                    token += char
                    self.estado_anterior = 15
                    self.estado_actual = 18
                elif char == '[':
                    self.guardar_token(char)
                    self.estado_anterior = 15
                    self.estado_actual = 19

            elif self.estado_actual == 15:
                if char.lower() in self.letras:
                    token += char
                    self.estado_anterior = 15
                    self.estado_actual = 16
            
            elif self.estado_actual == 16:
                if char.lower() in self.letras:
                    token += char
                    self.estado_anterior = 16
                    self.estado_actual = 16
                elif char == '"':
                    self.guardar_token(token)
                    tipo_operacion = token
                    token = ''
                    self.guardar_token(char)
                    self.estado_anterior = 16
                    self.estado_actual = 17
                    # generar nueva operacion
                    op = Operacion(tipo_operacion)
                    valor = self.analizar(cadena[1:], op)
                    cadena = valor[0]
                    operandos.append(valor[1])
                    

            elif self.estado_actual == 17:
                if char == ',':
                    self.guardar_token(char)
                    self.estado_anterior = 17
                    self.estado_actual = 10

            elif self.estado_actual == 18:
                if char in self.numeros:
                    token += char
                    self.estado_anterior = 18
                    self.estado_actual = 18
                elif char == ',':
                    self.guardar_token(token)
                    operandos.append(token)
                    token = ''
                    self.guardar_token(char)
                    self.estado_anterior = 18
                    self.estado_actual = 10
                elif char == ']':
                    self.guardar_token(token)
                    operandos.append(token)
                    token = ''
                    self.guardar_token(char)
                    self.estado_anterior = 18
                    self.estado_actual = 20
                    operacion.operandos = operandos
                    return [cadena, operacion]
                elif char == '}':
                    self.guardar_token(token)
                    operandos.append(token)
                    token = ''
                    self.guardar_token(char)
                    self.estado_anterior = 18
                    self.estado_actual = 21
                    operacion.operandos = operandos
                    return [cadena, operacion]

            elif self.estado_actual == 19:
                if char == '"':
                    self.guardar_token(char)
                    self.estado_anterior = 19
                    self.estado_actual = 11

            elif self.estado_actual == 20:
                if char == ',':
                    self.guardar_token(char)
                    self.estado_anterior = 20
                    self.estado_actual = 10
                elif char == ']':
                    self.guardar_token(char)
                    self.estado_anterior = 20
                    self.estado_actual = 20
                elif char == '}':
                    self.guardar_token(char)
                    self.estado_anterior = 20
                    self.estado_actual = 21
                    operacion.operandos = operandos
                    return [cadena, operacion]

            elif self.estado_actual == 21:
                if char == '}':
                    self.guardar_token(char)
                    self.estado_anterior = 21
                    self.estado_actual = 9
                elif char == ',':
                    self.guardar_token(char)
                    self.estado_anterior = 21
                    self.estado_actual = 1

            self.columna += 1
            cadena = cadena[1:]

        operacion.operandos = operacion
        return [cadena, operandos]
        #return self.estado_actual in self.estados_aceptacion


    def guardar_token(self, lexema):
        nuevo_token = Token(self.fila, self.columna, lexema)
        self.tabla_tokens.append(nuevo_token)
                
    def imprimir_tokens(self):
        print('-'*31)
        print ("| {:<4} | {:<7} | {:<10} |".format('Fila','Columna','Lexema'))
        print('-'*31)
        for token in self.tabla_tokens:
            print ("| {:<4} | {:<7} | {:<10} |".format(token.fila, token.columna, token.lexema))


# autom = Automata()
# cadena = open(archivo_seleccionado, 'r').read()
# resultado = autom.analizar(cadena, Operacion('suma'))

# #autom.imprimir_tokens()

# if autom.estado_actual in autom.estados_aceptacion:
#     for oper in resultado[1]:
#         resultado = oper.operar()
#         print(resultado[0], "=", resultado[1])