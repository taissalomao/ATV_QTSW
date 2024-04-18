class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        # Verifica se os valores dos lados são positivos
        if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
            raise ValueError("Os lados de um triângulo devem ser positivos e maiores que zero.")
        
        # Verifica se os lados formam um triângulo válido
        if (lado1 + lado2 <= lado3) or (lado1 + lado3 <= lado2) or (lado2 + lado3 <= lado1):
            raise ValueError("Os lados não formam um triângulo válido.")

        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def tipo_triangulo(self):
        # Verifica se todos os lados são iguais
        if self.lado1 == self.lado2 == self.lado3:
            return "Equilátero"
        
        # Verifica se dois lados são iguais e um é diferente
        if self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            return "Isósceles"
        
        # Caso contrário, é um triângulo escaleno
        return "Escaleno"
