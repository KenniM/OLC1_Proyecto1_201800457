from PyQt5.QtWidgets import QMessageBox
import Token
import Error
import TipoToken
import os
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
                contenidoHTML+="<td class='filas'>"+tokens.val+"</td>\n"
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
                contenidoHTML+="<td class='filas'>" + error.val + "</td>\n"
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
        reporte=open("reporteHTML.html","w")
        reporte.write(contenidoHTML)
        reporte.close()
        os.startfile("reporteHTML.html")
    else: 
        msgBox=QMessageBox()
        msgBox.setText("El archivo abierto se encuentra vacío.")
        msgBox.exec()


def lexCSS(entradaCSS):
    print("Analizando el archivo CSS...")
def lexJS(entradaJS):
    print("Analizando el archivo JavaScript...")