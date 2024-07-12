import tensorflow as tf
import numpy as np
import cv2
import matplotlib.pyplot as plt
from datetime import datetime  # Importar módulo datetime

def cargar_y_preprocesar_imagen(ruta):
    imagen = cv2.imread(ruta)
    imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
    imagen = cv2.resize(imagen, (224, 224))  # Tamaño que espera el modelo
    imagen = np.array(imagen, dtype=np.float32) / 255.0  # Normalizar
    imagen = np.expand_dims(imagen, axis=0)  # Añadir dimensión de batch
    return imagen

def mostrar_imagen(imagen):
    plt.imshow(imagen[0])
    plt.axis('off')
    plt.show()

def main():
    modelo = tf.keras.applications.MobileNetV2(weights='imagenet')

    ruta_imagen = input("Introduce la ruta de la imagen:")
    imagen = cargar_y_preprocesar_imagen(ruta_imagen)
    mostrar_imagen(imagen)

    predicciones = modelo.predict(imagen)
    resultados = tf.keras.applications.mobilenet_v2.decode_predictions(predicciones)

    # Obtener la fecha y hora actuales
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Abrir archivo para escribir los resultados
    with open("resultado_red.txt", "a") as archivo:
        archivo.write(f"Fecha y hora del reconocimiento: {fecha_actual}\n\n")
        for (imagenet_id, etiqueta, puntaje) in resultados[0]:
            resultado = f"{etiqueta}: {puntaje * 100:.2f}%\n"
            archivo.write(resultado)
            print(resultado)
        archivo.write("\n")  # Añadir una línea en blanco para separar entradas


    print("Resultados guardados en resultado_red.txt")

if __name__ == "__main__":
    main()
