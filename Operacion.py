import math
import graphviz
import uuid
from graphviz import Digraph
class Operacion:
    def __init__(self, tipo):
        self.tipo = tipo
        self.operandos = []
    def generar_grafo(self):
        grafo = graphviz.Digraph(comment=f'Grafo de operación {self.tipo}')
        self.generar_nodos(grafo)
        return grafo
    def generar_nodos(self, grafo):
        id_nodo = str(uuid.uuid4())
        # Agregar etiqueta con el nombre de la operación y el resultado
        etiqueta = f"{self.tipo}: {self.operar()[1]}"
        grafo.node(id_nodo, label=etiqueta,style='filled', fillcolor='green',fontcolor='#FB0000')
        for operando in self.operandos:
            if type(operando) is Operacion:
                id_operando = operando.generar_nodos(grafo)
                grafo.edge(id_nodo, id_operando, fontcolor='#FB0000',color='#0D2BE9')
            else:
                id_operando = str(uuid.uuid4())
                grafo.node(id_operando, label=operando,style='filled', fillcolor='green',fontcolor='#002EFF')
                grafo.edge(id_nodo, id_operando, fontcolor='#FB0000',color='#0D2BE9')
        return id_nodo
    
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
                for i, operando in enumerate(self.operandos):
                    if type(operando) is not Operacion:
                        if i == 0:
                            res += operando + ' - '
                            resnum += float(operando)
                        else:
                            res += operando + ' = '
                            resnum -= float(operando)
                    else:
                        operado = operando.operar()
                        if i == 0:
                            res += "(" + operado[0] + ") - "
                            resnum += operado[1]
                        else:
                            res += "(" + operado[0] + ") = "
                            resnum -= operado[1]       
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
            resnum = None
            for i, operando in enumerate(self.operandos):
                if type(operando) is not Operacion:
                    if i == 0:
                        res += operando + ' / '
                        resnum = float(operando)
                    else:
                        res += operando + ' = '
                        if float(operando) == 0:
                            resnum = None
                            break
                        else:
                            resnum = resnum / float(operando)
                else:
                    operado = operando.operar()
                    if i == 0:
                        res += "(" + operado[0] + ") / "
                        resnum = operado[1]
                    else:
                        res += "(" + operado[0] + ") = "
                        if operado[1] == 0:
                            resnum = None
                            break
                        else:
                            resnum = resnum / operado[1]
            if resnum is None:
                return ["División por cero no es posible", None]
            else:
                pass
        elif self.tipo.lower() == 'potencia':
            resnum = 1
            for i, operando in enumerate(self.operandos):
                if type(operando) is not Operacion:
                    if i == 0:
                        res += operando + ' ^ '
                        resnum = float(operando)
                    else:
                        res += operando + ' = '
                        resnum = resnum ** float(operando)
                else:
                    operado = operando.operar()
                    if i == 0:
                        res += "(" + operado[0] + ") ^ "
                        resnum = operado[1]
                    else:
                        res += "(" + operado[0] + ") = "
                        resnum = resnum ** operado[1]
        elif self.tipo.lower() == 'raiz':
            operando = self.operandos[0]
            if type(operando) is not Operacion:
                if float(operando) < 0:
                    return ["Raíz cuadrada de un número negativo no es posible", None]
                else:
                    res = "√" + operando + " = "
                    resnum = math.sqrt(float(operando))
            else:
                operado = operando.operar()
                if operado[1] < 0:
                    return ["Raíz cuadrada de un número negativo no es posible", None]
                else:
                    res = "√(" + operado[0] + ") = "
                    resnum = math.sqrt(operado[1])
                        
        elif self.tipo.lower() == 'inverso':
            operando = self.operandos[0]
            if type(operando) is not Operacion:
                if float(operando) == 0:
                    return ["No se puede calcular el inverso de cero", None]
                else:
                    res = "1/" + operando + " = "
                    resnum = 1 / float(operando)
            else:
                operado = operando.operar()
                if operado[1] == 0:
                    return ["No se puede calcular el inverso de cero", None]
                else:
                    res = "1/(" + operado[0] + ") = "
                    resnum = 1 / operado[1]

        elif self.tipo.lower() == 'mod':
            resnum = None
            for i, operando in enumerate(self.operandos):
                if type(operando) is not Operacion:
                    if i == 0:
                        res += operando + ' % '
                        resnum = float(operando)
                    else:
                        res += operando + ' = '
                        if float(operando) == 0:
                            resnum = None
                            break
                        else:
                            resnum = resnum % float(operando)
                else:
                    operado = operando.operar()
                    if i == 0:
                        res += "(" + operado[0] + ") % "
                        resnum = operado[1]
                    else:
                        res += "(" + operado[0] + ") = "
                        if operado[1] == 0:
                            resnum = None
                            break
                        else:
                            resnum = resnum % operado[1]
            if resnum is None:
                return ["División por cero no es posible", None]
            else:
                pass
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
