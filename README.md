# Reconocimiento de Imágenes de Naves Espaciales con Python y TensorFlow

Este proyecto realiza el reconocimiento de imágenes de naves espaciales utilizando la red neuronal MobileNetV2 de TensorFlow. El programa procesa imágenes, las analiza y guarda los resultados junto con la fecha y hora del reconocimiento en un archivo de texto.

## Requisitos

Antes de ejecutar el programa, asegúrate de tener instalados los siguientes paquetes de Python:

- tensorflow
- numpy
- opencv-python
- matplotlib
#
## Puedes instalarlos usando `pip`:


<code>pip install tensorflow numpy opencv-python matplotlib</code>

O

1. clona el repositorio:

<code>git clone https://github.com/0xfabrica/rocket-script
cd rocket-script</code>

2. Ejecuta el programa:

<code>python reconocimiento_naves.py</code>

3.Introduce la ruta de la imagen que deseas analizar cuando el programa lo solicite.
El programa procesará la imagen, realizará el reconocimiento y mostrará la imagen junto con las predicciones. Además, guardará los resultados en un archivo de texto resultado_red.txt, añadiendo la fecha y hora del reconocimiento.
#

## Funcionalidades
Carga y preprocesamiento de imágenes: El programa carga imágenes desde una ruta especificada, convierte el color de BGR a RGB, redimensiona la imagen a 224x224 píxeles y normaliza los valores de los píxeles.
Visualización de imágenes: Muestra la imagen procesada utilizando Matplotlib.
Reconocimiento de imágenes: Utiliza la red neuronal MobileNetV2 preentrenada con los pesos de ImageNet para predecir el contenido de la imagen.
Guardado de resultados: Escribe las predicciones junto con la fecha y hora del reconocimiento en el archivo resultado_red.txt, añadiendo nuevas entradas al final del archivo para preservar los resultados anteriores.
#
## Ejemplo de resultados
Después de ejecutar el programa y analizar una imagen, el archivo resultado_red.txt podría contener algo como esto:

<code>Fecha y hora del reconocimiento: 2024-07-12 14:35:22
espacio_nave: 97.53%
cohete: 85.21%
satélite: 70.34%</code>


<code>Fecha y hora del reconocimiento: 2024-07-13 09:47:10
espacio_nave: 96.45%
cohete: 88.11%
satélite: 72.25%</code>
#
## Contribuciones
Las contribuciones son bienvenidas. Si deseas mejorar este proyecto, por favor, sigue estos pasos:

1. Haz un fork del repositorio
2. Crea una nueva rama <b>(git checkout -b mejora-nueva-funcionalidad).</b>
3. Realiza los cambios necesarios y haz commit <b>(git commit -am 'Añadir nueva funcionalidad').</b>
4. Sube los cambios a tu rama <b>(git push origin mejora-nueva-funcionalidad).</b>
5. Crea un <b>Pull Request.</b>
