import java.util.Scanner;

public class Main {
   public static void main(String[] args) {
      Scanner scanner = new Scanner(System.in);
      int n = scanner.nextInt();
      int res = 0;
      for (int i=0;i<n;i++) {
         String t = scanner.next();
         int p = scanner.nextInt();
         String[] parts = t.split(":");
         int a = Integer.parseInt(parts[0]);
         int b = Integer.parseInt(parts[1]);
         int ae = a+(b+p)/60;
         int be = (b+p)%60;
         if (7<=a && a<19 && 7<=ae && ae<19) {
            res += ((ae-a)*60+(be-b))*10;
         }
         else if (a<7 && 7<=ae) {
            res += ((7-a)*60-b)*5+((ae-7)*60+be)*10;
         }
         else if (a<19 && 19<=ae) {
            res += ((19-a)*60-b)*10+((ae-19)*60+be)*5;
         }
         else {
            res += ((ae-a)*60+(be-b))*5;
         }
      }
      System.out.println(res);
      scanner.close();
   }
}
