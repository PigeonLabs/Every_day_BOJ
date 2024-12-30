import java.util.Scanner;

public class Main {
   public static void main(String[] args) {
      Scanner scanner = new Scanner(System.in);
      int n = scanner.nextInt();
      int x = scanner.nextInt();
      int y = scanner.nextInt();
      double t = n/Math.pow((Math.pow(x,2)+Math.pow(y,2)),0.5);
      double xx = x*t;
      double yy = y*t;
      System.out.println((int)xx + " " + (int)yy);
      scanner.close();
    }
}