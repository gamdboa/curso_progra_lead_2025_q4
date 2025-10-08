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
        formato=input('Seleccione el formato de salida (json/xml/trama): ').strip().lower()
        if formato not in ['json','xml','trama']:
            print('Formato invalido, intente de nuevo')
        else:
            pasa=False
            return formato

# selector de headers
def headers(headers: str):
    print('Columnas disponibles:')
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
        json.dump({'datos':datos},f,indent=2)
    print(f'JSON guardado como {nombre}')

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
    print(f'XML guardado como {nombre}')
    
def a_trama(filas,cols: str):
    STX='02'
    EXT='03'
    sep='|'
