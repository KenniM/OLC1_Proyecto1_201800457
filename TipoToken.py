from enum import Enum
class TipoToken(Enum):
    CADENA_DE_TEXTO=1
    ETQ_APERTURA=2
    ETQ_CIERRE=3
    RESERVADA_HTML=4
    RESERVADA_HEAD=5
    RESERVADA_TITLE=6
    RESERVADA_BODY=7
    RESERVADA_TITULO=8
    RESERVADA_P=9
    RESERVADA_IMG=10
    RESERVADA_A=11
    RESERVADA_OL=12
    RESERVADA_UL=13
    RESERVADA_STYLE=14
    RESERVADA_TABLE=15
    RESERVADA_TH=16
    RESERVADA_TR=17
    RESERVADA_TD=18
    RESERVADA_CAPTION=19
    RESERVADA_COLGROUP=20
    RESERVADA_COL=21
    RESERVADA_THEAD=22
    RESERVADA_TBODY=23
    RESERVADA_TFOOT=24
    RESERVADA_BR=25
    SIMBOLO_SLASH=26
    SIGNO_IGUAL=27
    ATRIBUTO_SRC=28
    ATRIBUTO_HREF=29
    SIGNO_EXCL_CIERRE=30
    SIGNO_GUION=31
    COMENTARIO=32
    ATRIBUTO_BORDER=33
    RESERVADA_DIV=34
    RESERVADA_FOOTER=35
    ATRIBUTO_CLASS=36
    ATRIBUTO_ID=37
    RESERVADA_SCRIPT=38
    ATRIBUTO_TYPE=39
    RESERVADA_LINK=40
    ATRIBUTO_SCOPE=41
    ATRIBUTO_REL=42
    DESCONOCIDO=100
