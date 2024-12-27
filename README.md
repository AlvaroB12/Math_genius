# Math_genius
## Introducción
Math_genius es una librería de 
python que abarca todo el ámbito
de las matemáticas, desde 
operaciones simples hasta 
integrales o estadísticas. 
Este manual está dividido por 
cada apartado que incluye esta 
librería, incluyendo todas las 
funciones que contienen y para 
qué sirve.

## 1. Aritmética:

### 1.1 Add
La función Add consiste en sumar dos números
'a' y 'b'. Por ejemplo:

#### Código:
    
    from Math_genius import *
    Add(250, 500)

#### Salida: 
750

### 1.2 Substract
La función Substract consiste en restar dos
números 'a' y 'b'. Por ejemplo:

#### Código:

    from Math_genius import *
    Substract(235, 87)

#### Salida: 
123

### 1.3 Multiply
La función Multiply regresa el producto de dos
números 'a' y 'b'. Por ejemplo:

#### Código:

     from Math_genius import *
     Multiply(25, 45)

#### Salida: 
1125

### 1.4 Divide
La función Divide incluye el cociente entre
dos números 'a' y 'b'. Por ejemplo:

#### Código:

     from Math_genius import *
     Divide(100, 5)

#### Salida: 
20
   
Además, si el número 'b' es equivalente a 0, 
devuelve un mensaje de error.


---

# 🌟 Math Genius Library

**Math Genius** es una poderosa librería de Python diseñada para realizar cálculos matemáticos avanzados de manera sencilla y eficiente. Ideal para estudiantes, académicos y desarrolladores, incluye herramientas para geometría, trigonometría, álgebra, estadística, probabilidad y mucho más.

---

## Tabla de Contenidos

1. [Descripción](#-descripción)
2. [Instalación](#-instalación)
3. [Uso](#-uso)
4. [Módulos y Funciones](#-módulos-y-funciones)
   - [Geometría](#-geometría)
   - [Áreas y Volúmenes](#-áreas-y-volúmenes)
   - [Trigonometría](#-trigonometría)
   - [Aritmética](#-aritmética)
   - [Álgebra](#-álgebra)
   - [Probabilidad](#-probabilidad)
   - [Estadística](#-estadística)
   - [Teoría de Conjuntos](#-teoría-de-conjuntos)
5. [Contribución](#-contribución)
6. [Licencia](#-licencia)
7. [Créditos](#-créditos)

---

## ✨ Descripción

Math Genius te permite realizar cálculos avanzados de una manera intuitiva. Desde fórmulas geométricas hasta análisis estadístico, esta librería es la herramienta definitiva para resolver problemas matemáticos.

- **Limpia y Modular:** Cada módulo aborda un tema matemático específico.
- **Fácil de Extender:** Puedes agregar más funciones según tus necesidades.

---

## 🔧 Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/tu_usuario/math-genius.git

2. Instalar dependencias:

pip install -r requirements.txt


3. ¡Listo! Ahora puedes comenzar a usar Math Genius.




---

🚀 Uso

from math_genius.geometry import triangle_area_by_points
from math_genius.trigonometry import pythagoras

# Área de un triángulo
area = triangle_area_by_points((0, 0), (4, 0), (4, 3))
print(f"Área del triángulo: {area}")

# Hipotenusa de un triángulo
hipotenusa = pythagoras(a=3, b=4)
print(f"Hipotenusa: {hipotenusa}")


---

📚 Módulos y Funciones

🧮 Geometría

Funciones principales:

triangle_area_by_points(p1, p2, p3):
Calcula el área de un triángulo a partir de tres puntos en el plano.

area = triangle_area_by_points((0, 0), (4, 0), (4, 3))
print(area)  # Salida: 6.0

distance(p1, p2):
Calcula la distancia entre dos puntos.

dist = distance((0, 0), (3, 4))
print(dist)  # Salida: 5.0



---

📐 Áreas y Volúmenes

Funciones principales:

cylinder_volume(radius, height):
Calcula el volumen de un cilindro.

volume = cylinder_volume(radius=5, height=10)
print(volume)  # Salida: 785.398

sphere_volume(radius):
Calcula el volumen de una esfera.

volume = sphere_volume(radius=3)
print(volume)  # Salida: 113.097



---

📏 Trigonometría

Funciones principales:

pythagoras(a, b):
Calcula la hipotenusa de un triángulo rectángulo.

hypotenuse = pythagoras(a=3, b=4)
print(hypotenuse)  # Salida: 5.0

sin(degrees):
Calcula el seno de un ángulo dado en grados.

result = sin(30)
print(result)  # Salida: 0.5



---

➕ Aritmética

Funciones principales:

add(a, b):
Suma dos números.

result = add(5, 3)
print(result)  # Salida: 8

subtract(a, b):
Resta dos números.

result = subtract(10, 4)
print(result)  # Salida: 6



---

📊 Probabilidad y Estadística

Funciones principales:

mean(data):
Calcula la media de una lista de datos.

avg = mean([1, 2, 3, 4, 5])
print(avg)  # Salida: 3.0

standard_deviation(data):
Calcula la desviación estándar.

sd = standard_deviation([1, 2, 3, 4, 5])
print(sd)  # Salida: 1.414



---

∞ Teoría de Conjuntos

Funciones principales:

union(set1, set2):
Devuelve la unión de dos conjuntos.

result = union({1, 2}, {2, 3})
print(result)  # Salida: {1, 2, 3}

intersection(set1, set2):
Devuelve la intersección de dos conjuntos.

result = intersection({1, 2}, {2, 3})
print(result)  # Salida: {2}



---

🤝 Contribución

¡Estamos abiertos a nuevas ideas! Para contribuir:

1. Haz un fork del proyecto.


2. Crea una rama: git checkout -b nueva-funcion.


3. Realiza tus cambios.


4. Abre un pull request detallando las modificaciones.




---

📜 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.


---

🙌 Créditos

Creado con cariño por Álvaro Bravo López .

---


    


