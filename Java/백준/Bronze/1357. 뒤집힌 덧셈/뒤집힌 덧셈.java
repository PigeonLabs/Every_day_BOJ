import java.util.Scanner;

public class Main {
   public static void main(String[] args) {
      Scanner scanner = new Scanner(System.in);
      int a = Integer.parseInt(new StringBuffer(scanner.next()).reverse().toString());
      int b = Integer.parseInt(new StringBuffer(scanner.next()).reverse().toString());
      int res = Integer.parseInt(new StringBuffer(Integer.toString(a+b)).reverse().toString());
      System.out.println(res);
      scanner.close();
   }
}