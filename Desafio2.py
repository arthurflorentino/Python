import java.util.Scanner;

public class Triangulo {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        // Lendo os três segmentos de reta
        System.out.print("Digite o comprimento do primeiro segmento: ");
        int a = sc.nextInt();
        System.out.print("Digite o comprimento do segundo segmento: ");
        int b = sc.nextInt();
        System.out.print("Digite o comprimento do terceiro segmento: ");
        int c = sc.nextInt();

        // Verificando se é possível formar um triângulo
        if (a < b + c && b < a + c && c < a + b) {
            System.out.println("É possível formar um triângulo.");
        } else {
            System.out.println("Não é possível formar um triângulo.");
        }
    }
}