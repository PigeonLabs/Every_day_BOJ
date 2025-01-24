import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int a = scanner.nextInt();
        int b = scanner.nextInt();
        int c = scanner.nextInt();
        int d = scanner.nextInt();
        int res;
        if (a+d<=b+c) {
         res = a+d;
        }
        else {
         res  = b+c;
        }
        System.out.println(res);
        scanner.close();
    }
}