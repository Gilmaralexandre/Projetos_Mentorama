import pytest
from funções import de5, de7, deambos, diferente

class function:
    def setup(self):
        pass

    def teste1(self):
        resultado1 = de5(25)

    def teste2(self):
        resultado2 = de7(28)

    def teste3(self):
        resultado3 = deambos(35)

    def teste4(self):
        resultado4 = diferente(36)

        assert resultado1 == "fizz"
        assert resultado2 == "buzz"
        assert resultado3 == "fizzbuzz"
        assert resultado4 == "miss"
       