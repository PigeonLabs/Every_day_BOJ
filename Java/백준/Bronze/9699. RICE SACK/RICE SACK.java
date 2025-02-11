import java.util.Scanner;

public class Main {
   public static void main(String[] args) {
      Scanner scanner = new Scanner(System.in);
      int n = scanner.nextInt();
      for (int i = 0; i < n; i++) {
         int res = 1;
         for (int j = 0; j < 5; j++) {
            int t = scanner.nextInt();
            if (t>res) {
               res = t;
            }
         }
         System.out.println("Case #"+(i+1)+": "+res);
      }
      scanner.close();
   }
}
