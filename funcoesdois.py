def processador_texto(texto, **kwargs):
    # Função para contar palavras
    contar_palavras = lambda t: len(t.split())
    
    # Função para contar letras (desconsiderando espaços)
    contar_letras = lambda t: sum(1 for c in t if c.isalpha())
    
    # Função para inverter o texto
    inverter_texto = lambda t: t[::-1]
    
    # Função para substituir uma palavra no texto
    substituir_palavra = lambda t, velha, nova: t.replace(velha, nova)
    
    # Exibe o texto inicial
    print(f"Texto inicial: {texto}")
    
    # Inicializa o texto original
    resultado = texto
    
    # Primeira operação: contar palavras
    if "contar_palavras" in kwargs and kwargs["contar_palavras"]:
        print(f"Quantidade de palavras: {contar_palavras(resultado)}")
    
    # Segunda operação: contar letras
    if "contar_letras" in kwargs and kwargs["contar_letras"]:
        print(f"Quantidade de letras: {contar_letras(resultado)}")
    
    # Terceira operação: 
    if "inverter_texto" in kwargs and kwargs["inverter_texto"]:
        texto_invertido = inverter_texto(resultado)
        print(f"Texto invertido: {texto_invertido}")
    
    # Quarta operação: substituir palavras
    if "substituir_palavra" in kwargs and kwargs["substituir_palavra"]:
        velha, nova = kwargs["substituir_palavra"]  # Espera que valor seja uma tupla (velha_palavra, nova_palavra)
        resultado = substituir_palavra(resultado, velha, nova)
        print(f"Texto com as substituições apresentadas: {resultado}")
    
    # Retorna o texto final após todas as operações, **sem inversão** no final
    return resultado

# Exemplo de uso da função
texto_inicial = "Ela foi ao parque para caminhar e relaxar."
texto_processado = processador_texto(
    texto_inicial, 
    contar_palavras=True,
    contar_letras=True,
    inverter_texto=True,  
    substituir_palavra=("ao parque", "à praia")
)

print(f"Texto resultante: {texto_processado}")
