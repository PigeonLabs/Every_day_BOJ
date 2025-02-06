import java.util.Scanner;

public class Main {
   public static int Add_A(char arr[], int c, int len) {
      if (arr[c]=='X' && arr[c+1]=='X' && arr[c+2]=='X' && arr[c+3]=='X') {
         for (int i=c;i<c+4;i++) {
            arr[i] = 'A';
         }
         return 1;
      }
      return 0;
   }

   public static int Add_B(char arr[], int c, int len) {
      if (arr[c]=='X' && arr[c+1]=='X') {
         for (int i=c;i<c+2;i++) {
            arr[i] = 'B';
         }
         return 1;
      }
      return 0;
   }

   public static void main(String[] args) {
      Scanner scanner = new Scanner(System.in);
      char[] arr = scanner.nextLine().toCharArray();
      int len = arr.length;
      int count = 0;

      while (true) {
         if (count <= len-4) {
            if (Add_A(arr, count, len)==1) {
               count += 4;
               continue;
            }
            else if (Add_B(arr, count, len)==1) {
               count += 2;
               continue;
            }
         }
         else if (count <= len-2) {
            if (Add_B(arr, count, len)==1) {
               count += 2;
               continue;
            }
         }
         count++;
         if (count >= len) break;
      }
      int res = 0;
      for (int i=0;i<len;i++) {
         if (arr[i]=='X') {
            res = 1;
            break;
         }
      }
      if (res==1) {
         System.out.println(-1);
      }
      else {
         System.out.println(new String(arr));
      }
      scanner.close();
   }
}