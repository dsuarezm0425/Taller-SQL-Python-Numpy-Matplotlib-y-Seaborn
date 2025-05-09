import mysql.connector
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Conectar a la base de datos MySQL
conn = mysql.connector.connect(
    host="localhost",  
    user="root",  
    password="0919",  
    database="accidentes_electricos",  
)

#Cargar datos desde una tabla
df = pd.read_sql("SELECT * FROM accidentes_de_origen_electrico", conn)

# Ver primeras filas
print(df.head())

## Eliminar Duplicados
df = df.drop_duplicates()

#Cerrar la conexión
conn.close()