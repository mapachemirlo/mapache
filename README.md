#  mapache

Mapache es un script muy simple para extraer subdominios, filtrar los http/https, información de las cabeceras, screen de los sitios y archivos JavaScripts, utilizando algunas de las herramientas que más me gustan en la actualidad.
Filtrará y generará una carpeta con el nombre de dominio y su respectiva información recompilada.

# Requisitos
- Python 3.*

<a href="https://github.com/tomnomnom/assetfinder">- Assetfinder</a>

<a href="https://github.com/projectdiscovery/subfinder">- Subfinder</a>

<a href="https://github.com/tomnomnom/httprobe">- Httprobe</a>

<a href="https://github.com/michenriksen/aquatone">- Aquatone</a>

<a href="https://github.com/GerbenJavado/LinkFinder">- LinkFinder</a>

*Todos los ejecutables deberán ser agregados al $PATH, o copiados a `/usr/bin/` (Linux).

# Instalación
Clone el repositorio a su directorio local:

`git clone https://github.com/mapachemirlo/mapache.git`

Instale las dependencias:

Ingrese al directorio `mapache` y ejecute:

`pip install -r requirements.txt`

Puede agregar el archivo `mapache.py` al $PATH para más comodidad.

# Uso
Muy fácil, ejecute:

`python mapache.py -d dominio`

En el directorio de salida que usted eliga se encontrará toda la información.

# Nota
La extracción de archivos .js está en modo prueba.


