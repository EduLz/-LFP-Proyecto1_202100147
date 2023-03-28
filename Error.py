class Error:
    def __init__(self, fila, columna, lexema):
        self.fila = fila
        self.columna = columna
        self.lexema = lexema
    def generar_cadena(self, posicion):
      return  "\t{\n"\
                '\t\t"No.":'+str(posicion)+'\n'\
                '\t\t"Descripcion-Token":{\n'\
                '\t\t\t"Lexema":'+str(self.lexema)+'\n'\
                '\t\t\t"Tipo": Error\n'\
                '\t\t\t"Columna":'+str(self.fila)+'\n'\
                '\t\t\t"Fila":'+str(self.columna)+'\n'\
                '\t\t}\n'\
        '\t}'
        