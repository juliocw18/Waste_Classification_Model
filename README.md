<div id="header" align="center">
  <img src="GitHub_Banner_TFM_Modelo_de_Clasificación_de_Desechos.png"/>
</div>

# Modelo de Clasificación de Desechos ♻

Hola 👋, en este repositorio les presento mi trabajo final de máster (TFM). Se trata de un modelo de Red Neuronal Convolucional (CNN) para clasificar imágenes de desechos en las categorías "orgánico" y "reciclable".

Puedes ingresar en las carpetas respectivas para visualizar o descargar los códigos tanto del modelo como de la aplicación web.

## Dataset
El dataset que utilicé para desarrollar el modelo se denomina "Waste Classification data". Este dataset consta de más de 25mil imágenes de diversos objetos que han sido etiquetados por su autor, y se encuentra publicado bajo la licencia Creative Commons Attribution Share-Alike 4.0 ("CC BY-SA 4.0") ([Waste Classification data](https://www.kaggle.com/datasets/techsash/waste-classification-data)).

## Modelización
Para crear un modelo capaz de procesar imágenes, recurrí a las redes neuronales convolucionales. Con base en este tipo de arquitectura de red, desarrollé un primer modelo de referencia, llamado Modelo Base. Y luego de experimentar con distintos parámetros, finalmente obtuve el “Modelo Optimizado”. Éste modelo consta de 6.8 millones de parámetros y tiene principalmente las siguientes características:
- En la capa de entrada, utilicé la técnica de Data Augmentation para incrementar la diversidad de los datos de entrenamiento.
- Cuenta con 4 capas ocultas de convolución 2D de 32, 64, 128 y 256 filtros, cada una acompañada de una función de activación Relu y una capa Max Pooling.
- En la capa Fully Connected, cuenta con 2 capas densas de 128 y 64 neuronas, cada una con su función de activación Relu y regularización dropout del 20% de las neuronas.
- Compilé el modelo utilizando:
  - Adam como algoritmo de optimización
  - Binary Cross-Entropy como función de pérdida para medir las desviaciones del modelo
  - Accuracy como métrica para evaluar el rendimiento del modelo

Luego de 30 épocas de entrenamiento con un batch size de 32, al generalizar sobre el conjunto de test, el Modelo Optimizado obtuvo en promedio 0.25 en error/loss (Binary Cross-entropy), 90.73% en Accuracy y 90% AUC.

<div align="center">
  <img src="Model Code\History.png", , height="250"/>
</div>

Adicionalmente, experimenté realizando transfer learning con el modelo preentrenado llamado "Xception", para ver la potencia 🦾 que tienen estos modelos y qué tanto podrían inferir en el tema.

Debajo detallo los resultados de los 3 modelos obtenidos con el conjunto de test, las matrices de confusión y las curvas AUC.

| Model Name | Test Loss | Test Accuracy |
| --- | --- | --- |
| 1. Modelo_Base | 1.287241 | 0.845205 |
| 2. Modelo_Optimizado | 0.251224  | 0.907282 |
| 3. Modelo_TransferLearning | 0.230865 | 0.907680 |


<div align="center">
  <img src="Model Code\CM.png", height="200"/>
  <img src="Model Code\AUC.png", height="200"/>
</div>

## Productivización
Para que el Modelo Optimizado, realmente cumpla su objetivo, desarrollé una aplicación utilizando el framework llamado Streamlit y la desplegué en Google Cloud Platform.

<div align="center">
  <img src="App Code\App_Screenshot.png", height="350"/>
</div>

Esta aplicación le brinda al usuario la opción de cargar la imagen de un desecho, a partir de una imagen en el dispositivo o tomando una fotografía. La aplicación predice en tiempo real si el desecho pertenece a la categoría “orgánico” o “reciclable”.

Esta aplicación puede ser accedida a través de cualquier dispositivo, ya sea una computadora, un teléfono o una tablet, mediante este enlace: [Clasificador de Desechos](https://clasificadordedesechos-6ejwhynecq-uc.a.run.app/)