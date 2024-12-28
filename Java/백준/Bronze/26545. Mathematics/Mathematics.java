import java.util.Scanner;

public class Main {
   public static void main(String[] args) {
      int res = 0;
      Scanner scanner = new Scanner(System.in);
      int n = scanner.nextInt();
      for (int i=0;i<n;i++) {
         int t = scanner.nextInt();
         res += t;
      }
      System.out.println(res);
      scanner.close();
    }
}