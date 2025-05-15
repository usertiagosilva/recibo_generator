from num2words import num2words

def valor_por_extenso(valor: float) -> str:
    """
    Converte um valor numérico para sua forma por extenso, em português.
    
    """
    inteiro = int(valor)
    centavos = round((valor - inteiro) * 100)

    valor_extenso = num2words(inteiro, lang='pt-br') + " reais"
    
    if centavos > 0:
        valor_extenso += f" e {num2words(centavos, lang='pt-br')} centavos"

    return valor_extenso