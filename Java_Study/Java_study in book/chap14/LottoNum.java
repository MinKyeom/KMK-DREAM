import java.util.Arrays;
import java.util.Random;
public class LottoNum {
	public static void main(String args[]) {
		Random r = new Random();
		int[] lnum = new int[6];
		int tmp;
		int i = 0;
		a : while(i < 6) {
			tmp = r.nextInt(45)+1;
			for(int j = 0 ; j <= i ; j++) {
				if (tmp == lnum[j])
					continue a;
			}
		lnum[i]=tmp;
		i++;
		}
		System.out.println("이번 주 로또 당첨번호 : "+Arrays.toString(lnum));
	}
}