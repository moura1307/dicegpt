def ler(nome_arq):  ## Aqui é feito a leitura do corpus
    arquivo = open(nome_arq, 'r', encoding='utf-8')
    conteudo_arq = arquivo.read()
    arquivo.close()

    return conteudo_arq

def concordanciador(alvo, texto):  ## Aqui é feita a busca pela palavra alvo no corpus
    texto = texto.replace('\n', ' ')
    texto = texto.replace('\t', ' ')

    ocorrencias = list()
    encontrado_aqui = texto.find(alvo, 0)

    while encontrado_aqui > 0:
        pos_inicial = encontrado_aqui - (40 - len(alvo)//2)
        ocorrencias.append(texto[pos_inicial : pos_inicial + 80])

        encontrado_aqui = texto.find(alvo, encontrado_aqui + 1)

    return ocorrencias

def limpar(lista):  ## Aqui é feita a limpeza do corpus
    lixo = '.,:;?!`()[]{}\/|#$%^&*«»_'
    quase_limpo = [x.strip(lixo).lower() for x in lista]
    return [x for x in quase_limpo if x.isalpha() or '-' in x]

texto = ler('texto.txt')

##resultados = concordanciador(' tupí ', texto)
##for i in resultados:
##    print(i)

###########################################
## Aqui é só um pequeno teste da função limpar

corpus_sujo = texto.split()
corpus_limpo = limpar(corpus_sujo)

print(len(corpus_sujo))
print(len(corpus_limpo))

############################################

# para fins didáticos, a leitura do livro foi feito até a página 82.