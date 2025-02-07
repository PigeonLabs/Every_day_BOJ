import java.util.Scanner;

public class Main {
   public static void main(String[] args) {
      Scanner scanner = new Scanner(System.in);
      long n = scanner.nextLong();
      long sum = 0;
      long count = 0;
      long i = 1;
      while (sum < n) {
         if (sum + i <= n) {
            sum += i;
            count++;
            i++;
         } else {
            i = 1;
         }
      }
      System.out.println(count);
      scanner.close();
   }
}
