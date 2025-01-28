import java.util.Scanner;

public class Main {
   public static void main(String[] args) {
      Scanner scanner = new Scanner(System.in);
      int n = scanner.nextInt();
      if (n%2==1) {
         System.out.println((n/2+1)*(n/2+2));
      }
      else {
         System.out.println((n/2+1)*(n/2+1));
      }
      scanner.close();
   }
}