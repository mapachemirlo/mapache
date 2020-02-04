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
from progress.bar import Bar
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
                print('            github.com/tomnomnom/assetfinder')
                print('------------------------------------------------------')
                bar = Bar(('Extrayendo de ... {}'.format(parsito)), max=10)
                for e in range(10): 
                    os.system('assetfinder -subs-only {} > {}'.format(parsito, rc1))
                    bar.next()
                bar.finish()
                print('======================================================')               
                
                #SUBFINDER
                os.system('subfinder -d {} > {}'.format(parsito, rc2))
                print('======================================================')
            
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
                path_vivos = '{}/{}/vivos.txt'.format(path_folder, parsito, parsito)
                path_js = '{}/{}/infojs.txt'.format(path_folder, parsito, parsito)

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

                #************************************** Filtrados de http/https y armado de .html *************************

                #HTTPROBE
                print('======================================================')
                banner_httpr = Figlet(font='slant')
                print(banner_httpr.renderText('Httprobe'))
                print('            github.com/tomnomnom/httprobe')
                print('------------------------------------------------------')
                arch_vivos = open(path_vivos, 'a+')
                bar = Bar(('Extrayendo de ... {}'.format(parsito)), max=10)
                for e in range(10):
                    os.system('cat {} | httprobe > {}'.format(path_salida, path_vivos))
                    bar.next()
                bar.finish()
                arch_vivos.close()

                #AQUATONE
                print('======================================================')
                banner_aqua = Figlet(font='slant')
                print(banner_aqua.renderText('Aquatone'))
                os.system('cat {} | aquatone -ports large -out {}/{}'.format(path_salida, path_folder, parsito))
                print('======================================================')

                #LINKFINDER (Saca todo sucio, tengo que limpiarlo)
                banner_link = Figlet(font='slant')
                print(banner_link.renderText('LinkFinder'))
                print('            github.com/GerbenJavado/LinkFinder')
                print('------------------------------------------------------')
                arch_link = open(path_js, 'a+')
                bar = Bar(('Extrayendo de ... {}'.format(parsito)), max=5)
                for e in range(5):
                    os.system('linkfinder.py -i {} -d > {}'.format(dominio, path_js))
                    bar.next()
                bar.finish()
                arch_link.close()
                print('------------------------------------------------------')
                print("\nFin del recon\n")
                
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
        
