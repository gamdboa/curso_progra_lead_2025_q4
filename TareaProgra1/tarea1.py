import modulos as m

def main():
    archivo=m.extractor_nombre()
    filas, headers=m.lector(archivo)
    formato=m.formatos()
    columnas=m.headers(headers)
    
    nombre=archivo.rsplit('.',1)[0]
    if formato=='json':
        m.a_json(filas,columnas,nombre+'.json')
    elif formato=='xml':
        # print('hola, aqui va xml')
        m.a_xml(filas,columnas,nombre+'.xml',nombre)
    else:
        print('hola, aqui va trama')

if __name__=='__main__':
    main()