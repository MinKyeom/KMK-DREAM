package school_4_2_1;

public class week11homework1 {
	public static void main(String[] args) {
		int lotto[] = new int [6];
		
     	  	
		for(int i=0; i<6; i++) {
			lotto[i] = (int)(Math.random() * 45) + 1;
            
       		  	
			for(int j=0; j<i; j++) {
				if(lotto[i] == lotto[j]) {
					i--;
					break;
				}
			}
		}
	System.out.print("�ζ� ��ȣ: ");
	
  	 // ��ȣ ���
	for(int i=0; i<6; i++) {
		System.out.print(lotto[i] + " ");
	}	
	}
}
