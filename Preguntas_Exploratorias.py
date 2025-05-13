import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el archivo limpio
df = pd.read_csv("AccidentesElectricos_Limpio.csv")

#1. ¿Cuál es la distribución de edad de las personas que han sufrido accidentes eléctricos? (histograma)
plt.figure(figsize=(10,6))
sns.histplot(df["EDAD"], bins=15, kde=True, color='skyblue')
plt.title("1. Distribución de Edad de Personas con Accidentes Eléctricos")
plt.xlabel("Edad")
plt.ylabel("Frecuencia")
plt.show()

# 2. ¿Cómo varía la edad según el sexo? (histograma)
plt.figure(figsize=(10,6))
sns.histplot(data=df, x="EDAD", hue="SEXO", bins=15, kde=True, palette="Set2", multiple="stack")
plt.title("2. Distribución de Edad por Sexo en Accidentes Eléctricos")
plt.xlabel("Edad")
plt.ylabel("Frecuencia")
plt.show()

#3. ¿Cómo se distribuyen los accidentes por año? (countplot)
plt.figure(figsize=(12, 6))
sns.countplot(data=df, x="ANIO", palette="tab10")
plt.title("3. Distribución de accidentes eléctricos por año", fontsize=14)
plt.xlabel("Año", fontsize=12)
plt.ylabel("Número de Accidentes", fontsize=12)
plt.xticks(rotation=45)
plt.show()

#4. ¿Cuál es el trimestre con más accidentes y su porcentaje? (gráfico torta)
trimestre_counts = df['TRIMESTRE'].value_counts().sort_index()      #contar accidentes por trimestre
trimestre_percent = (trimestre_counts / trimestre_counts.sum()) * 100       #para % por trimestre
labels = [f"Trimestre {i}" for i in trimestre_counts.index]     #etiqueta para trimestres
plt.figure(figsize=(8, 8))
plt.pie(trimestre_percent.values,
        labels=labels,
        autopct='%1.1f%%',
        startangle=140,
        colors=plt.cm.Set3.colors)
plt.title("4. Porcentaje de Accidentes Eléctricos por Trimestre")
plt.axis('equal')  # Mantener forma circular
plt.tight_layout()
plt.show()

#5. ¿Cuál es el departamento con más accidentalidad? (barras de porcentaje)
dept_counts = df['DEPARTAMENTO'].value_counts()     #contar departamentos
dept_percent = (dept_counts / len(df)) * 100        # %
anio_counts = df['ANIO'].value_counts().sort_index()
anio_percent = (anio_counts / len(df)) * 100        # lo mismo pero con años
plt.figure(figsize=(12, 6))
dept_percent.sort_values(ascending=False).plot(kind='bar', color='skyblue')
plt.title('5. Porcentaje de Accidentalidad por Departamento')
plt.ylabel('Porcentaje (%)')
plt.xlabel('Departamento')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#6. ¿Cuáles son las principales causas, orígenes y tipos de lesión? (gráfico torta)
# Obtener los valores más frecuentes
causas = df["CAUSA_ACCIDENTE"].value_counts().head(5)
origenes = df["ORIGEN_ACCIDENTE"].value_counts().head(5)
lesiones = df["TIPO_LESION"].value_counts().head(5)
# Crear la figura con 3 gráficos de torta
fig, axes = plt.subplots(1, 3, figsize=(25, 6))
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
plt.subplots_adjust(wspace=0.5) 
plt.show()

#7. ¿Cuáles son las primeras 5 empresas que reportan más accidentes? (gráfico torta)
accidentes_por_empresa = df["EMPRESA"].value_counts().head(5)  # Las 5 empresas con más accidentes
plt.figure(figsize=(9, 9))
plt.pie(accidentes_por_empresa.values, labels=accidentes_por_empresa.index, autopct="%1.1f%%", colors=plt.cm.Set3.colors)
plt.title("7. Top 5 empresas con más accidentes eléctricos", fontsize=14)
plt.axis("equal")  # Para mantener proporciones
plt.show()

#8. ¿Cuáles son las principales características de los accidentes en las dos empresas con mayor número de accidentes (histograma)
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
plt.tight_layout(pad=3.0)
plt.show()