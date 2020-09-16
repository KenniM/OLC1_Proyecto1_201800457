import ResultadosSintax
def sintaxParentesis(entrada):
    if(entrada!=""):
        listado=entrada.split("\n")
        salida="\t\t---------------------- REPORTE DE ANÁLISIS SINTÁCTICO ------------------\n"
        pilaSintax=[]
        resultados=[]
        interrumpido=False
        i=1
        for test in listado:
            indice=0
            basura=""
            while indice<len(test):
                if test[indice]=="(": pilaSintax.append("(")
                if test[indice]==")": 
                    if len(pilaSintax)>0:
                        basura=pilaSintax.pop()
                    else:
                        resultados.append(ResultadosSintax.ResultadosSintax(test,"INCORRECTO"))
                        interrumpido=True
                indice+=1
            if not interrumpido:
                if len(pilaSintax)==0: 
                    resultados.append(ResultadosSintax.ResultadosSintax(test,"CORRECTO"))
                else: 
                    resultados.append(ResultadosSintax.ResultadosSintax(test,"INCORRECTO"))
            else: interrumpido=False
            indice=0
            pilaSintax.clear()
        for salida_ in resultados:
            salida+=str(i)+".\t"+salida_.linea_+"\t----->\t"+salida_.resultado_+"\n"
            i+=1
        return salida
    else:
        return "El archivo de entrada está vacío"