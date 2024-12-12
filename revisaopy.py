dados = {
    2021: {
        'Fazenda A': {'milho': 100, 'soja': 150, 'trigo': 200},
        'Fazenda B': {'milho': 120, 'soja': 130, 'trigo': 180},
        'Fazenda C': {'milho': 110, 'soja': 140, 'trigo': 190},
    },
    2022: {
        'Fazenda A': {'milho': 130, 'soja': 160, 'trigo': 210},
        'Fazenda B': {'milho': 140, 'soja': 150, 'trigo': 200},
        'Fazenda C': {'milho': 135, 'soja': 155, 'trigo': 195},
    },
    2023: {
        'Fazenda A': {'milho': 140, 'soja': 170, 'trigo': 220},
        'Fazenda B': {'milho': 150, 'soja': 160, 'trigo': 210},
        'Fazenda C': {'milho': 145, 'soja': 165, 'trigo': 205},
    }
}

# Função para encontrar o ano com a produção total máxima e mínima
def encontrar_anos_max_min(dados):
    producao_por_ano = {ano: sum(sum(culturas.values()) for culturas in fazendas.values()) for ano, fazendas in dados.items()}
    ano_max = max(producao_por_ano, key=producao_por_ano.get)
    ano_min = min(producao_por_ano, key=producao_por_ano.get)
    return ano_max, ano_min

# Função para identificar a cultura com a maior e menor produção total ao longo dos anos
def encontrar_culturas_max_min(dados):
    producao_por_cultura = {}
    for ano, fazendas in dados.items():
        for fazenda, culturas in fazendas.items():
            for cultura, producao in culturas.items():
                if cultura not in producao_por_cultura:
                    producao_por_cultura[cultura] = 0
                producao_por_cultura[cultura] += producao
    cultura_max = max(producao_por_cultura, key=producao_por_cultura.get)
    cultura_min = min(producao_por_cultura, key=producao_por_cultura.get)
    return cultura_max, cultura_min

# Função para encontrar a fazenda com a produção máxima e mínima em um determinado ano
def encontrar_fazendas_max_min(dados, ano):
    if ano not in dados:
        return None, None
    producao_por_fazenda = {fazenda: sum(culturas.values()) for fazenda, culturas in dados[ano].items()}
    fazenda_max = max(producao_por_fazenda, key=producao_por_fazenda.get)
    fazenda_min = min(producao_por_fazenda, key=producao_por_fazenda.get)
    return fazenda_max, fazenda_min

# Executando as funções
ano_max, ano_min = encontrar_anos_max_min(dados)
print(f"Ano com a produção total máxima: {ano_max}")
print(f"Ano com a produção total mínima: {ano_min}")

cultura_max, cultura_min = encontrar_culturas_max_min(dados)
print(f"Cultura com a maior produção total: {cultura_max}")
print(f"Cultura com a menor produção total: {cultura_min}")

ano_selecionado = 2022
fazenda_max, fazenda_min = encontrar_fazendas_max_min(dados, ano_selecionado)
print(f"No ano {ano_selecionado}, a fazenda com a produção máxima foi: {fazenda_max}")
print(f"No ano {ano_selecionado}, a fazenda com a produção mínima foi: {fazenda_min}")
