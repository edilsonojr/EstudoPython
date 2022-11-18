frase = "Curso em video python"
print(frase[3:13]) #Fatiando, pegando tudo da posição 3 até 13
print("""No Brasil, 38,7 milhões de pessoas vivem em lares sem 
qualquer renda do trabalho, nem informal. Elas representavam 17,9% 
da população em 2021, o segundo maior patamar já registrado desde 
2012. Só perde para 2020, quando o isolamento social para evitar a 
propagação da pandemia impediu que parte relevante dos trabalhadores, 
principalmente os informais, conseguisse trabalhar.""") #print longo
print(frase.count("o")) #Vai contar quantas letras "o" minúsculo existe em frase
print(frase.upper().count("O")) #Vai contar quantas letras "O" maiúsculo existe em frase
print(len(frase)) #Retorna a quantidade de letras na variável
print(frase.strip()) #Remove os espaços vazios antes e depois
print(frase.replace("python", "Android")) #Substitui todos os valores "python" para "Android"
print("Curso" in frase) #Verifica se existe a palavra "Curso" na variável frase
print(frase.lower().find("video")) #põe tudo pra minúsculo e procura por "video" em frase
print(frase.split()) #Separa as palavras na frase
print(frase.split()[0]) #Separa as palavras e mostra a palavra que se encontra na posição 0
