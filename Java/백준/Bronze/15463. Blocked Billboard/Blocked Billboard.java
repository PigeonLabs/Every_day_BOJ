import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int ans = 0;
        int[][] loc = new int[3][4];
        for (int i = 0; i < 3; i++) {
            StringTokenizer stk = new StringTokenizer(br.readLine());
            for (int j = 0; j < 4; j++) {
                loc[i][j] = Integer.parseInt(stk.nextToken());
            }
        }
        for (int i = 0; i < 2; i++) {
            ans += (loc[i][2] - loc[i][0]) * (loc[i][3] - loc[i][1]);
            int W = Math.min(loc[2][2], loc[i][2]) - Math.max(loc[2][0], loc[i][0]);
            int H = Math.min(loc[2][3], loc[i][3]) - Math.max(loc[2][1], loc[i][1]);
            if (W > 0 && H > 0) {
                ans -= (W * H);
            }
        }
        System.out.println(ans);
    }
}