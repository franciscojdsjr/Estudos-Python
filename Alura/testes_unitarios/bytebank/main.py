from codigo import Funcionarios


nome = Funcionarios('Francisco Yamato','29/12/1993',5000) 
esperado = True

print(nome._cargo_executivo() == esperado)