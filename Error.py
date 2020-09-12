class Error:
    def __init__(self,tipoToken,valor,fila,columna):
        self.tipo=tipoToken
        self.val=valor
        self.fila_=fila
        self.columna_=columna
