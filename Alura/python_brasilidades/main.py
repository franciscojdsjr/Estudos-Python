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

print(resposta.group())

padrao1 = "\w{5,50}@\w{3,10}.\w{2,3}(.\w{2,3})?"
texto1 = "aaabbccc franciscojdsjr@gmail.com.br"
resposta1 = re.search(padrao1, texto1)

print(resposta1.group())


