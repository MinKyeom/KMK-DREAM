package school_4_2_1;

class Account {
	  private int total = 0;
	  synchronized void deposit() {
	    total = total + 1000;
	  }
	  int gettotal() {
	    return total;
	  }
	}
	class Customer extends Thread {
	  Account same_a; 
	  Customer(Account a, String s) {
	    same_a = a;
	    setName(s);
	  } 
	  public void run() {
	    for(int i = 1; i <= 200 ; i++) {
	      System.out.println(getName() + " : " + i +"번째");
	      same_a.deposit();
	      if (same_a.gettotal() >= 500000) break;
	    }
	  }
	}
	public class week12homework2 {
	  public static void main(String args[])throws Exception {
	    Account same_account = new Account();  
	    Customer donator1 = new Customer(same_account,"1번째 성금자");
	    Customer donator2 = new Customer(same_account,"2번째 성금자");
	    Customer donator3 = new Customer(same_account,"3번째 성금자");
	    Customer donator4 = new Customer(same_account,"4번째 성금자");
	    Customer donator5 = new Customer(same_account,"5번째 성금자");
	    donator1.start();
	    donator2.start();
	    donator3.start();
	    donator4.start();
	    donator5.start();
	    donator1.join();
	    donator2.join();
	    donator3.join();
	    donator4.join();
	    donator5.join();
	    System.out.println("성금 총액은 : " + same_account.gettotal());
	  }
	}