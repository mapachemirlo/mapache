#!/usr/bin/env python
#_*_coding: utf8 _*_
# Mapache - Version 1.0
# +++ Mapache es un pequeño script para ordenar un recon hecho con 2 excelentes herramientas +++
# Author: Claudio Herrera
# Ejecutar con Python 3.*

import subprocess
import requests
import argparse
from os import path
from pyfiglet import Figlet
import os
import sys

sis_op = sys.platform
sis_op = sis_op[:3]
if sis_op == 'lin':
    os.system('clear')
elif sis_op == 'win':
    os.system('cls')
else:
    pass

print('')
custom_fig = Figlet(font='slant')
print(custom_fig.renderText(' Mapache'))
print("         *** Recon simple y ordenado ***")
print(' Autor: Claudio Herrera - claudioherrera@protonmail.ch')
print('------------------------------------------------------')
print(' Ejecutar con Python 3.*\n')


parser = argparse.ArgumentParser(description="Indexador de recon")
parser.add_argument('-d', '--dominio', help='Dominio')
parser = parser.parse_args()
#print('Dominio a buscar => ' , parser)
print('Crear directorio de salida, ejemplo: /home/user/recon\n')
path_folder = input("Ingrese PATH: ")
print('')


def main():
    if parser.dominio:
        if path.exists(path_folder):
            parsito = (parser.dominio)
            os.system('mkdir {}/{}'.format(path_folder, parsito))
            dominio = ('https://www.' + parser.dominio)       
            print("\nConectado a: {}\n".format(dominio))
            
            try:
                path_arch_all = '{}/{}/all.txt'.format(path_folder, parsito)
                archivo = open(path_arch_all, 'r')
                print("Archivo inicial ya existe, se sobreescribe..\n")
                
            except:
                archivo = open(path_arch_all, 'a+')
                print("Archivo inicial creado con éxito..\n")
            
            try:
                # Usar CD para entrar en la variable path_folder
                rc1 = '{}/{}/rc1.txt'.format(path_folder, parsito)
                rc2 = '{}/{}/rc2.txt'.format(path_folder, parsito)
                
                
                # Solo para probar la conectividad
                #url = requests.get(url=dominio)
                #cabeceras = dict(url.headers)
                #for m in cabeceras.keys():
                #    print("{}:{}".format(m,cabeceras[m]))
                #print("\ndominio es: \n" + dominio)
                
                #**********************************************  TOOLS **************************************************
                #ASSETFINDER
                banner_asset = Figlet(font='slant')
                print(banner_asset.renderText('Assetfinder'))
                print('      github.com/tomnomnom/assetfider')
                os.system('assetfinder -subs-only {} > {}'.format(parsito, rc1))               
                
                #SUBFINDER
                os.system('subfinder -d {} > {}'.format(parsito, rc2))
            
                #***************************************** Abrir Archivos-recon ****************************************
                
                arch1 = open(rc1, 'r')
                arch2 = open(rc2, 'r')
                
                rc1 = arch1.readlines()
                rc2 = arch2.readlines()
                
                archivo.writelines(rc1)
                archivo.writelines(rc2)
                
                arch1.close()
                arch2.close()
                archivo.close()

                #*************************************** Pasar en limpio ***********************************************
                
                path_salida = '{}/{}/recon.txt'.format(path_folder, parsito, parsito)

                palabras = open(path_arch_all, 'r')
                archivo2 = open(path_salida, 'a+')

                lis = list(palabras)
                vamo = list(set(lis))
                vamo.sort()
                for i in vamo:
                    
                    item = (i.rstrip('\n'))
                    print(item)
                    archivo2.write(item + '\n')

                palabras.close()
                archivo2.close()
                os.system('rm -r {}/{}/rc*'.format(path_folder, parsito))
                os.system('rm -r {}/{}/all.txt'.format(path_folder, parsito))
                
            except:
                print("*** No hay conectividad ***\n")
        else:
            print("!!!Error en la ruta al crear carpeta!!!")
             
    else:
        print('')
        print("+++++ NO INGRESÓ EL DOMINIO +++++")
        print('')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Saliendo...")
        
