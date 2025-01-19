import java.util.Scanner;

public class Main {
   public static void main(String[] args) {
      Scanner scanner = new Scanner(System.in);
      int a = scanner.nextInt();
      int b = scanner.nextInt();
      int c = scanner.nextInt();
      int d = scanner.nextInt();
      int res = a+b+c+d;
      System.out.println(res/60);
      System.out.println(res%60);
      scanner.close();
    }
}