import java.util.Scanner;

public class Main {
   public static void main(String[] args) {
      Scanner scanner = new Scanner(System.in);
      String a = scanner.next();
      String b = scanner.next();
      long res = 0;
      for (int i=0;i<a.length();i++) {
         for (int j=0;j<b.length();j++) {
            res += (a.charAt(i)-'0')*(b.charAt(j)-'0');
         }
      }
      System.out.println(res);
      scanner.close();
   }
}