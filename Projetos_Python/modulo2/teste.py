from gera_Fibonacci import Sequencia

gerar = Sequencia()
gerar = iter(gerar)
sequencia_fib = {
posição + 1 : valor for posição,
valor in enumerate(next(gerar))
}
print(sequencia_fib)