import java.util.Scanner;

public class Main {
   public static int love(int[] arr) {
      if (arr.length==2) {
         return arr[0]*10+arr[1];
      }
      int newarr[] = new int[arr.length-1];
      for (int i = 0; i < arr.length-1; i++) {
         newarr[i] = (arr[i] + arr[i+1])%10;
      }
      return love(newarr);
   }

   public static void main(String[] args) {
      Scanner scanner = new Scanner(System.in);
      int[] strokes = {
         3, 2, 1, 2, 4, 3, 1, 3, 1, 1,
         3, 1, 3, 2, 1, 2, 2, 2, 1, 2,
         1, 1, 1, 2, 2, 1
      };

      int a = scanner.nextInt();
      int b = scanner.nextInt();
      String name1 = scanner.next();
      String name2 = scanner.next();
      
      StringBuilder name = new StringBuilder();
      int len = Math.max(name1.length(), name2.length());
      for (int i = 0; i < len; i++) {
         if (i < name1.length()) {
            name.append(name1.charAt(i));
         }
         if (i < name2.length()) {
            name.append(name2.charAt(i));
         }
      }

      int arr[] = new int[name.length()];
      for (int i = 0; i < name.length(); i++) {
         arr[i] = strokes[name.charAt(i)-65];
      }

      System.out.println(love(arr)+"%");
      
      scanner.close();
   }
}
