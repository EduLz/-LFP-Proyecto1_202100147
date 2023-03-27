import math
class Operacion:
    def __init__(self, tipo):
        self.tipo = tipo
        self.operandos = []

    def operar(self):
        res = '' # 1 + (1 + 1) = 3
        resnum = 0
        if self.tipo.lower() == 'suma':
            for operando in self.operandos:
                if type(operando) is not Operacion:
                    res += operando + ' + '
                    resnum += float(operando)
                else:
                    operado = operando.operar()
                    if type(operado) is list:
                        res += "(" + operado[0] + ") + "
                        resnum += operado[1]
                    else:
                        res += "(" + operado + ") + "
                        resnum += float(operado)   
        elif self.tipo.lower() == 'resta':
            for operando in self.operandos:
                if type(operando) is not Operacion:
                    res += operando + ' - '
                    resnum -= float(operando)
                else:
                    operado = operando.operar()
                    if type(operado) is list:
                        res += "(" + operado[0] + ") - "
                        resnum -= operado[1]
                    else:
                        res += "(" + operado + ") - "
                        resnum -= float(operado)           
        elif self.tipo.lower() == 'multiplicacion':
            resnum = 1
            for operando in self.operandos:
                if type(operando) is not Operacion:
                    res += operando + ' * '
                    resnum = resnum * float(operando)
                else:
                    operado = operando.operar()
                    if type(operado) is list:
                        res += "(" + operado[0] + ") * "
                        resnum = resnum * operado[1]
                    else:
                        res += "(" + operado + ") * "
                        resnum = resnum * float(operado)
        elif self.tipo.lower() == 'division':
            resnum = 1
            for operando in self.operandos:
                if type(operando) is not Operacion:
                    res += operando + ' / '
                    resnum /= float(operando)
                else:
                    operado = operando.operar()
                    if type(operado) is list:
                        res += "(" + operado[0] + ") / "
                        resnum /= operado[1]
                    else:
                        res += "(" + operado + ") / "
                        resnum /= float(operado)
        elif self.tipo.lower() == 'potencia':
            resnum = 1
            for operando in self.operandos:
                if type(operando) is not Operacion:
                    res += operando + ' ** '
                    resnum = resnum ** float(operando)
                else:
                    operado = operando.operar()
                    if type(operado) is list:
                        res += "(" + operado[0] + ") ** "
                        resnum = resnum ** operado[1]
                    else:
                        res += "(" + operado + ") ** "
                        resnum = resnum ** float(operado)
        elif self.tipo.lower() == 'raiz':
            resnum = 1
            for operando in self.operandos:
                if type(operando) is not Operacion:
                    res += 'sqrt(' + operando + ')'
                    resnum = math.sqrt(float(operando))
                else:
                    operado = operando.operar()
                    if type(operado) is list:
                        res += "sqrt(" + operado[0] + ")"
                        resnum = math.sqrt(operado[1])
                    else:
                        res += "sqrt(" + operado + ")"
                        resnum = math.sqrt(float(operado))
                        
        elif self.tipo.lower() == 'inverso':
            resnum = 1
            for operando in self.operandos:
                if type(operando) is not Operacion:
                    res += '1/' + operando
                    resnum = 1 / float(operando)
                else:
                    operado = operando.operar()
                    if type(operado) is list:
                        res += "1/(" + operado[0] + ")"
                        resnum = 1 / operado[1]
                    else:
                        res += "1/(" + operado + ")"
                        resnum = 1 / float(operado)

        elif self.tipo.lower() == 'mod':
            resnum = 1
            for operando in self.operandos:
                if type(operando) is not Operacion:
                    res += operando + ' % '
                    resnum = resnum % float(operando)
                else:
                    operado = operando.operar()
                    if type(operado) is list:
                        res += "(" + operado[0] + ") % "
                        resnum = resnum % operado[1]
                    else:
                        res += "(" + operado + ") % "
                        resnum = resnum % float(operado) 
        elif self.tipo.lower() == 'seno':
            resnum = math.sin(float(self.operandos[0]))
            res = f'sin({self.operandos[0]})'

        elif self.tipo.lower() == 'coseno':
            resnum = math.cos(float(self.operandos[0]))
            res = f'cos({self.operandos[0]})'

        elif self.tipo.lower() == 'tangente':
            resnum = math.tan(float(self.operandos[0]))
            res = f'tan({self.operandos[0]})'                       
        return [res[0:-3], resnum]
