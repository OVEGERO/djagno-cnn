from keras.models import load_model
import numpy as np
from PIL import Image
import requests
import os

class modeloCNN():

    def cargarCNN(self, nombreArchivo):
        ruta = '/app/resources/'
        nombre_archivo = nombreArchivo + '.h5'
        ruta_archivo = os.path.join(ruta, nombre_archivo)
        modelo = load_model(ruta_archivo)
        print("Red Neuronal Cargada desde Archivo") 
        return modelo
    
    def obtenerResultadosyCertezas(self, lista):
        marcas=[]
        certezas=[]
        nuevomax=1
        nuevomin=0
        marca=-1
        certeza=-1
        for i in range(len(lista)):
            prediccion=lista[i]
            if (prediccion < 0.5):
                marca = 'Tumor Benigno'
                maxa=0.5
                mina=0
                certeza=1-((prediccion-mina)/(maxa-mina)*(nuevomax-nuevomin)+nuevomin)
                certeza=str(int((certeza)*100))+'%'
            elif (prediccion >= 0.5):
                marca = 'Tumor Maligno'
                maxa=1
                mina=0.5
                certeza=(prediccion-mina)/(maxa-mina)*(nuevomax-nuevomin)+nuevomin
                certeza=str(int((certeza)*100))+'%'
            marcas.append(marca)
            certezas.append(certeza)
        return prediccion, marcas, certezas
    
    def predecir_tumor(self, url_imagen=""):
        # Cargar y preprocesar la imagen
        modelo = self.cargarCNN(self, 'modelo_base')
        response = requests.get(url_imagen, stream=True)
        response.raise_for_status()
        imagen = Image.open(response.raw)

        # Convertir la imagen en color a escala de grises
        imagen_gris = imagen.convert('L')
        imagen_gris = imagen_gris.resize((128, 128))
        imagen_gris = np.array(imagen_gris) / 255.0
        # Verificar el tamaño de la imagen
        if imagen_gris.shape != (128, 128):
            raise ValueError('La imagen no tiene el tamaño esperado de 128x128.')

        imagen_gris = np.expand_dims(imagen_gris, axis=0).reshape(1, 128, 128, 1)

        # Realizar la predicción
        y_pred = modelo.predict(imagen_gris)
        predicciones, marcas, certezas = self.obtenerResultadosyCertezas(self, y_pred[0])
        resultado = f'La imagen arroja como resultado un porcentaje de {predicciones:.4f}% lo que significa que es un {marcas[0]} con una certeza del {certezas[0]}'
        resultado = f'{marcas[0]}. Probabilidad: {predicciones:.2f}%. Certeza: {certezas[0]}'
        print(resultado)
        return resultado







