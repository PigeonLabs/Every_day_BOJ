import java.util.Scanner;

public class Main {
   public static void main(String[] args) {
      Scanner scanner = new Scanner(System.in);
      int n = scanner.nextInt();
      for (int i=0;i<n;i++) {
         for (int j=0;j<i;j++) {
            System.out.print(" ");
         }
         for (int j=0;j<(2*n-1-2*i);j++) {
            System.out.print("*");
         }
         System.out.println("");
      }
      for (int i=1;i<n;i++) {
         for (int j=0;j<n-i-1;j++) {
            System.out.print(" ");
         }
         for (int j=1;j<=(2*i+1);j++) {
            System.out.print("*");
         }
         System.out.println("");
      }
      scanner.close();
   }
}