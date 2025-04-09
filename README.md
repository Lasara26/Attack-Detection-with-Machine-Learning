# 🛡️ Attack Detection with Machine Learning
Proyecto de detección de tráfico malicioso en redes mediante algoritmos de Machine Learning, específicamente Random Forest.
Este proyecto incluye un menú interactivo, visualización de la matriz de confusión, generación de reportes automáticos en JSON y la capacidad de cargar diferentes datasets.

## 🚀 Características
- ✅ Menú interactivo para facilidad de uso
- ✅ Entrenamiento automático si no existe modelo previo
- ✅ Guardado y carga del modelo entrenado
- ✅ Reporte automático de métricas en JSON
- ✅ Visualización gráfica de la matriz de confusión
- ✅ Opción para cargar un dataset personalizado
- ✅ Proyecto limpio y listo para escalar

## 📁 Estructura del proyecto

- ├── main.py                 # Script principal con menú interactivo
- ├── model.pkl               # Modelo RandomForest entrenado (se genera automáticamente)
- ├── report.json             # Reporte de métricas en JSON
- ├── data/                   # Carpeta para datasets locales (agregada al .gitignore)
- │   └── tu_dataset.csv
- ├── requirements.txt        # Dependencias del proyecto
- └── README.md               # Este archivo


## 🧩 Requisitos

- Python 3.8+
- Librerías necesarias (instalar con pip):
  pip install -r requirements.txt

## ⚙️ Uso

1. Clonar el repositorio:
 - git clone https://github.com/FrancoGarciaC9701/Attack-Detection-with-Machine-Learning.git
 - cd Attack-Detection-with-Machine-Learning
  
2. Ejecutar el proyecto:
  python main.py

3. Descarga el archivo de "http://cicresearch.ca/CICDataset/CIC-IDS-2017/Dataset/CIC-IDS-2017/CSVs/" el que dice "MachineLearningCSV.zip", lo descomprimís y tenés los datos para ensayar
   Podés generar un archivo conjunto o escanearlo de a uno (No subí los archivos porque pesaban más de lo permitido)

4. Seguí las instrucciones del menú para entrenar el modelo, cargar datasets y generar reportes.

## 📊 Resultados
El proyecto genera un report.json con las métricas de precisión, recall, f1-score y soporte.

Visualiza la matriz de confusión para entender el rendimiento del modelo.

## 🤖 Algoritmo utilizado
Se utiliza Random Forest, un poderoso algoritmo de ensamble basado en árboles de decisión, ideal para problemas de clasificación de tráfico de red.

## 📝 Notas
Por seguridad y para mantener el repositorio liviano, los datasets están ignorados en el control de versiones.

Podés añadir tu propio dataset colocándolo en la carpeta data/ y seleccionándolo desde el menú interactivo.

## 📌 TODOs / Mejoras futuras
 
- Mejorar la visualización de gráficos con librerías más avanzadas
- Agregar opción de exportar el modelo en otros formatos
- Integrar una interfaz web para facilitar el uso

## 👨‍💻 Autor
https://www.linkedin.com/in/franco-garcia9701/ | https://github.com/FrancoGarciaC9701 

Muchas gracias por tomarse la molestia de leerlo, cualquier crítica constructiva es bien recibida.


