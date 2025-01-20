import java.util.Scanner;

public class Main {
   public static void main(String[] args) {
      Scanner scanner = new Scanner(System.in);
      int n = scanner.nextInt();
      int res_a = 0;
      int res_b = 0;
      for (int i=0;i<n;i++) {
         int t = scanner.nextInt();
         if (t<30) {
            res_a += 10;
         }
         else if (t<60) {
            res_a += 20;
         }
         else {
            res_a += (t/30+1)*10;
         }

         if (t<60) {
            res_b += 15;
         }
         else if (t<120) {
            res_b += 30;
         }
         else {
            res_b += (t/60+1)*15;
         }
      }
      if (res_a<res_b) {
         System.out.println("Y "+res_a);
      }
      else if (res_a>res_b) {
         System.out.println("M "+res_b);
      }
      else {
         System.out.println("Y M "+res_a);
      }

      scanner.close();
    }
}