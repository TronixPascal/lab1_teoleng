# -*- coding: utf-8 -*-
import re
import sys
from programa4 import programa4
from programa2 import programa2
from programa5 import programa5

def programa6(RutaPdf,RutaXML):
    text = ""
    '''
    SU CÓDIGO
    1. buscamos coinicidencias con programa3
        2.1 if (coinciden)
            2.1.1 obtenemos fecha y debito bancario de RutaPDF con programa2
            2.1.2 buscamos en xml y eliminamos
        2.2 else: nada
    3. return text (en realidad se modifica el )
    '''
    if programa5(RutaPdf,RutaXML):
        fecha,debito = programa2(RutaPdf)
        texto_xml = programa4(RutaXML)
        text = texto_xml

        patron = rf'^\s*<BanTeng:Movimiento\b[^>]*\bImporte="{re.escape(debito)}"[^>]*\bFecha="{re.escape(fecha)}"[^>]*/>\s*$'
        print(re.findall(patron,texto_xml, flags=re.MULTILINE))

        total_movimientos_text = re.findall(r'<BanTeng:TotalMovimientos>\d+</BanTeng:TotalMovimientos>',texto_xml)
        print(total_movimientos_text)
        total_movimientos = re.search(r'(\d+)',total_movimientos_text[0])
        if total_movimientos != None: #se supone que nunca va a ser none en nuestro caso pero el compilador me tira error si no hago el checkeo pq el .group() no esta definido para None
            nuevo_total_movimientos = int(total_movimientos.group(1)) - len(re.findall(patron,texto_xml, flags=re.MULTILINE))
            print(nuevo_total_movimientos)
            text = re.sub(r'<BanTeng:TotalMovimientos>\d+</BanTeng:TotalMovimientos>',rf'<BanTeng:TotalMovimientos>{nuevo_total_movimientos}</BanTeng:TotalMovimientos>',text)

        text = re.sub(patron + r'(?:\r?\n)?',"",text, flags=re.MULTILINE)
    
    return text
 

if __name__ == '__main__':
    entrada_pdf = sys.argv[1]  # archivo entrada (param)
    entrada_xml = sys.argv[2]  # archivo entrada (param)
    salida = sys.argv[3]   # archivo salida (param)    
 
    ret = programa6(entrada_pdf,entrada_xml)      # ejecutar 
    
    f = open(salida, 'w', encoding='utf-8')  # abrir archivo salida
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida
