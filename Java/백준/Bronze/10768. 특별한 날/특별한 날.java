import java.util.Scanner;

public class Main {
   public static void main(String[] args) {
      Scanner scanner = new Scanner(System.in);
      int a = scanner.nextInt();
      int b = scanner.nextInt();
      if (a<2) {
         System.out.println("Before");
      }
      else if (2<a) {
         System.out.println("After");
      }
      else {
         if (b<18) {
            System.out.println("Before");
         }
         else if (18<b) {
            System.out.println("After");
         }
         else {
            System.out.println("Special");
         }
      }
      scanner.close();
   }
}