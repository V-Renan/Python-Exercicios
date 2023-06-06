frase = str(input('Digite uma frase: ')).upper().strip()
print(f"""A letra (a) aparece {frase.count('A')}
A primeira letra (A) apareceu na posição {frase.find('A')+1}
A última letra (A) apareceu na posição {frase.rfind('A')+1}""")

