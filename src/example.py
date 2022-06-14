
def suma(x, y):
    return x + y

def escribir(fpath, data_in):
    '''
    Functión que escribe en un archivo
    Args:
        fpath: path absoluto del archivo
        data_in: información a escribir
    '''
    
    with open(fpath, 'w') as file_in:
        file_in.write(data_in)
        

class calculadora():
    '''
    CLASE CALCULADORA
    '''
    def sumar(x, y):
        '''
        Función que toma 2 argumentos y devuelve su suma
        Args:
            x (int/float): Primer valor a sumar
            y (int/float): Segundo valor a sumar
        return: suma(x, y)
        '''
        return suma(x, y)