#  mapache

Mapache es un script muy simple para extraer subdominios, filtrar los http/https, información de las cabeceras, screen de los sitios y archivos JavaScripts, utilizando algunas de las herramientas que más me gustan en la actualidad.
Filtrará y generará una carpeta con el nombre de dominio y su respectiva información recompilada.

# Requisitos
Python 3.*

-Assetfinder

-Subfinder

-Httprobe

-Aquatone

-LinkFinder

*Todos los ejecutables deberán ser agregados al $PATH, o copiados a `/usr/bin/` (Linux).

# Instalación
Clone el repositorio a su directorio local:

`git clone https://github.com/mapachemirlo/mapache.git`

Instale las dependencias:

`pip install -r requirements.txt`

# Uso
Ejecute:

`python mapache.py -d dominio`

En el directorio de salida que usted eliga se encontrará el archivo de salida recon.txt

# Tools
https://github.com/projectdiscovery/subfinder 

https://github.com/tomnomnom/assetfinder


