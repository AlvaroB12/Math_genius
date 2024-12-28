class Main():
  class Mates():
    class Aritmetica():
      def Sumar(a, b):
        return a + b
input1 = 'Ingrese el 1er número'
input2 = 'Ingrese el 2do número'
Sumar = Main.Mates.Aritmetica.Sumar(float(input(input1)), float(input(input2)))
print(f"El resultado es {Sumar}.")
