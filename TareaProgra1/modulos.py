import json, csv, sys

# lector de argumentos en terminal
def extractor_nombre():
    if len(sys.argv) < 2:
        print('Es necesario 2 argumentos: tarea1.py y <archivo>.csv')
        sys.exit(1)
    #el argv[1] es el segundo argumento, en este caso, el nombre del csv
    return sys.argv[1]
        
# lector de CSV y headers
def lector(archivo: str):
    with open(archivo,newline='',encoding='utf-8') as f:
        lector=csv.DictReader(f)
        filas=list(lector)
    return filas, lector.fieldnames

def formatos():
    pasa=True
    while pasa:
        formato=input('\nSeleccione el formato de salida (json/xml/hex): ').strip().lower()
        if formato not in ['json','xml','hex']:
            print('Formato invalido, intente de nuevo')
        else:
            pasa=False
            return formato

# selector de headers
def headers(headers: str):
    print('Columnas disponibles: ')
    for i, col in enumerate(headers,start=1):
        print(f'{i}: {col}')
    select=input('Por favor seleccione las columnas, separadas por coma (,) o presione Enter para todas las columnas:')
    if not select.strip():
        return headers
    seleccionadas= [headers[int(i.strip())-1] for i in select.split(',')]
    return seleccionadas

# conversor a JSON
def a_json(filas,cols: str,nombre: str):
    datos=[{col:fila[col] for col in cols} for  fila in filas]
    with open(nombre,'w',encoding='utf-8') as f:
        json.dump({'data':datos},f,indent=2)
    print(f'\nJSON guardado como {nombre}\n')

# conversor a XML
def a_xml(filas,cols: str,nombre: str,original: str):
    with open(nombre,'w',encoding='utf-8') as f:
        f.write(f'<{original}>\n<data>\n')
        for fila in filas:
            f.write('  <row>\n')
            for col in cols:
                valor=str(fila[col])
                col=col.replace(' ','_')
                f.write(f'    <{col}>{valor}</{col}>\n')
            f.write('  </row>\n')
        f.write(f'</data>\n</{original}>\n')
    print(f'\nXML guardado como {nombre}\n')
    
def a_trama(filas,cols: str,nombre: str):
    STX=0x02
    ETX=0x03
    sep='|'
    
    with open(nombre,'w',encoding='ascii') as f:
        for fila in filas:
            descompuesto=sep.join(str(fila[col]) for col in cols)
            bytes=descompuesto.encode('ascii',errors='replace')
            tamanno=len(bytes)
            checksum=sum(bytes)%256
            hex=' '.join(f'{b:02X}' for b in bytes)
            frame=f'{STX:02X} {tamanno:02X} {hex} {checksum:02X} {ETX:02X}'
            f.write(frame+'\n')
    print(f'\nSeparador: {sep}\nCaracter Inicial:{str(STX)}\nCaracter Final:{str(ETX)}')
    print(f'\nTrama de bytes guardado como {nombre}\n')
