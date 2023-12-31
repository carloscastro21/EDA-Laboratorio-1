# -*- coding: utf-8 -*-
"""Histograma_dimensionalidad.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13zBVhsjqgM4mo-JHYZjSxvp3vPOknSLk
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("2.txt", sep=",", header=None)

dim = df.T.squeeze()

# Graficar un histograma
plt.hist(dim, bins=10, color="#607c8e", rwidth=0.9)
plt.title("Distancia entre puntos con dimensión 2")
plt.xlabel("Distancia")
plt.ylabel("Frecuencia")
plt.grid(True)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("10.txt", sep=",", header=None)

dim = df.T.squeeze()

# Graficar un histograma
plt.hist(dim, bins=10, color="#607c8e", rwidth=0.9)
plt.title("Distancia entre puntos con dimensión 10")
plt.xlabel("Distancia")
plt.ylabel("Frecuencia")
plt.xlim(0,2.5)
plt.grid(True)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("50.txt", sep=",", header=None)

dim = df.T.squeeze()

# Graficar un histograma
plt.hist(dim, bins=10, color="#607c8e", rwidth=0.9)
plt.title("Distancia entre puntos con dimensión 50")
plt.xlabel("Distancia")
plt.ylabel("Frecuencia")
plt.xlim(0,4)
plt.grid(True)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("100.txt", sep=",", header=None)

dim = df.T.squeeze()

# Graficar un histograma
plt.hist(dim, bins=10, color="#607c8e", rwidth=0.9)
plt.title("Distancia entre puntos con dimensión 100")
plt.xlabel("Distancia")
plt.ylabel("Frecuencia")
plt.xlim(0,5)
plt.grid(True)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("500.txt", sep=",", header=None)

dim = df.T.squeeze()

# Graficar un histograma
plt.hist(dim, bins=10, color="#607c8e", rwidth=0.9)
plt.title("Distancia entre puntos con dimensión 500")
plt.xlabel("Distancia")
plt.ylabel("Frecuencia")
plt.xlim(0,10.5)
plt.grid(True)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("1000.txt", sep=",", header=None)

dim = df.T.squeeze()

# Graficar un histograma
plt.hist(dim, bins=10, color="#607c8e", rwidth=0.9)
plt.title("Distancia entre puntos con dimensión 1000")
plt.xlabel("Distancia")
plt.ylabel("Frecuencia")
plt.xlim(10,14)
plt.grid(True)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("2000.txt", sep=",", header=None)

dim = df.T.squeeze()

# Graficar un histograma
plt.hist(dim, bins=10, color="#607c8e", rwidth=0.9)
plt.title("Distancia entre puntos con dimensión 2000")
plt.xlabel("Distancia")
plt.ylabel("Frecuencia")
plt.xlim(10,20)
plt.grid(True)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("5000.txt", sep=",", header=None)

dim = df.T.squeeze()

# Graficar un histograma
plt.hist(dim, bins=10, color="#607c8e", rwidth=0.9)
plt.title("Distancia entre puntos con dimensión 5000")
plt.xlabel("Distancia")
plt.ylabel("Frecuencia")
plt.xlim(25,30)
plt.grid(True)
plt.show()