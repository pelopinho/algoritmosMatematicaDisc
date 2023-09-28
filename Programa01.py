# PROGRAMA 01 - Criar código para que o usuário informe a expressão lógica e o programa forneça a tabela verdade conforme tal expressão.

import itertools
import re

# Os "imports" que estão sendo utilizados acima servem para manipular o código. 
# O "import intertools" tem acesso à biblioteca-padrão e o fornece para gerar modificações; 
# Já o "import re" tem como função extrair as variáveis da expressão fornecida pelo usuário.


def evaluate_expression(expression, variables, values):
    for i in range(len(variables)):
        expression = expression.replace(variables[i], str(values[i]))
    return int(eval(expression))  # Retorna 0 ou 1 como inteiro

def main():
    expression = input("Digite a expressão lógica (usando 'and', 'or', 'not', parênteses e variáveis): ")
    variables = set(re.findall(r'\b[A-Za-z]\b', expression))
    variables = sorted(list(variables))
    
    # Nas linhas 11 e 16 temos, respectivamente, as "defs" (evaluate_expression() e main()). 
    # Elas são denominadas como funções, são conceituadas como sequência de comandos com a finalidade de executar determinadas tarefas em certas situações.
    # A função "evaluate_expression" recebe a expressão, as variáveis e os valores das variáveis informadas pelo usuário
    # para uma combinação específica. Ela substitui os valores das variáveis na expressão e depois a avalia
    # usando outra função chamada "eval". Logo, a primeira "def" retorna o resultado como um inteiro (0 ou 1);
    
    # A função "main", escrita na linha 16 é definida como o ponto de entrada do programa, onde será solicitado ao usuário
    # que insira uma expressão lógica para ser avaliada. Através de expressões regulares ("re.findall"), encontra todas as variáveis
    # na expressão e as armazenadas em um conjunto. Em seguida, converte o conjunto em uma lista ordenada. 

    combinations = list(itertools.product([0, 1], repeat=len(variables)))

    print("Tabela Verdade:")
    print("--------------")
    
    # Cabeçalho com as variáveis
    header = " | ".join(variables)
    print(header + " | Resultado Final")
    
    print("-" * (len(header) + 20))  # Linha de separação
    
    for comb in combinations:
        result = evaluate_expression(expression, variables, comb)
        row = " | ".join(str(val) for val in comb)
        print(row + f" | {result}")

if __name__ == "__main__":
    main()

    # Nessa parte da estrutura, são gerados todos os símbolos possíveis (0s e 1s) para as variáveis expressas usando a função "itertools.product".
    # Em seguida, o cabeçalho da tabela com os nomes das variáveis e a coluna Resultado Final são exibidos.
    # Logo após, é utilizado o comando "join" para formatar a linha de cabeçalho já criada. Finalmente, é impressa uma linha de separação
    # com hífens, cujo tamanho é definido com base no cabeçalho.

    # Dentro do loop "for", para cada combinação, avaliamos a expressão lógica utilizando a primeira função descrita, passando pelas variáveis,
    # a combinação de valores e a expressão. Posteriormente, é formatada a linha com os valores da combinação e o resultado final e assim o código imprime na tela.

    # Por fim, a estrutura de condição "if" garante que o código dentro dele seja executado somente quando o script for executado diretamente e não quando
    # for importando como um módulo.