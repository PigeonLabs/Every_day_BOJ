import java.util.Scanner;

public class Main {
   public static void main(String[] args) {
      Scanner scanner = new Scanner(System.in);
      int n = scanner.nextInt();
      for (int i=0;i<n;i++) {
         int num = scanner.nextInt();
         if (Integer.toString(num*num).endsWith(Integer.toString(num))) {
            System.out.println("YES");
         }
         else {
            System.out.println("NO");
         }
      }
      scanner.close();
   }
}