from PyQt5.QtWidgets import QMessageBox
import Token
import TokenJS
import Error
import TipoToken
import os
def generarReporte(ruta,salida,errores):
    contenidoHTML=""
    contenidoHTML+="<!DOCTYPE html>\n"
    contenidoHTML+="<html>"+"\n"
    contenidoHTML+="<head>"+"\n"
    contenidoHTML+="<title> RESULTADOS DEL ANÁLISIS</title>"+"\n"
    contenidoHTML+="<meta charset = 'utf-8'>"+"\n"
    contenidoHTML+="</head> "+"\n"
    contenidoHTML+="<body style = 'background-color: #212121;"+"\n"
    contenidoHTML+="font-family: Microsoft Jhenghei UI; '> "+"\n"
    contenidoHTML+="<h1 class='titulos'>LISTA DE TOKENS</h1> "+"\n"
    contenidoHTML+="<center>"+"\n"
    contenidoHTML+="<div class='contenedor'>"+"\n"
    contenidoHTML+="<table class='Tabla'>"+"\n"
    contenidoHTML+="<tr>"+"\n"
    contenidoHTML+="<th class='encabezados'>#</th>"+"\n"
    contenidoHTML+="<th class='encabezados'>Lexema</th>"+"\n"
    contenidoHTML+="<th class='encabezados'>Fila</th>"+"\n"
    contenidoHTML+="<th class='encabezados'>Columna</th>"+"\n"
    contenidoHTML+="<th class='encabezados'>Token</th>"+"\n"
    contenidoHTML+="</tr>"+"\n"
    contenidoHTML+="<!-- FILAS -->"+"\n"
    contadorTokens=1
    for tokens in salida:
        contenidoHTML+="<tr class='filas'>\n"
        contenidoHTML+="<td class='filas'>"+str(contadorTokens)+"</td>\n"
        if tokens.tipo.name=="COMENTARIO":
            temp1=tokens.val.replace("<!--","")
            temp2=temp1.replace("-->","")
            contenidoHTML+="<td class='filas'>"+temp2+"</td>\n"
        else:
            contenidoHTML+="<td class='filas'>"+str(tokens.val)+"</td>\n"
        contenidoHTML+="<td class='filas'>"+str(tokens.fila_)+"</td>\n"
        contenidoHTML+="<td class='filas'>"+str(tokens.columna_)+"</td>\n"
        contenidoHTML+="<td class='filas'>"+tokens.tipo.name+"</td>\n"
        contenidoHTML+="</tr>\n"
        contadorTokens+=1
    contenidoHTML+="</table>\n"
    contenidoHTML+="</div>\n"
    contenidoHTML+="</center>\n"
    contenidoHTML+="<h1 class='titulos'>LISTA DE ERRORES</h1>\n"
    if len(errores)==0:
        contenidoHTML+="<h4 class='noErrores'>¡No se han detectado errores!</h4>\n"
    else:
        contenidoHTML+="<h4 class='siErrores'>Se han detectado errores, los mismos se muestran a continuación</h4>\n"
        contenidoHTML+="<center>\n"
        contenidoHTML+="<div class='contenedor'>\n"
        contenidoHTML+="<table class='Tabla'>\n"
        contenidoHTML+="<tr>\n"
        contenidoHTML+="<th class='encabezados'>#</th>\n"
        contenidoHTML+="<th class='encabezados'>Fila</th>\n"
        contenidoHTML+="<th class='encabezados'>Columna</th>\n"
        contenidoHTML+="<th class='encabezados'>Carácter</th>\n"
        contenidoHTML+="<th class='encabezados'>Descripción</th>\n"
        contenidoHTML+="</tr>\n"
        contenidoHTML+="<!-- FILAS -->\n"
        contadorTokens=1
        for error in errores:
            contenidoHTML+="<tr class='filas'>\n"
            contenidoHTML+="<td class='filas'>" + str(contadorTokens) + "</td>\n"
            contenidoHTML+="<td class='filas'>" + str(error.fila_) + "</td>\n"
            contenidoHTML+="<td class='filas'>" + str(error.columna_) + "</td>\n"
            contenidoHTML+="<td class='filas'>" + str(error.val) + "</td>\n"
            contenidoHTML+="<td class='filas'>" + error.tipo.name + "</td>\n"
            contenidoHTML+="</tr>\n"
            contadorTokens+=1
    contenidoHTML+="</table>\n"
    contenidoHTML+="</div>\n"
    contenidoHTML+="</center>\n"
    contenidoHTML+="</body>\n"
    contenidoHTML+="<style type= 'text/css'>\n"
    contenidoHTML+=".titulos{\n"
    contenidoHTML+="text-align: center;\n"
    contenidoHTML+="background-color: black;\n"
    contenidoHTML+="color: white;\n"
    contenidoHTML+="}\n"
    contenidoHTML+=".contenedor{\n"
    contenidoHTML+="display: block;\n"
    contenidoHTML+="}\n"
    contenidoHTML+=".encabezados{\n"
    contenidoHTML+="width: 200px;\n"
    contenidoHTML+="height: 20px;\n"
    contenidoHTML+="padding: 5px;\n"
    contenidoHTML+="background-color: black;\n"
    contenidoHTML+="color:white;\n"
    contenidoHTML+="border-style: solid;\n"
    contenidoHTML+="border-width: 2px;\n"
    contenidoHTML+="border-color: white;\n"
    contenidoHTML+="}\n"
    contenidoHTML+=".filas{\n"
    contenidoHTML+="text-align: center;\n"
    contenidoHTML+="width: 200px;\n"
    contenidoHTML+="height: 20px;\n"
    contenidoHTML+="padding: 5px;\n"
    contenidoHTML+="background-color: white;\n"
    contenidoHTML+="color:black;\n"
    contenidoHTML+="border-style: solid;\n"
    contenidoHTML+="border-width: 2px;\n"
    contenidoHTML+="border-color: black;\n"
    contenidoHTML+="}\n"
    contenidoHTML+=".noErrores{\n"
    contenidoHTML+="padding-top: 5px;\n"
    contenidoHTML+="padding-bottom: 5px;\n"
    contenidoHTML+="text-align: center;\n"
    contenidoHTML+="background-color: green;\n"
    contenidoHTML+="color: white;\n"
    contenidoHTML+="}\n"
    contenidoHTML+=".siErrores{\n"
    contenidoHTML+="padding-top: 5px;\n"
    contenidoHTML+="padding-bottom: 5px;\n"
    contenidoHTML+="text-align: center;\n"
    contenidoHTML+="background-color: red;\n"
    contenidoHTML+="color: white;\n"
    contenidoHTML+="}\n"
    contenidoHTML+="</style>\n"
    contenidoHTML+="</html>\n"
    reporte=open(ruta,"w")
    reporte.write(contenidoHTML)
    reporte.close()
    os.startfile(ruta)

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
                        salida.append(Token.Token(TipoToken.TipoToken(2),auxiliar,fila,columna))
                        auxiliar=""
                        caso=1
                        columna+=1
                elif entrada[indice]==">":
                    auxiliar+=entrada[indice]
                    salida.append(Token.Token(TipoToken.TipoToken(3),auxiliar,fila,columna))
                    auxiliar=""
                    columna+=1
                elif entrada[indice]=="/":
                    auxiliar+=entrada[indice]
                    salida.append(Token.Token(TipoToken.TipoToken(26),auxiliar,fila,columna))
                    auxiliar=""
                    columna+=1
                elif entrada[indice]=="=":
                    auxiliar+=entrada[indice]
                    salida.append(Token.Token(TipoToken.TipoToken(27),auxiliar,fila,columna))
                    auxiliar=""
                    columna+=1
                elif entrada[indice]==" " or entrada[indice]=="\t":columna+=1
                elif entrada[indice]=="\n" or entrada[indice]=="\r\n" or entrada[indice]=="\r":
                    fila+=1
                    columna=1
                elif entrada[indice]=="\"":
                    auxiliar+=entrada[indice]
                    caso=99
                elif entrada[indice]=="\'":
                    auxiliar+=entrada[indice]
                    caso=100
                else:
                    auxiliar+=entrada[indice]
                    if entrada[indice]==" " or entrada[indice]=="\t":columna+=1
                    elif entrada[indice]=="\n" or entrada[indice]=="\r\n" or entrada[indice]=="\r":
                        fila+=1
                        columna=1
                    caso=25
            elif caso==1:
                if entrada[indice]==">":
                    if auxiliar.casefold()=="html".casefold():
                        salida.append(Token.Token(TipoToken.TipoToken(4),auxiliar,fila,columna))
                        auxiliar=""
                        caso=0
                    elif auxiliar.casefold()=="head".casefold():
                        salida.append(Token.Token(TipoToken.TipoToken(5),auxiliar,fila,columna))
                        auxiliar=""
                        caso=0
                    elif auxiliar.casefold()=="title".casefold():
                        salida.append(Token.Token(TipoToken.TipoToken(6),auxiliar,fila,columna))
                        auxiliar=""
                        caso=0
                    elif auxiliar.casefold()=="body".casefold():
                        salida.append(Token.Token(TipoToken.TipoToken(7),auxiliar,fila,columna))
                        auxiliar=""
                        caso=0
                    elif auxiliar.casefold()=="h1".casefold() or auxiliar.casefold()=="h2".casefold() or auxiliar.casefold()=="h3".casefold() or auxiliar.casefold()=="h4".casefold() or auxiliar.casefold()=="h5".casefold() or auxiliar.casefold()=="h6".casefold():
                        salida.append(Token.Token(TipoToken.TipoToken(8),auxiliar,fila,columna))
                        auxiliar=""
                        caso=0
                    elif auxiliar.casefold()=="p".casefold():
                        salida.append(Token.Token(TipoToken.TipoToken(9),auxiliar,fila,columna))
                        auxiliar=""
                        caso=0
                    elif auxiliar.casefold()=="br".casefold():
                        salida.append(Token.Token(TipoToken.TipoToken(25),auxiliar,fila,columna))
                        auxiliar=""
                        caso=0
                    elif auxiliar.casefold()=="img".casefold():
                        salida.append(Token.Token(TipoToken.TipoToken(10),auxiliar,fila,columna))
                        auxiliar=""
                        caso=0
                    elif auxiliar.casefold()=="a".casefold():
                        salida.append(Token.Token(TipoToken.TipoToken(11),auxiliar,fila,columna))
                        auxiliar=""
                        caso=0
                    elif auxiliar.casefold()=="ol".casefold():
                        salida.append(Token.Token(TipoToken.TipoToken(12),auxiliar,fila,columna))
                        auxiliar=""
                        caso=0
                    elif auxiliar.casefold()=="ul".casefold():
                        salida.append(Token.Token(TipoToken.TipoToken(13),auxiliar,fila,columna))
                        auxiliar=""
                        caso=0
                    elif auxiliar.casefold()=="style".casefold():
                        salida.append(Token.Token(TipoToken.TipoToken(14),auxiliar,fila,columna))
                        auxiliar=""
                        caso=0
                    elif auxiliar.casefold()=="table".casefold():
                        salida.append(Token.Token(TipoToken.TipoToken(15),auxiliar,fila,columna))
                        auxiliar=""
                        caso=0
                    elif auxiliar.casefold()=="th".casefold():
                        salida.append(Token.Token(TipoToken.TipoToken(16),auxiliar,fila,columna))
                        auxiliar=""
                        caso=0
                    elif auxiliar.casefold()=="tr".casefold():
                        salida.append(Token.Token(TipoToken.TipoToken(17),auxiliar,fila,columna))
                        auxiliar=""
                        caso=0
                    elif auxiliar.casefold()=="td".casefold():
                        salida.append(Token.Token(TipoToken.TipoToken(18),auxiliar,fila,columna))
                        auxiliar=""
                        caso=0
                    elif auxiliar.casefold()=="caption".casefold():
                        salida.append(Token.Token(TipoToken.TipoToken(19),auxiliar,fila,columna))
                        auxiliar=""
                        caso=0
                    elif auxiliar.casefold()=="colgroup".casefold():
                        salida.append(Token.Token(TipoToken.TipoToken(20),auxiliar,fila,columna))
                        auxiliar=""
                        caso=0
                    elif auxiliar.casefold()=="col".casefold():
                        salida.append(Token.Token(TipoToken.TipoToken(21),auxiliar,fila,columna))
                        auxiliar=""
                        caso=0
                    elif auxiliar.casefold()=="thead".casefold():
                        salida.append(Token.Token(TipoToken.TipoToken(22),auxiliar,fila,columna))
                        auxiliar=""
                        caso=0
                    elif auxiliar.casefold()=="tbody".casefold():
                        salida.append(Token.Token(TipoToken.TipoToken(23),auxiliar,fila,columna))
                        auxiliar=""
                        caso=0
                    elif auxiliar.casefold()=="tfoot".casefold():
                        salida.append(Token.Token(TipoToken.TipoToken(24),auxiliar,fila,columna))
                        auxiliar=""
                        caso=0
                    elif auxiliar.casefold()=="div".casefold():
                        salida.append(Token.Token(TipoToken.TipoToken(34),auxiliar,fila,columna))
                        auxiliar=""
                        caso=1
                    elif auxiliar.casefold()=="footer".casefold():
                        salida.append(Token.Token(TipoToken.TipoToken(35),auxiliar,fila,columna))
                        auxiliar=""
                        caso=1
                    elif auxiliar.casefold()=="script".casefold():
                        salida.append(Token.Token(TipoToken.TipoToken(38),auxiliar,fila,columna))
                        auxiliar=""
                        caso=1
                    elif auxiliar.casefold()=="link".casefold():
                        salida.append(Token.Token(TipoToken.TipoToken(40),auxiliar,fila,columna))
                        auxiliar=""
                        caso=1
                    else:
                        if auxiliar!="":
                            errores.append(Error.Error(TipoToken.TipoToken(100),auxiliar,fila,columna))
                            auxiliar=""
                            caso=0
                        else:
                            caso=0
                    indice-=1
                elif entrada[indice]=="/":
                    auxiliar+=entrada[indice]
                    salida.append(Token.Token(TipoToken.TipoToken(26),auxiliar,fila,columna))
                    auxiliar=""
                    columna+=1
                elif entrada[indice]=="=":
                    if auxiliar.casefold()=="src".casefold():
                        salida.append(Token.Token(TipoToken.TipoToken(28),auxiliar,fila,columna))
                        salida.append(Token.Token(TipoToken.TipoToken(27),entrada[indice],fila,columna))
                        auxiliar=""
                        caso=0
                    elif auxiliar.casefold()=="href".casefold():
                        salida.append(Token.Token(TipoToken.TipoToken(29),auxiliar,fila,columna))
                        salida.append(Token.Token(TipoToken.TipoToken(27),entrada[indice],fila,columna))
                        auxiliar=""
                        caso=0
                    elif auxiliar.casefold()=="style".casefold():
                        salida.append(Token.Token(TipoToken.TipoToken(14),auxiliar,fila,columna))
                        salida.append(Token.Token(TipoToken.TipoToken(27),entrada[indice],fila,columna))
                        auxiliar=""
                        caso=0
                    elif auxiliar.casefold()=="border".casefold():
                        salida.append(Token.Token(TipoToken.TipoToken(33),auxiliar,fila,columna))
                        salida.append(Token.Token(TipoToken.TipoToken(27),entrada[indice],fila,columna))
                        auxiliar=""
                        caso=0
                    elif auxiliar.casefold()=="class".casefold():
                        salida.append(Token.Token(TipoToken.TipoToken(36),auxiliar,fila,columna))
                        salida.append(Token.Token(TipoToken.TipoToken(27),entrada[indice],fila,columna))
                        auxiliar=""
                        caso=0
                    elif auxiliar.casefold()=="id".casefold():
                        salida.append(Token.Token(TipoToken.TipoToken(37),auxiliar,fila,columna))
                        salida.append(Token.Token(TipoToken.TipoToken(27),entrada[indice],fila,columna))
                        auxiliar=""
                        caso=0
                    elif auxiliar.casefold()=="type".casefold():
                        salida.append(Token.Token(TipoToken.TipoToken(39),auxiliar,fila,columna))
                        salida.append(Token.Token(TipoToken.TipoToken(27),entrada[indice],fila,columna))
                        auxiliar=""
                        caso=0
                    elif auxiliar.casefold()=="scope".casefold():
                        salida.append(Token.Token(TipoToken.TipoToken(41),auxiliar,fila,columna))
                        salida.append(Token.Token(TipoToken.TipoToken(27),entrada[indice],fila,columna))
                        auxiliar=""
                        caso=0
                    elif auxiliar.casefold()=="rel".casefold():
                        salida.append(Token.Token(TipoToken.TipoToken(42),auxiliar,fila,columna))
                        salida.append(Token.Token(TipoToken.TipoToken(27),entrada[indice],fila,columna))
                        auxiliar=""
                        caso=0
                    else:
                        errores.append(Error.Error(TipoToken.TipoToken(100),auxiliar,fila,columna))
                        auxiliar=""
                        caso=0
                    indice-=1
                elif entrada[indice]==" ":
                    if auxiliar.casefold()=="html".casefold():
                        salida.append(Token.Token(TipoToken.TipoToken(4),auxiliar,fila,columna))
                        auxiliar=""
                        caso=1
                    elif auxiliar.casefold()=="head".casefold():
                        salida.append(Token.Token(TipoToken.TipoToken(5),auxiliar,fila,columna))
                        auxiliar=""
                        caso=1
                    elif auxiliar.casefold()=="title".casefold():
                        salida.append(Token.Token(TipoToken.TipoToken(6),auxiliar,fila,columna))
                        auxiliar=""
                        caso=1
                    elif auxiliar.casefold()=="body".casefold():
                        salida.append(Token.Token(TipoToken.TipoToken(7),auxiliar,fila,columna))
                        auxiliar=""
                        caso=1
                    elif auxiliar.casefold()=="h1".casefold() or auxiliar.casefold()=="h2".casefold() or auxiliar.casefold()=="h3".casefold() or auxiliar.casefold()=="h4".casefold() or auxiliar.casefold()=="h5".casefold() or auxiliar.casefold()=="h6".casefold():
                        salida.append(Token.Token(TipoToken.TipoToken(8),auxiliar,fila,columna))
                        auxiliar=""
                        caso=1
                    elif auxiliar.casefold()=="p".casefold():
                        salida.append(Token.Token(TipoToken.TipoToken(9),auxiliar,fila,columna))
                        auxiliar=""
                        caso=1
                    elif auxiliar.casefold()=="br".casefold():
                        salida.append(Token.Token(TipoToken.TipoToken(25),auxiliar,fila,columna))
                        auxiliar=""
                        caso=1
                    elif auxiliar.casefold()=="img".casefold():
                        salida.append(Token.Token(TipoToken.TipoToken(10),auxiliar,fila,columna))
                        auxiliar=""
                        caso=1
                    elif auxiliar.casefold()=="a".casefold():
                        salida.append(Token.Token(TipoToken.TipoToken(11),auxiliar,fila,columna))
                        auxiliar=""
                        caso=1
                    elif auxiliar.casefold()=="ol".casefold():
                        salida.append(Token.Token(TipoToken.TipoToken(12),auxiliar,fila,columna))
                        auxiliar=""
                        caso=1
                    elif auxiliar.casefold()=="ul".casefold():
                        salida.append(Token.Token(TipoToken.TipoToken(13),auxiliar,fila,columna))
                        auxiliar=""
                        caso=1
                    elif auxiliar.casefold()=="style".casefold():
                        salida.append(Token.Token(TipoToken.TipoToken(14),auxiliar,fila,columna))
                        auxiliar=""
                        caso=1
                    elif auxiliar.casefold()=="table".casefold():
                        salida.append(Token.Token(TipoToken.TipoToken(15),auxiliar,fila,columna))
                        auxiliar=""
                        caso=1
                    elif auxiliar.casefold()=="th".casefold():
                        salida.append(Token.Token(TipoToken.TipoToken(16),auxiliar,fila,columna))
                        auxiliar=""
                        caso=1
                    elif auxiliar.casefold()=="tr".casefold():
                        salida.append(Token.Token(TipoToken.TipoToken(17),auxiliar,fila,columna))
                        auxiliar=""
                        caso=1
                    elif auxiliar.casefold()=="td".casefold():
                        salida.append(Token.Token(TipoToken.TipoToken(18),auxiliar,fila,columna))
                        auxiliar=""
                        caso=1
                    elif auxiliar.casefold()=="caption".casefold():
                        salida.append(Token.Token(TipoToken.TipoToken(19),auxiliar,fila,columna))
                        auxiliar=""
                        caso=1
                    elif auxiliar.casefold()=="colgroup".casefold():
                        salida.append(Token.Token(TipoToken.TipoToken(20),auxiliar,fila,columna))
                        auxiliar=""
                        caso=1
                    elif auxiliar.casefold()=="col".casefold():
                        salida.append(Token.Token(TipoToken.TipoToken(21),auxiliar,fila,columna))
                        auxiliar=""
                        caso=1
                    elif auxiliar.casefold()=="thead".casefold():
                        salida.append(Token.Token(TipoToken.TipoToken(22),auxiliar,fila,columna))
                        auxiliar=""
                        caso=1
                    elif auxiliar.casefold()=="tbody".casefold():
                        salida.append(Token.Token(TipoToken.TipoToken(23),auxiliar,fila,columna))
                        auxiliar=""
                        caso=1
                    elif auxiliar.casefold()=="tfoot".casefold():
                        salida.append(Token.Token(TipoToken.TipoToken(24),auxiliar,fila,columna))
                        auxiliar=""
                        caso=1
                    elif auxiliar.casefold()=="div".casefold():
                        salida.append(Token.Token(TipoToken.TipoToken(34),auxiliar,fila,columna))
                        auxiliar=""
                        caso=1
                    elif auxiliar.casefold()=="footer".casefold():
                        salida.append(Token.Token(TipoToken.TipoToken(35),auxiliar,fila,columna))
                        auxiliar=""
                        caso=1
                    elif auxiliar.casefold()=="script".casefold():
                        salida.append(Token.Token(TipoToken.TipoToken(38),auxiliar,fila,columna))
                        auxiliar=""
                        caso=1
                    elif auxiliar.casefold()=="link".casefold():
                        salida.append(Token.Token(TipoToken.TipoToken(40),auxiliar,fila,columna))
                        auxiliar=""
                        caso=1
                    else:
                        errores.append(Error.Error(TipoToken.TipoToken(100),auxiliar,fila,columna))
                        caso=0
                        auxiliar=""
                        columna+=1
                else:
                    auxiliar+=entrada[indice]
                    columna+=1
            elif caso==25:
                if entrada[indice]=="<":
                    salida.append(Token.Token(TipoToken.TipoToken(1),auxiliar,fila,columna))
                    auxiliar=""
                    caso=0
                    indice-=1
                else:
                    if entrada[indice]==" " or entrada[indice]=="\t":columna+=1
                    elif entrada[indice]=="\n" or entrada[indice]=="\r\n" or entrada[indice]=="\r":
                        fila+=1
                        columna=1
                    auxiliar+=entrada[indice]
            elif caso==50:
                if entrada[indice]=="-":
                    auxiliar+=entrada[indice]
                    caso=51
                    columna+=1
                else:
                    errores.append(Error.Error(TipoToken.TipoToken(100),auxiliar,fila,columna))
                    columna+=1
                    auxiliar=""
                    caso=0
            elif caso==51:
                if entrada[indice]=="-":
                    auxiliar+=entrada[indice]
                    columna+=1
                    caso=52
                else:
                    errores.append(Error.Error(TipoToken.TipoToken(100),auxiliar,fila,columna))
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
                else: 
                    auxiliar+=entrada[indice]
                    caso=53
            elif caso==53:
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
                    salida.append(Token.Token(TipoToken.TipoToken(32),auxiliar,filaTemporal,colTemporal))
                    columna+=1
                    auxiliar=""
                    caso=0
                else:
                    columna+=1
                    caso:52
            elif caso==99:
                if entrada[indice]!="\"":
                    if entrada[indice]=="\n":
                        columna=1
                        fila+=1
                    else:columna+=1
                    auxiliar+=entrada[indice]
                else: 
                    auxiliar+="\""
                    salida.append(Token.Token(TipoToken.TipoToken(1),auxiliar,fila,columna))
                    auxiliar=""
                    caso=0
            elif caso==100:
                if entrada[indice]!="\'":
                    if entrada[indice]=="\n":
                        columna=1
                        fila+=1
                    else:columna+=1
                    auxiliar+=entrada[indice]
                else: 
                    auxiliar+="\'"
                    salida.append(Token.Token(TipoToken.TipoToken(1),auxiliar,fila,columna))
                    auxiliar=""
                    caso=0
            indice+=1
        generarReporte("reporteHTML.html",salida,errores)
    else: 
        msgBox=QMessageBox()
        msgBox.setText("El archivo abierto se encuentra vacío.")
        msgBox.exec()


def lexCSS(entradaCSS):
    print("Analizando el archivo CSS...")
    entrada=entradaCSS          
def lexJS(entradaJS):
    print("Analizando el archivo JavaScript...")
    entrada=entradaJS
    if(entrada!=""):
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
            if caso==0:
                if entrada[indice]==" " or entrada[indice]=="=" or entrada[indice]=="." or entrada[indice]=="(" or entrada[indice]==")" or entrada[indice]==";" or entrada[indice]=="{":
                    if str(auxiliar).isalpha():
                        if auxiliar.casefold()=="var".casefold():
                            salida.append(Token.Token(TokenJS.TokenJS(2),auxiliar,fila,columna))
                            auxiliar=""
                            caso=0
                        elif auxiliar.casefold()=="if".casefold():
                            salida.append(Token.Token(TokenJS.TokenJS(12),auxiliar,fila,columna))
                            auxiliar=""
                            caso=0
                        elif auxiliar.casefold()=="else".casefold():
                            salida.append(Token.Token(TokenJS.TokenJS(13),auxiliar,fila,columna))
                            auxiliar=""
                            caso=0
                        elif auxiliar.casefold()=="console".casefold():
                            salida.append(Token.Token(TokenJS.TokenJS(32),auxiliar,fila,columna))
                            auxiliar=""
                            caso=0
                        elif auxiliar.casefold()=="log".casefold():
                            salida.append(Token.Token(TokenJS.TokenJS(33),auxiliar,fila,columna))
                            auxiliar=""
                            caso=0
                        elif auxiliar.casefold()=="while".casefold():
                            salida.append(Token.Token(TokenJS.TokenJS(34),auxiliar,fila,columna))
                            auxiliar=""
                            caso=0
                        elif auxiliar.casefold()=="do".casefold():
                            salida.append(Token.Token(TokenJS.TokenJS(35),auxiliar,fila,columna))
                            auxiliar=""
                            caso=0
                        elif auxiliar.casefold()=="continue".casefold():
                            salida.append(Token.Token(TokenJS.TokenJS(36),auxiliar,fila,columna))
                            auxiliar=""
                            caso=0
                        elif auxiliar.casefold()=="break".casefold():
                            salida.append(Token.Token(TokenJS.TokenJS(37),auxiliar,fila,columna))
                            auxiliar=""
                            caso=0
                        elif auxiliar.casefold()=="return".casefold():
                            salida.append(Token.Token(TokenJS.TokenJS(38),auxiliar,fila,columna))
                            auxiliar=""
                            caso=0
                        elif auxiliar.casefold()=="true".casefold():
                            salida.append(Token.Token(TokenJS.TokenJS(39),auxiliar,fila,columna))
                            auxiliar=""
                            caso=0
                        elif auxiliar.casefold()=="false".casefold():
                            salida.append(Token.Token(TokenJS.TokenJS(40),auxiliar,fila,columna))
                            auxiliar=""
                            caso=0
                        elif auxiliar.casefold()=="function".casefold():
                            salida.append(Token.Token(TokenJS.TokenJS(41),auxiliar,fila,columna))
                            auxiliar=""
                            caso=0
                        elif auxiliar.casefold()=="class".casefold():
                            salida.append(Token.Token(TokenJS.TokenJS(45),auxiliar,fila,columna))
                            auxiliar=""
                            caso=0
                        elif auxiliar.casefold()=="this".casefold():
                            salida.append(Token.Token(TokenJS.TokenJS(46),auxiliar,fila,columna))
                            auxiliar=""
                            caso=0
                        elif auxiliar.casefold()=="math".casefold():
                            salida.append(Token.Token(TokenJS.TokenJS(47),auxiliar,fila,columna))
                            auxiliar=""
                            caso=0
                        elif auxiliar.casefold()=="pow".casefold():
                            salida.append(Token.Token(TokenJS.TokenJS(48),auxiliar,fila,columna))
                            auxiliar=""
                            caso=0
                        else:
                            salida.append(Token.Token(TokenJS.TokenJS(3),auxiliar,fila,columna))
                            auxiliar=""
                            caso=0
                    elif str(auxiliar).isidentifier():
                        salida.append(Token.Token(TokenJS.TokenJS(3),auxiliar,fila,columna))
                        auxiliar=""
                        caso=0
                    elif str(auxiliar).isnumeric():
                        salida.append(Token.Token(TokenJS.TokenJS(9),auxiliar,fila,columna))
                        auxiliar=""
                        caso=0
                    if entrada[indice]=="{":
                        salida.append(Token.Token(TokenJS.TokenJS(20),"{",fila,columna))
                        caso=0
                    elif entrada[indice]=="(":
                        salida.append(Token.Token(TokenJS.TokenJS(10),"(",fila,columna))
                        caso=0
                    elif entrada[indice]==")":
                        salida.append(Token.Token(TokenJS.TokenJS(11),")",fila,columna))
                        caso=0
                    elif entrada[indice]==".":
                        salida.append(Token.Token(TokenJS.TokenJS(21),".",fila,columna))
                        caso=0
                    elif entrada[indice]=="=":
                        salida.append(Token.Token(TokenJS.TokenJS(21),"=",fila,columna))
                        caso=0
                    elif entrada[indice]==";":
                        salida.append(Token.Token(TokenJS.TokenJS(51),";",fila,columna))
                        caso=0
                    else:
                        if auxiliar!=" " and auxiliar!="":
                            errores.append(Error.Error(TokenJS.TokenJS(100),auxiliar,fila,columna))
                            auxiliar=""
                            caso=0
                elif entrada[indice]=="=":
                    caso=1 #CASO PARA DETECTAR UN SEGUNDO =
                    columna+=1
                elif entrada[indice]=="+":
                    caso=2 #CASO PARA DETECTAR SEGUNDO +
                    columna+=1
                elif entrada[indice]=="-":
                    caso=3 #CASO PARA DETECTAR SEGUNDO -
                    columna+=1
                elif entrada[indice]=="*":
                    caso=4 #CASO PARA DETECTAR UN =
                    columna+=1
                elif entrada[indice]=="{":
                    salida.append(Token.Token(TokenJS.TokenJS(20),"{",fila,columna))
                    auxiliar=""
                    caso=0
                elif entrada[indice]=="}":
                    salida.append(Token.Token(TokenJS.TokenJS(50),"}",fila,columna))
                    auxiliar=""
                    caso=0
                elif entrada[indice]=="(":
                    salida.append(Token.Token(TokenJS.TokenJS(10),"(",fila,columna))
                    auxiliar=""
                    caso=0
                elif entrada[indice]==")":
                    salida.append(Token.Token(TokenJS.TokenJS(11),")",fila,columna))
                    auxiliar=""
                    caso=0
                elif entrada[indice]==".":
                    salida.append(Token.Token(TokenJS.TokenJS(21),".",fila,columna))
                    auxiliar=""
                    caso=0
                elif entrada[indice]==";":
                    salida.append(Token.Token(TokenJS.TokenJS(51),";",fila,columna))
                    auxiliar=""
                    caso=0
                elif entrada[indice]=="!":
                    salida.append(Token.Token(TokenJS.TokenJS(31),"!",fila,columna))
                    caso=0
                elif entrada[indice]=="/":
                    auxiliar=str(auxiliar)+str(entrada[indice])
                    caso=6 #CASO PARA DETECTAR COMENTARIO
                elif entrada[indice]=="\"":
                    if auxiliar!=" " and auxiliar!="":
                        errores.append(Error.Error(TokenJS.TokenJS(100),auxiliar,fila,columna))
                        auxiliar=""
                    caso=7 #CASO PARA DETECTAR CADENAS
                    auxiliar=entrada[indice]
                elif entrada[indice]=="\'":
                    if auxiliar!=" " and auxiliar!="":
                        errores.append(Error.Error(TokenJS.TokenJS(100),auxiliar,fila,columna))
                        auxiliar=""
                    caso=8 #CASO PARA DETECTAR CADENAS
                    auxiliar=entrada[indice]
                elif entrada[indice]==">":
                    caso=9 #CASO PARA DETECTAR =
                    columna+=1
                elif entrada[indice]=="<":
                    caso=10 #CASO PARA DETECTAR =
                    columna+=1
                elif entrada[indice]=="|":
                    auxiliar=str(auxiliar)+str(entrada[indice])
                    caso=11 #CASO PARA DETECTAR SEGUNDO |
                    columna+=1
                elif entrada[indice]=="&":
                    auxiliar=str(auxiliar)+str(entrada[indice])
                    caso=12 #CASO PARA DETECTAR SEGUNDO &
                    columna+=12
                elif entrada[indice]==" " or entrada[indice]=="\t":
                    columna+=1
                elif entrada[indice]=="\n" or entrada[indice]=="\r":
                    fila+=1
                    columna=1
                else:
                    auxiliar=str(auxiliar)+str(entrada[indice])
            elif caso==1:
                if entrada[indice]=="=":
                    if entrada[indice+1]=="=":
                        salida.append(Token.Token(TokenJS.TokenJS(27),"===",fila,columna))
                        indice+=1
                        columna+=3
                        auxiliar=""
                        caso=0
                    else:
                        salida.append(Token.Token(TokenJS.TokenJS(18),"==",fila,columna))
                        columna+=2
                        auxiliar=""
                        caso=0
                elif entrada[indice]==">":
                    salida.append(Token.Token(TokenJS.TokenJS(43),"=>",fila,columna))
                    columna+=2
                    auxiliar=""
                    caso=0
                else:
                    salida.append(Token.Token(TokenJS.TokenJS(4),"=",fila,columna))
                    auxiliar=""
                    caso=0
                    indice-=1
                    columna+=1
            elif caso==2:
                if entrada[indice]=="+":
                    salida.append(Token.Token(TokenJS.TokenJS(22),"++",fila,columna))
                    columna+=2
                    auxiliar=""
                    caso=0
                elif entrada[indice]=="=":
                    salida.append(Token.Token(TokenJS.TokenJS(24),"+=",fila,columna))
                    columna+=2
                    auxiliar=""
                    caso=0
                else:
                    salida.append(Token.Token(TokenJS.TokenJS(5),"+",fila,columna))
                    columna+=1
                    auxiliar=""
                    caso=0
                    indice-=1
            elif caso==3:
                if entrada[indice]=="-":
                    salida.append(Token.Token(TokenJS.TokenJS(23),"--",fila,columna))
                    columna+=2
                    auxiliar=""
                    caso=0
                elif entrada[indice]=="=":
                    salida.append(Token.Token(TokenJS.TokenJS(25),"-=",fila,columna))
                    columna+=2
                    auxiliar=""
                    caso=0
                else:
                    salida.append(Token.Token(TokenJS.TokenJS(7),"-",fila,columna))
                    columna+=1
                    auxiliar=""
                    caso=0
                    indice-=1
            elif caso==4:
                if entrada[indice]=="=":
                    salida.append(Token.Token(TokenJS.TokenJS(26),"*=",fila,columna))
                    columna+=2
                    auxiliar=""
                    caso=0
                else:
                    salida.append(Token.Token(TokenJS.TokenJS(6),"*",fila,columna))
                    columna+=1
                    auxiliar=""
                    caso=0
                    indice-=1
            elif caso==6:
                if entrada[indice]=="*":
                    colTemporal=columna-1
                    filaTemporal=fila
                    auxiliar=str(auxiliar)+str(entrada[indice])
                    caso=13
                    columna+=1
                elif entrada[indice]=="/":
                    colTemporal=columna
                    filaTemporal=fila
                    while entrada[indice]!="\n" and indice<len(entrada):
                        auxiliar=str(auxiliar)+str(entrada[indice])
                        indice+=1
                    fila+=1
                    columna=1
                    salida.append(Token.Token(TokenJS.TokenJS(49),auxiliar,filaTemporal,colTemporal))
                else:
                    salida.append(Token.Token(TokenJS.TokenJS(8),"/",fila,columna))
                    auxiliar=""
                    columna+=1
                    caso=0
                    indice-=1
            elif caso==13:#/*
                if entrada[indice]!="*":
                    auxiliar=str(auxiliar)+str(entrada[indice])
                    if entrada[indice]=="\n":
                        fila+=1
                        columna=1
                    else: columna+=1
                else:
                    auxiliar=str(auxiliar)+str(entrada[indice])
                    columna+=1
                    caso=14
            elif caso==14:
                if entrada[indice]=="*":
                    if entrada[indice+1]=="/":
                        auxiliar=str(auxiliar)+str(entrada[indice+1])
                        salida.append(Token.Token(TokenJS.TokenJS(1),auxiliar,filaTemporal,colTemporal))
                        auxiliar=""
                        caso=0
                        columna+=1
                    else:
                        auxiliar=str(auxiliar)+str(entrada[indice+1])
                        if entrada[indice]=="\n":
                            fila+=1
                            columna=1
                        else:
                            columna+=1
                        caso=13
                elif entrada[indice]=="/":
                        auxiliar=str(auxiliar)+str(entrada[indice])
                        salida.append(Token.Token(TokenJS.TokenJS(1),auxiliar,filaTemporal,colTemporal))
                        auxiliar=""
                        caso=0
                        columna+=1
                else:
                    auxiliar=str(auxiliar)+str(entrada[indice+1])
                    if entrada[indice]=="\n":
                        fila+=1
                        columna=1
                    else:
                        columna+=1
                    caso=13
            elif caso==7:
                colTemporal=columna
                filaTemporal=fila
                while entrada[indice]!="\"":
                    auxiliar=str(auxiliar)+str(entrada[indice])
                    if entrada[indice]=="\n":
                        fila+=1
                        columna=1
                    else: columna+=1
                    indice+=1
                auxiliar+="\""
                salida.append(Token.Token(TokenJS.TokenJS(19),auxiliar,filaTemporal,colTemporal))
                auxiliar=""
                caso=0
                columna+=1
            elif caso==8:
                colTemporal=columna
                filaTemporal=fila
                while entrada[indice]!="\'":
                    auxiliar=str(auxiliar)+str(entrada[indice])
                    if entrada[indice]=="\n":
                        fila+=1
                        columna=1
                    else: columna+=1
                    indice+=1
                auxiliar+="\'"
                salida.append(Token.Token(TokenJS.TokenJS(19),auxiliar,filaTemporal,colTemporal))
                auxiliar=""
                caso=0
                columna+=1
            elif caso==9:
                if entrada[indice]=="=":
                    salida.append(Token.Token(TokenJS.TokenJS(16),">=",fila,columna-1))
                    columna+=1
                    auxiliar=""
                    caso=0
                else: 
                    salida.append(Token.Token(TokenJS.TokenJS(14),">",fila,columna-1))
                    auxiliar=""
                    indice-=1
                    caso=0
            elif caso==10:
                if entrada[indice]=="=":
                    salida.append(Token.Token(TokenJS.TokenJS(17),"<=",fila,columna-1))
                    columna+=1
                    auxiliar=""
                    caso=0
                else: 
                    salida.append(Token.Token(TokenJS.TokenJS(15),"<",fila,columna-1))
                    auxiliar=""
                    indice-=1
                    caso=0
            elif caso==11:
                if entrada[indice]=="|":
                    salida.append(Token.Token(TokenJS.TokenJS(29),"||",fila,columna-1))
                    columna+=1
                    auxiliar=""
                    caso=0
                else:
                    if auxiliar!=" " and auxiliar!="": 
                        errores.append(Error.Error(TokenJS.TokenJS(100),auxiliar,fila,columna-1))
                        auxiliar=""
                        indice-=1
                        caso=0
            elif caso==12:
                if entrada[indice]=="&":
                    salida.append(Token.Token(TokenJS.TokenJS(28),"&&",fila,columna-1))
                    columna+=1
                    auxiliar=""
                    caso=0
                else: 
                    if auxiliar!=" " and auxiliar!="":
                        errores.append(Error.Error(TokenJS.TokenJS(100),auxiliar,fila,columna-1))
                        auxiliar=""
                        indice-=1
                        caso=0
            # ... caso=8
            indice+=1
        print("Análisis finalizado")
        generarReporte("reporteJS.html",salida,errores)


