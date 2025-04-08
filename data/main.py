import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import json
import seaborn as sns
import matplotlib.pyplot as plt

DATASET_PATH = 'data/MachineLearningCVE/combined_dataset.csv'
MODEL_PATH = 'modelo_entrenado.pkl'

def cargar_dataset():
    dataset_path = DATASET_PATH
    try:
        dataset = pd.read_csv(dataset_path)
        dataset.columns = dataset.columns.str.strip()  # Limpia espacios
        dataset.columns = dataset.columns.str.lower()  # Opcional: pasa todo a minúsculas
        print("[INFO] Dataset cargado correctamente.")
        print("[INFO] Columnas del dataset:", dataset.columns.tolist())
        return dataset
    except Exception as e:
        print(f"[ERROR] No se pudo cargar el dataset: {e}")
        return None

def preprocesar_dataset(dataset):
    print("[INFO] Preprocesando dataset...")
    dataset = dataset.rename(columns=lambda x: x.strip())
    X = dataset.drop('label', axis=1)
    y = dataset['label']
    return train_test_split(X, y, test_size=0.3, random_state=42)

def entrenar_modelo(X_train, y_train):
    print("[INFO] Entrenando modelo...")
    modelo = RandomForestClassifier(n_estimators=100, random_state=42)
    modelo.fit(X_train, y_train)
    joblib.dump(modelo, MODEL_PATH)
    print(f"[INFO] Modelo guardado en {MODEL_PATH}")

def cargar_modelo():
    print("[INFO] Cargando modelo entrenado...")
    return joblib.load(MODEL_PATH)

def evaluar_modelo(modelo, X_test, y_test):
    print("[INFO] Evaluando modelo...")
    y_pred = modelo.predict(X_test)

    # Reporte de clasificación
    reporte = classification_report(y_test, y_pred, output_dict=True)
    print("\n[INFO] Reporte de clasificación:\n")
    print(classification_report(y_test, y_pred))

    # Guardar reporte como JSON
    with open('reporte.json', 'w') as f:
        json.dump(reporte, f, indent=4)
    print("[INFO] Reporte guardado en reporte.json")

    # Matriz de confusión
    matriz_confusion = confusion_matrix(y_test, y_pred)
    print("[INFO] Matriz de confusión (numérica):\n")
    print(matriz_confusion)

    # Visualización de la matriz de confusión
    plt.figure(figsize=(8, 6))
    sns.heatmap(matriz_confusion, annot=True, fmt='d', cmap='Blues', cbar=False)
    plt.title('Matriz de Confusión')
    plt.xlabel('Predicciones')
    plt.ylabel('Valores Reales')
    plt.tight_layout()
    plt.show()

def menu():
    dataset = cargar_dataset()
    if dataset is None:
        return

    X_train, X_test, y_train, y_test = preprocesar_dataset(dataset)

    while True:
        print("\n=== Menú Principal ===")
        print("1. Entrenar modelo")
        print("2. Evaluar modelo")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            entrenar_modelo(X_train, y_train)
        elif opcion == '2':
            modelo = cargar_modelo()
            evaluar_modelo(modelo, X_test, y_test)
        elif opcion == '3':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")

if __name__ == "__main__":
    menu()
