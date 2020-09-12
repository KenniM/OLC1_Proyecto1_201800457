from PyQt5.QtWidgets import QMessageBox
import Token
import Error
import TipoToken
def lexHTML(entradaHTML):
    entrada=entradaHTML
    print("Analizando el archivo HTML...")
    if(entradaHTML!=""):
        salida=[]
        errores=[]
        fila=1
        columna=1
        caso=0
        indice=0
        auxiliar=""
        colTemporal=0
        filaTemporal=0
        while indice<len(entrada):
            ''' CASO 0: RECONOCER SÍMBOLOS DE ETIQUETAS '''
            if caso==0:
                if entrada[indice]=="<":
                    auxiliar+=entrada[indice]
                    if entrada[indice+1]=="!":
                        auxiliar+=entrada[indice+1]
                        colTemporal=columna
                        filaTemporal=fila
                        indice+=1
                        caso=50
                    else:
                        salida.append(Token(TipoToken(2),auxiliar,fila,columna))
                        auxiliar=""
                        caso=1
                        columna+=1
                elif entrada[indice]==">":
                    auxiliar+=entrada[indice]
                    salida.append(Token(TipoToken(3),auxiliar,fila,columna))
                    auxiliar=""
                    columna+=1
                elif entrada[indice]=="/":
                    auxiliar+=entrada[indice]
                    salida.append(Token(TipoToken(26),auxiliar,fila,columna))
                    auxiliar=""
                    columna+=1
                elif entrada[indice]=="=":
                    auxiliar+=entrada[indice]
                    salida.append(Token(TipoToken(27),auxiliar,fila,columna))
                    auxiliar=""
                    columna+=1
                elif entrada[indice]==" " or entrada[indice]=="\t":columna+=1
                elif entrada[indice]=="\n" or entrada[indice]=="\r\n" or entrada[indice]=="\r":
                    fila+=1
                    columna=1
                elif entrada[indice]=="\"" or entrada[indice]=="\'":
                    indice-=1
                    caso=99
            elif caso==1:
                if entrada[indice]==">":
                    if auxiliar.casefold()=="html".casefold():
                        salida.append(Token(TipoToken(4),auxiliar,fila,columna))
                        auxiliar=""
                        caso=0
                    elif auxiliar.casefold()=="head".casefold():
                        salida.append(Token(TipoToken(5),auxiliar,fila,columna))
                        auxiliar=""
                        caso=0
                    elif auxiliar.casefold()=="title".casefold():
                        salida.append(Token(TipoToken(6),auxiliar,fila,columna))
                        auxiliar=""
                        caso=0
                    elif auxiliar.casefold()=="body".casefold():
                        salida.append(Token(TipoToken(7),auxiliar,fila,columna))
                        auxiliar=""
                        caso=0
                    elif auxiliar.casefold()=="h1".casefold() or auxiliar.casefold()=="h2".casefold() or auxiliar.casefold()=="h3".casefold() or auxiliar.casefold()=="h4".casefold() or auxiliar.casefold()=="h5".casefold() or auxiliar.casefold()=="h6".casefold():
                        salida.append(Token(TipoToken(8),auxiliar,fila,columna))
                        auxiliar=""
                        caso=0
                    elif auxiliar.casefold()=="p".casefold():
                        salida.append(Token(TipoToken(9),auxiliar,fila,columna))
                        auxiliar=""
                        caso=0
                    elif auxiliar.casefold()=="br".casefold():
                        salida.append(Token(TipoToken(25),auxiliar,fila,columna))
                        auxiliar=""
                        caso=0
                    elif auxiliar.casefold()=="img".casefold():
                        salida.append(Token(TipoToken(10),auxiliar,fila,columna))
                        auxiliar=""
                        caso=0
                    elif auxiliar.casefold()=="a".casefold():
                        salida.append(Token(TipoToken(11),auxiliar,fila,columna))
                        auxiliar=""
                        caso=0
                    elif auxiliar.casefold()=="ol".casefold():
                        salida.append(Token(TipoToken(12),auxiliar,fila,columna))
                        auxiliar=""
                        caso=0
                    elif auxiliar.casefold()=="ul".casefold():
                        salida.append(Token(TipoToken(13),auxiliar,fila,columna))
                        auxiliar=""
                        caso=0
                    elif auxiliar.casefold()=="style".casefold():
                        salida.append(Token(TipoToken(14),auxiliar,fila,columna))
                        auxiliar=""
                        caso=0
                    elif auxiliar.casefold()=="table".casefold():
                        salida.append(Token(TipoToken(15),auxiliar,fila,columna))
                        auxiliar=""
                        caso=0
                    elif auxiliar.casefold()=="th".casefold():
                        salida.append(Token(TipoToken(16),auxiliar,fila,columna))
                        auxiliar=""
                        caso=0
                    elif auxiliar.casefold()=="tr".casefold():
                        salida.append(Token(TipoToken(17),auxiliar,fila,columna))
                        auxiliar=""
                        caso=0
                    elif auxiliar.casefold()=="td".casefold():
                        salida.append(Token(TipoToken(18),auxiliar,fila,columna))
                        auxiliar=""
                        caso=0
                    elif auxiliar.casefold()=="caption".casefold():
                        salida.append(Token(TipoToken(19),auxiliar,fila,columna))
                        auxiliar=""
                        caso=0
                    elif auxiliar.casefold()=="colgroup".casefold():
                        salida.append(Token(TipoToken(20),auxiliar,fila,columna))
                        auxiliar=""
                        caso=0
                    elif auxiliar.casefold()=="col".casefold():
                        salida.append(Token(TipoToken(21),auxiliar,fila,columna))
                        auxiliar=""
                        caso=0
                    elif auxiliar.casefold()=="thead".casefold():
                        salida.append(Token(TipoToken(22),auxiliar,fila,columna))
                        auxiliar=""
                        caso=0
                    elif auxiliar.casefold()=="tbody".casefold():
                        salida.append(Token(TipoToken(23),auxiliar,fila,columna))
                        auxiliar=""
                        caso=0
                    elif auxiliar.casefold()=="tfoot".casefold():
                        salida.append(Token(TipoToken(24),auxiliar,fila,columna))
                        auxiliar=""
                        caso=0
                    else:
                        if auxiliar!="":
                            errores.append(Error(TipoToken(100),auxiliar,fila,columna))
                        else:
                            caso=0
                    indice-=1
                elif entrada[indice]=="/":
                    auxiliar+=entrada[indice]
                    salida.append(Token(TipoToken(26),auxiliar,fila,columna))
                    auxiliar=""
                    columna+=1
                elif entrada[indice]=="=":
                    if auxiliar=="src":
                        salida.append(Token(TipoToken(28),auxiliar,fila,columna))
                        salida.append(Token(TipoToken(27),entrada[indice],fila,columna))
                        auxiliar=""
                        caso=0
                    elif auxiliar=="href":
                        salida.append(Token(TipoToken(29),auxiliar,fila,columna))
                        salida.append(Token(TipoToken(27),entrada[indice],fila,columna))
                        auxiliar=""
                        caso=0
                    elif auxiliar=="style":
                        salida.append(Token(TipoToken(14),auxiliar,fila,columna))
                        salida.append(Token(TipoToken(27),entrada[indice],fila,columna))
                        auxiliar=""
                        caso=0
                    elif auxiliar=="border":
                        salida.append(Token(TipoToken(33),auxiliar,fila,columna))
                        salida.append(Token(TipoToken(27),entrada[indice],fila,columna))
                        auxiliar=""
                        caso=0
                    else:
                        errores.append(Error(TipoToken(100),auxiliar,fila,columna))
                        auxiliar=""
                        caso=0
                    indice-=1
                elif entrada[indice]==" ":
                    if auxiliar.casefold()=="html".casefold():
                        salida.append(Token(TipoToken(4),auxiliar,fila,columna))
                        auxiliar=""
                        caso=1
                    elif auxiliar.casefold()=="head".casefold():
                        salida.append(Token(TipoToken(5),auxiliar,fila,columna))
                        auxiliar=""
                        caso=1
                    elif auxiliar.casefold()=="title".casefold():
                        salida.append(Token(TipoToken(6),auxiliar,fila,columna))
                        auxiliar=""
                        caso=1
                    elif auxiliar.casefold()=="body".casefold():
                        salida.append(Token(TipoToken(7),auxiliar,fila,columna))
                        auxiliar=""
                        caso=1
                    elif auxiliar.casefold()=="h1".casefold() or auxiliar.casefold()=="h2".casefold() or auxiliar.casefold()=="h3".casefold() or auxiliar.casefold()=="h4".casefold() or auxiliar.casefold()=="h5".casefold() or auxiliar.casefold()=="h6".casefold():
                        salida.append(Token(TipoToken(8),auxiliar,fila,columna))
                        auxiliar=""
                        caso=1
                    elif auxiliar.casefold()=="p".casefold():
                        salida.append(Token(TipoToken(9),auxiliar,fila,columna))
                        auxiliar=""
                        caso=1
                    elif auxiliar.casefold()=="br".casefold():
                        salida.append(Token(TipoToken(25),auxiliar,fila,columna))
                        auxiliar=""
                        caso=1
                    elif auxiliar.casefold()=="img".casefold():
                        salida.append(Token(TipoToken(10),auxiliar,fila,columna))
                        auxiliar=""
                        caso=1
                    elif auxiliar.casefold()=="a".casefold():
                        salida.append(Token(TipoToken(11),auxiliar,fila,columna))
                        auxiliar=""
                        caso=1
                    elif auxiliar.casefold()=="ol".casefold():
                        salida.append(Token(TipoToken(12),auxiliar,fila,columna))
                        auxiliar=""
                        caso=1
                    elif auxiliar.casefold()=="ul".casefold():
                        salida.append(Token(TipoToken(13),auxiliar,fila,columna))
                        auxiliar=""
                        caso=1
                    elif auxiliar.casefold()=="style".casefold():
                        salida.append(Token(TipoToken(14),auxiliar,fila,columna))
                        auxiliar=""
                        caso=1
                    elif auxiliar.casefold()=="table".casefold():
                        salida.append(Token(TipoToken(15),auxiliar,fila,columna))
                        auxiliar=""
                        caso=1
                    elif auxiliar.casefold()=="th".casefold():
                        salida.append(Token(TipoToken(16),auxiliar,fila,columna))
                        auxiliar=""
                        caso=1
                    elif auxiliar.casefold()=="tr".casefold():
                        salida.append(Token(TipoToken(17),auxiliar,fila,columna))
                        auxiliar=""
                        caso=1
                    elif auxiliar.casefold()=="td".casefold():
                        salida.append(Token(TipoToken(18),auxiliar,fila,columna))
                        auxiliar=""
                        caso=1
                    elif auxiliar.casefold()=="caption".casefold():
                        salida.append(Token(TipoToken(19),auxiliar,fila,columna))
                        auxiliar=""
                        caso=1
                    elif auxiliar.casefold()=="colgroup".casefold():
                        salida.append(Token(TipoToken(20),auxiliar,fila,columna))
                        auxiliar=""
                        caso=1
                    elif auxiliar.casefold()=="col".casefold():
                        salida.append(Token(TipoToken(21),auxiliar,fila,columna))
                        auxiliar=""
                        caso=1
                    elif auxiliar.casefold()=="thead".casefold():
                        salida.append(Token(TipoToken(22),auxiliar,fila,columna))
                        auxiliar=""
                        caso=1
                    elif auxiliar.casefold()=="tbody".casefold():
                        salida.append(Token(TipoToken(23),auxiliar,fila,columna))
                        auxiliar=""
                        caso=1
                    elif auxiliar.casefold()=="tfoot".casefold():
                        salida.append(Token(TipoToken(24),auxiliar,fila,columna))
                        auxiliar=""
                        caso=1
                    else:
                        if auxiliar!="":
                            errores.append(Error(TipoToken(100),auxiliar,fila,columna))
                        else:
                            caso=0
                    indice-=1
            elif caso==50:
                if entrada[indice]=="-":
                    auxiliar+=entrada[indice]
                    caso=51
                    columna+=1
                else:
                    errores.append(Error(TipoToken(100),auxiliar,fila,columna))
                    columna+=1
                    auxiliar=""
                    caso=0
            elif caso==51:
                if entrada[indice]=="-":
                    auxiliar+=entrada[indice]
                    columna+=1
                    caso=52
                else:
                    errores.append(Error(TipoToken(100),auxiliar,fila,columna))
                    auxiliar=""
                    columna+=1
                    caso=0
            elif caso==52:
                if entrada[indice]!="-":
                    auxiliar+=entrada[indice]
                    if entrada[indice]=="\n":
                        fila+=1
                        columna=1
                    else: columna+=1
                else: caso=53
            elif caso==53:
                if entrada[indice]=="-":
                    auxiliar+=entrada[indice]
                    columna+=1
                    caso=54
                else:
                    auxiliar+=entrada[indice]
                    if entrada[indice]=="\n":
                        fila+=1
                        columna=1
                    columna+=1
                    caso=53
            elif caso==54:
                if entrada[indice]=="-":
                    auxiliar+=entrada[indice]
                    columna+=1
                    caso=55
                else:
                    auxiliar+=entrada[indice]
                    if entrada[indice]=="\n":
                        fila+=1
                        columna=1
                    columna+=1
                    caso=53
            elif caso==55:
                if entrada[indice]==">":
                    auxiliar+=entrada[indice]
                    salida.append(Token(TipoToken(32),auxiliar,filaTemporal,colTemporal))
                    columna+=1
                    auxiliar=""
                    caso=0
            elif caso==99:
                while entrada[indice]!="\"" or entrada[indice]!="\'":
                    if entrada[indice]=="\n":
                        columna=1
                        fila+=1
                    else:columna+=1
                    auxiliar+=entrada[indice]
                    indice+=1
                if entrada[indice]=="\"":auxiliar+="\""
                else: auxiliar+="\'"
                salida.append(Token(TipoToken(1),auxiliar,fila,columna))
                auxiliar=""
                caso=0
            indice+=1
    else: 
        msgBox=QMessageBox()
        msgBox.setText("El archivo abierto se encuentra vacío.")
        msgBox.exec()


def lexCSS(entradaCSS):
    print("Analizando el archivo CSS...")
def lexJS(entradaJS):
    print("Analizando el archivo JavaScript...")