import java.util.Scanner;

public class Main {
   public static void main(String[] args) {
      Scanner scanner = new Scanner(System.in);
      int res = 0;
      int mn = 10000;
      int n = scanner.nextInt();
      int pv = scanner.nextInt();
      int cr;
      for (int i=1;i<n;i++) {
         cr = scanner.nextInt();
         if (pv<cr) {
            mn = mn<pv?mn:pv;
            pv = cr;
         }
         else {
            res = res<pv-mn?pv-mn:res;
            mn = 10000;
         }
         pv = cr;
      }
      res = res<pv-mn?pv-mn:res;
      System.out.println(res);
      scanner.close();
   }
}