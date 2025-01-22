import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        
        for (int i = 0; i < n; i++) {
            double a = scanner.nextDouble();
            String b = scanner.next();
            
            if (b.equals("kg")) {
                System.out.println(String.format("%.4f lb", a * 2.2046));
            }
            else if (b.equals("lb")) {
                System.out.println(String.format("%.4f kg", a * 0.4536));
            }
            else if (b.equals("l")) {
                System.out.println(String.format("%.4f g", a * 0.2642));
            }
            else if (b.equals("g")) {
                System.out.println(String.format("%.4f l", a * 3.7854));
            }
        }
        
        scanner.close();
    }
}