import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        while (true) {
            int a = scanner.nextInt();
            int b = scanner.nextInt();
            int c = scanner.nextInt();
            
            if (a == 0 && b == 0 && c == 0) {
                break;
            }
            
            if ((b - a) == (c - b)) {
                System.out.println("AP " + (2 * c - b));
            }
            else if ((b / a) == (c / b)) {
                System.out.println("GP " + (c * c / b));
            }
        }
        scanner.close();
    }
}