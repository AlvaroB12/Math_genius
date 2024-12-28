# **Math Genius Library**

**Math Genius** es una poderosa librería de Python diseñada para realizar cálculos matemáticos avanzados de manera sencilla y eficiente. Ideal para estudiantes, académicos y desarrolladores, incluye herramientas para geometría, trigonometría, álgebra, estadística, probabilidad y mucho más.

---

## **Tabla de Contenidos**

1. [Descripción](#-)
2. [Instalación](#-)
3. [Módulos y Funciones](#-)
 -  [Geometría](#-)
 -  [Áreas y Volúmenes](#-)
 -  [Trigonometría](#-)
 -  [Aritmética](#-)
 -  [Probabilidad](#-)
 -  [Estadística](#-)
 -  [Teoría de Conjuntos](#-)
4. [Contribución](#-)
5. [Licencia](#-)
6. [Créditos](#-)

---

## **Descripción**

Math Genius te permite realizar cálculos avanzados de una manera intuitiva. Desde fórmulas geométricas hasta análisis estadístico, esta librería es la herramienta definitiva para resolver problemas matemáticos.

- **Limpia y Modular:** Cada módulo aborda un tema matemático específico.
- **Fácil de Extender:** Puedes agregar más funciones según tus necesidades.

---

## **Instalación**

**1. Clonar el repositorio:**

    git clone   https://github.com/AlvaroB12/math-genius.git

**2. Instalar dependencias:**

   pip install -r requirements.txt

**3.** ¡Listo! Ahora puedes comenzar a usar Math Genius.

---

## **Módulos y Funciones**

### **1. Geometría**

Funciones principales:

#### triangle_area_by_points(p1, p2, p3):
Calcula el área de un triángulo a partir de tres puntos en el plano.

    area = triangle_area_by_points((0, 0), (4, 0), (4, 3))
    print(area)  

##### **Salida:** 6.0

#### distance(p1, p2):
Calcula la distancia entre dos puntos.

    dist = distance((0, 0), (3, 4))
    print(dist)  

##### **Salida:** 5.0



---

### **2. Áreas y Volúmenes**

Funciones principales:

#### cylinder_volume(radius, height):
Calcula el volumen de un cilindro.

    volume = cylinder_volume(radius=5, height=10)
    print(volume)  

##### **Salida:** 785.398

#### sphere_volume(radius):
Calcula el volumen de una esfera.

    volume = sphere_volume(radius=3)
    print(volume)  

##### **Salida:** 113.097



---

### **3. Trigonometría**

Funciones principales:

#### pythagoras(a, b):
Calcula la hipotenusa de un triángulo rectángulo.

    hypotenuse = pythagoras(a=3, b=4)
    print(hypotenuse) 
 
##### **Salida:** 5.0

#### sin(degrees):
Calcula el seno de un ángulo dado en grados.

    result = sin(30)
    print(result)  

##### **Salida:** 0.5



---

### **4. Aritmética**

Funciones principales:

#### add(a, b):
Suma dos números.

    result = add(5, 3)
    print(result)  

##### **Salida:** 8

#### subtract(a, b):
Resta dos números.

    result = subtract(10, 4)
    print(result)
  
##### **Salida:** 6



---

### **5. Probabilidad y Estadística**

Funciones principales:

#### mean(data):
Calcula la media de una lista de datos.

    avg = mean([1, 2, 3, 4, 5])
    print(avg)  

##### **Salida:** 3.0

#### standard_deviation(data):
Calcula la desviación estándar.

    sd = standard_deviation([1, 2, 3, 4, 5])
    print(sd)  

##### **Salida:** 1.414



---

### **6. Teoría de Conjuntos**

Funciones principales:

#### union(set1, set2):
Devuelve la unión de dos conjuntos.

    result = union({1, 2}, {2, 3})
    print(result)  

##### **Salida:** {1, 2, 3}

#### intersection(set1, set2):
Devuelve la intersección de dos conjuntos.

    result = intersection({1, 2}, {2, 3})
    print(result)  

##### **Salida:** {2}



---

## **Contribución**

¡Estamos abiertos a nuevas ideas! Para contribuir:

**1.** Haz un fork del proyecto.


**2.** Crea una rama: 

    ```bash
    git checkout -b nueva-funcion.


**3.** Realiza tus cambios.


**4.** Abre un pull request detallando las modificaciones.




---

## **Licencia**

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.


---

## **Créditos**

Creado con cariño por Álvaro Bravo López .

---


    


