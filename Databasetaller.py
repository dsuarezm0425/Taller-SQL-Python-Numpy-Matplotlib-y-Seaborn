import pandas as pd
import mysql.connector
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Conexión a la base de datos
conn = mysql.connector.connect(
    host="localhost",         
    user="root",         
    password="0919",  
    database="Accidentes_Electricos"
)

# Cargar datos desde una tabla
df = pd.read_sql("SELECT * FROM accidentes_de_origen_electrico", conn)

# Análisis básico
print("🔹 Número de filas y columnas:", df.shape)
print("\n🔹 Tipos de datos:")
print(df.dtypes)

print("\n🔹 Cantidad de valores nulos por columna:")
print(df.isnull().sum())

print("\n🔹 Cantidad de valores únicos por columna:")
print(df.nunique())

print("\n🔹 Estadísticas descriptivas (solo numéricas):")
print(df.describe())

print("\n🔹 Primeras filas de la base:")
print(df.head())

# Ver primeras filas
print(df.head())

## Eliminar Duplicados
df = df.drop_duplicates()

## Elimina todas las filas que tengan al menos un Na
df = df.dropna()

##Revisar que columnas numericas tenemos
print(df.dtypes)

## Histograma de edad de persona de accidente electrico
plt.figure(figsize=(10,6))
sns.histplot(df["EDAD"], bins=15, kde=True, color='skyblue')
plt.title("Distribución de Edad en Accidentes Eléctricos")
plt.xlabel("Edad")
plt.ylabel("Frecuencia")
plt.grid(True)
plt.show()

## Histograma de tiempo de vinculacion de la persona accidentada
plt.figure(figsize=(10,6))
sns.histplot(df["TIEMPO_VINCULACION"], bins=10, kde=True, color='orange')
plt.title("Distribución del Tiempo de Vinculación")
plt.xlabel("Meses de Vinculación")
plt.ylabel("Frecuencia")
plt.grid(True)
plt.show()

## Histograma comparativo 
plt.figure(figsize=(10,6))
sns.histplot(data=df, x="EDAD", hue="SEXO", bins=15, kde=True, palette="Set2", multiple="stack")
plt.title("Distribución de Edad por Sexo")
plt.xlabel("Edad")
plt.ylabel("Frecuencia")
plt.grid(True)
plt.show()

## Grafico de cajas por edada y año
plt.figure(figsize=(12,6))
sns.boxplot(data=df, x="ANIO", y="EDAD", palette="coolwarm")
plt.title("Distribución de Edad por Año")
plt.xlabel("Año")
plt.ylabel("Edad")
plt.grid(True)
plt.show()

## Grafico de cajas por edada y sxo
plt.figure(figsize=(10,6))
sns.boxplot(data=df, x="SEXO", y="EDAD", palette="Set2")
plt.title("Distribución de Edad por Sexo")
plt.xlabel("Sexo")
plt.ylabel("Edad")
plt.grid(True)
plt.show()

##¿Cuál es la distribución anual de los accidentes eléctricos?
plt.figure(figsize=(12, 6))
sns.countplot(data=df, x="ANIO", hue="TRIMESTRE", palette="tab10")

plt.title("Distribución de accidentes eléctricos por año y trimestre", fontsize=14)
plt.xlabel("Año", fontsize=12)
plt.ylabel("Número de Accidentes", fontsize=12)
plt.legend(title="Trimestre")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

## 1. ¿Qué empresa reporta la mayor cantidad de accidentes eléctricos?
import matplotlib.pyplot as plt

# Contar accidentes por empresa
accidentes_por_empresa = df["EMPRESA"].value_counts().head(5)  # Las 5 empresas con más accidentes

# Crear gráfico de torta
plt.figure(figsize=(9, 9))
plt.pie(accidentes_por_empresa.values, labels=accidentes_por_empresa.index, autopct="%1.1f%%", colors=plt.cm.Set3.colors)
plt.title("Top 5 empresas con más accidentes eléctricos", fontsize=14)
plt.axis("equal")  # Para mantener proporciones
plt.show()


### 2 Cuál es la causa más frecuente de los accidentes eléctricos y el origen del accidente ?

# Obtener los valores más frecuentes
causas = df["CAUSA_ACCIDENTE"].value_counts().head(5)
origenes = df["ORIGEN_ACCIDENTE"].value_counts().head(5)
lesiones = df["TIPO_LESION"].value_counts().head(5)

# Crear la figura con 3 gráficos de torta
fig, axes = plt.subplots(1, 3, figsize=(20, 6))

# Torta de causas
axes[0].pie(causas.values, labels=causas.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.tab20.colors)
axes[0].set_title("Principales causas")

# Torta de orígenes
axes[1].pie(origenes.values, labels=origenes.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Set3.colors)
axes[1].set_title("Principales orígenes")

# Torta de tipos de lesión
axes[2].pie(lesiones.values, labels=lesiones.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Pastel1.colors)
axes[2].set_title("Tipos de lesión más frecuentes")

plt.tight_layout()
plt.show()


## Cuales son las 2 empresas con mayor accidentalidad , cuales el tipo de contrato de los trabajadores y que grado de escolaridad tienen..

# Asegurarse de que no haya espacios extra en los nombres de empresa
df["EMPRESA"] = df["EMPRESA"].str.strip()

# Obtener las 2 empresas con mayor número de accidentes
top_empresas = df["EMPRESA"].value_counts().head(2).index.tolist()

# Crear subplots (3 gráficos por cada empresa)
fig, axes = plt.subplots(2, 3, figsize=(20, 12))

for i, empresa in enumerate(top_empresas):
    empresa_df = df[df["EMPRESA"] == empresa]

    # Gráfico de barras para causas de accidente
    causas = empresa_df["CAUSA_ACCIDENTE"].value_counts().head(5)
    axes[i][0].bar(causas.index, causas.values, color='skyblue')
    axes[i][0].set_title(f"Causas - {empresa[:30]}")
    axes[i][0].tick_params(axis='x', rotation=45)

    # Gráfico de barras para tipo de vinculación
    vinculacion = empresa_df["TIPO_VINCULACION"].value_counts()
    axes[i][1].bar(vinculacion.index, vinculacion.values, color='lightgreen')
    axes[i][1].set_title(f"Vinculación - {empresa[:30]}")
    axes[i][1].tick_params(axis='x', rotation=45)

    # Gráfico de barras para grado de escolaridad
    escolaridad = empresa_df["GRADO_ESCOLARIDAD"].value_counts().head(5)
    axes[i][2].bar(escolaridad.index, escolaridad.values, color='salmon')
    axes[i][2].set_title(f"Escolaridad - {empresa[:30]}")
    axes[i][2].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()

### Cual es el departamento con mayor accidentalidad y que año tiene el mayor porcentaje ?

# Agrupar por departamento y calcular porcentaje
dept_counts = df['DEPARTAMENTO'].value_counts()
dept_percent = (dept_counts / len(df)) * 100

# Agrupar por año y calcular porcentaje
anio_counts = df['ANIO'].value_counts().sort_index()
anio_percent = (anio_counts / len(df)) * 100

# ----- Gráfico 1: Porcentaje por departamento -----
plt.figure(figsize=(12, 6))
dept_percent.sort_values(ascending=False).plot(kind='bar', color='skyblue')
plt.title('Porcentaje de Accidentalidad por Departamento')
plt.ylabel('Porcentaje (%)')
plt.xlabel('Departamento')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Contar accidentes por año
anio_counts = df['ANIO'].value_counts().sort_index()

# Calcular el porcentaje por año
anio_percent = (anio_counts / anio_counts.sum()) * 100

# Crear gráfico de torta
plt.figure(figsize=(8, 8))
plt.pie(anio_percent.values,
        labels=anio_percent.index,
        autopct='%1.1f%%',
        startangle=140,
        colors=plt.cm.Pastel2.colors)
plt.title("Porcentaje de Accidentes Eléctricos por Año")
plt.axis('equal')  # Para que la torta sea un círculo
plt.tight_layout()
plt.show()

## Cual es el trimestre del año con mayor accidentalidad y cuales son los % de cada trimestre?

# Contar accidentes por trimestre
trimestre_counts = df['TRIMESTRE'].value_counts().sort_index()

# Calcular porcentaje por trimestre
trimestre_percent = (trimestre_counts / trimestre_counts.sum()) * 100

# Etiquetas para los trimestres
labels = [f"Trimestre {i}" for i in trimestre_counts.index]

# Crear gráfico de torta
plt.figure(figsize=(8, 8))
plt.pie(trimestre_percent.values,
        labels=labels,
        autopct='%1.1f%%',
        startangle=140,
        colors=plt.cm.Set3.colors)
plt.title("Porcentaje de Accidentes Eléctricos por Trimestre")
plt.axis('equal')  # Mantener forma circular
plt.tight_layout()
plt.show()


# Cerrar la conexión 
conn.close()
