***Nota:*** Este semestre 2024-1 asistiré al semillero "análisis de datos con Python" como estudiante. La intención de este repositorio es compartir mis notas y diferentes aprendizajes provenientes de este semillero. Otro de los mótivos de este semillero es utilizar Visual Studio Code para llevarlo a cabo, ya que, actualmente el semillero es desarrollado en hojas de Colab. En este repositorio compartiré tanto archivos propios como provenientes del propio Semillero, es decir, hecho por el docente. 

# Semillero Análisis de datos con Python

> ## **Docente:** *Juan Guillermo Suarez*
![imagen ilustrativa](https://media.licdn.com/dms/image/D5612AQG-tCAXZkEUHw/article-cover_image-shrink_720_1280/0/1701564869677?e=2147483647&v=beta&t=nUKsbAydDoOpeoTXRsafO3Hg4HmbGCE77QE0nNpCbRU)

El semillero de Analisis de datos con Python, es un semillero disponible en la Universidad EIA y dirigido por el docente Juan Guillermo suarez; está dividido en 3 dificultados/complejidades: Básico, intermedio y avanzado. En el semestre 2024-1 abordaremos el básico y contiene los siguientes temas: 

### Temas 
1. Introducción al semillero, Python para el Análisis de Datos.
2. Numpy I.
3. Numpy II.
4. Numpy III.
5. Numpy IV. 
6. Pandas I. Formulación Reto 1 (EDA).
7. Pandas II.
8. Pandas III. Formulación Reto 2 (Modelos). 

---
Semana santa (25/03 - 03/24)

---

9. Pandas IV.
10. Matplotlip
11. Seaborn
12. Scikit-Learn I. 
13. Hiperparámetros y Validación de modelos.
14. Scikit-Leanr II.
15. Pronóstico para ST con Skfore.
16. Revisión de los proyectos 1 y 2.

## Estructura del Repositorio 
- Para presentar de mejor manera la unión de texto (Apartado teório) y código (apartado práctico) usaré notebooks de Jupyter.
- Cada uno de los encuentros (que por cierto, son semanales) tendrá su propio directorio, en este dividiré el contenido del encuentro en tantos ficheros como vea necesario, aunque se puede dar en el caso en el que el directorio contenga un único fichero con el contenido del  encuentro. 
- Cada encuentro tendrá su respectivo notebook de Jupyter, en el que estará tanto la parte teórica como práctica, recomiendo desarrollar cada fichero en el orden determinado.
- Tanto los encuentros, como los ficheros, estarán enumerados para ser expuestos en orden. 
- Recomiendo leer por completo el cada uno de lo ficheros para tener claridad del tema en cuestión. 

## Requisitos previos 
- **Intalación de Python**: Asegúrate de tener Python instalado en tu sistema. Es recomendable usar la última versión estable. Puedes descargarla desde el [sitio oficial de Python](https://www.python.org/downloads/).
- **Instalación de VSCode**: Si aún no lo tienes, descarga e instala Visual Studio Code desde el [sitio oficial de VSCode](https://code.visualstudio.com/download).
## Configuración del Entorno Python
Una vez instalado python, necesitaremos algunas bibliotecas para poder ejecutar el temario anteriormente expuesto. Necesitaremos las siguentes bibliotecas: 

- **NumPy**: Como hay varias sesiones dedicadas a NumPy, esta es una biblioteca fundamental para el manejo de arrays y matrices, esencial para el análisis numérico.
- **Pandas**: Fundamental para el manejo de datos estructurados, manipulación y análisis. Especialmente útil para el trabajo con datos tabulares.
- **Matplotlib**: Esta biblioteca de gráficos es necesaria para la visualización de datos, y será útil especialmente en la sesión dedicada a ella.
- **Seaborn**: Una biblioteca de visualización de datos basada en Matplotlib pero con interfaces de alto nivel y estilos más atractivos.
- **Scikit-Learn**: Para las sesiones sobre modelado de datos, aprendizaje automático, hiperparámetros y validación de modelos. Es la biblioteca principal para machine learning en Python.
- **Skforecast**: Para el pronóstico de series temporales. Esta biblioteca se utiliza para modelos de forecasting basados en scikit-learn.

Para poder realizar la instalación de las bibliotecas anteriormente mencionadas sigue los siguientes pasos: 

1. Abre la terminal o consola de comandos/cmd con permisos de administrador
2. Ejecuta el siguiente comando: 
```
pip install numpy pandas matplotlib seaborn scikit-learn skforecast jupyterlab

```

> **Nota**: Recomiendo instalar la extension de Visual Studio Code llamada "Better Coments" ya que yo la usare para mostrar diferente informacion en los ficheros. Permite poner comentarios con estilos como:
> 
> ![BetterComments](https://ihatetomatoes.net/wp-content/uploads/2018/07/img_better-comments.png)
