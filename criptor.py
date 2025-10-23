import os 
import pyAesCrypt

def criptor(_mode, _file):
    password = input('Enter password: ')
    buffer_size = 512 * 1024
    _ext = _file.split('.')[0]
    
    if int(_mode) == 0:
        pyAesCrypt.encryptFile(_file, _ext.lower() + '.enc', password, buffer_size)
    elif int(_mode) == 1:
        _type = input('Enter type: ')
        pyAesCrypt.decryptFile(_file, _ext.lower() + '.' + _type, password, buffer_size)
        
    os.remove(_file)
    

print('0 - Criptor\n1 - Decriptor')
mode = input('Select mode: ')
filename = input('Enter file: ')

criptor(mode, filename)