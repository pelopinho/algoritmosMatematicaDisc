<!-- PROGRAMA04 - Criar uma calculadora para realizar operações matemáticas básicas-->

import java.util.Scanner; // importação da classe 'Scanner' que permite a entrada de dados pelo usuário
public class Programa04 {

    public static void main(String[] args) {
        Scanner a = new Scanner(System.in);
        double resultado;

        // Mensagens iniciais: impressão da entrada de dados onde o usuário irá colocar dois números para realizar uma operação
        System.out.println("\n----------Calculadora---------- ");
        System.out.println("\nDigite o número: ");
        double num1 = a.nextDouble();
        System.out.println("\nDigite outro número: ");
        double num2 = a.nextDouble();

        // Limpa a entrada do teclado
        a.nextLine();

        // Apresenta opções de operação: adição, subtração, multiplicação e divisão (para realizar a operação, é necessário entrar com o respectivo símbolo)
        System.out.println("\nInforme a operação que deseja: ");
        System.out.println("\nAdição (+)");
        System.out.println("\nSubtração (-)");
        System.out.println("\nMultiplicação (*)");
        System.out.println("\nDivisão (/)");
        String operacao = a.nextLine();

        // Verifica a operação escolhida pelo usuário através da estrutura 'if-else'
        if(operacao.equals("+")){
            resultado = num1 + num2;
            System.out.println("O resultado é igual a "+resultado);
        } else if(operacao.equals("-")) {
            resultado = num1 - num2;
            System.out.println("O resultado é igual a "+resultado);
        }else if(operacao.equals("*")) {
            resultado = num1 * num2;
            System.out.println("O resultado é igual a "+resultado);
        } else if(operacao.equals("/")){
            // Verifica se o segundo número é zero (divisão por zero)
            if (num2 == 0) {
                System.out.println("Erro: DIVISÃO POR 0");
            } else {
                resultado = num1 / num2;
                System.out.println("O resultado é igual a "+resultado);
            }
        }

        // Fecha o Scanner
        a.close();
    }
}
