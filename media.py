def calcular_media(notas):
    """
    Calcula a média de uma lista de notas recebida.
    Caso a lista esteja vazia, retorna 0.0 para evitar divisão por zero.
    """
    # Tratamento para lista de notas vazia
    if not notas:
        return 0.0

    soma_total = sum(notas)
    quantidade_notas = len(notas)
    
    return soma_total / quantidade_notas


# Exemplo de uso
notas_turma = [8.5, 7.0, 9.5, 6.0]
media_final = calcular_media(notas_turma)

# Exibição do resultado formatado com duas casas decimais
print(f"A média da turma é: {media_final:.2f}")
