endereco = "Rua das Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 57081-760"

import re #RegEx

padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")

busca = padrao.search(endereco) #Match

if busca:
    cep = busca.group()
    print(cep)