import java.util.Scanner;

public class Main {
   public static void main(String[] args) {
      Scanner scanner = new Scanner(System.in);
      int n = scanner.nextInt();
      int m = scanner.nextInt();
      int temp = m;
      int res = 1;
      if (n==0) {
         System.out.println(0);
      }
      else {
         for (int i=0;i<n;i++) {
            int t = scanner.nextInt();
            if (t<=temp) {
               temp -= t;
            }
            else {
               temp = m-t;
               res++;
            }
         }
         System.out.println(res);
      }
      scanner.close();
   }
}
