import pytest
class Sequencia:
    def __iter__(self):
        self.anterior = 0
        self.proximo = 1
        self.iteracao = 1

        return self

    def __next__(self):
        fibonacci = [self.anterior]
        try:
            self.iteracao = int(input("Informe a sequencia desejada: "))
            if self.iteracao == 0:
                raise StopIteration
        except:
            print("Operação Cancelada")
        for x in range(self.iteracao -1):
            soma= self.proximo + self.anterior
            self.anterior = self.proximo
            self.proximo = soma
            fibonacci.append(self.proximo)

        assert len(fibonacci) == self.iteracao
        return fibonacci
