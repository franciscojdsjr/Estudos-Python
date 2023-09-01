import re

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

def isValid(email):
    if re.fullmatch(regex, email):
      print("Valid email")
    else:
      print("Invalid email")
      
#isValid('franciscojdsjr@gmail.com')


#################




padrao = "\w{5,50}@\w{3,10}.\w{2,3}.\w{2,3}"
texto = "aaabbbcc rodrigo123@gmail.com.br"
resposta = re.search(padrao, texto)

#print(resposta.group())

padrao1 = "\w{5,50}@\w{3,10}.\w{2,3}(.\w{2,3})?"
texto1 = "aaabbccc franciscojdsjr@gmail.com.br"
resposta1 = re.search(padrao1, texto1)

#print(resposta1.group())


#####

padrao_molde = '(xx) XXXXX-XXXX'

padrao = "[0-9]{2}[0-9]{4,5}[0-9]{4}"

texto = 'eu gosto de pizza meu numero é 82991059072'

resposta = re.findall(padrao,texto)

#print(resposta)


from TelefonesBr import TellefonesBr

telefone = '558291059072'

telefone_objeto = TellefonesBr(telefone)

print(telefone_objeto)