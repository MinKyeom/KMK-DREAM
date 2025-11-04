package src.Java_Basic;

public class 2022_03_20 {

  int r = 0;
  
  for ( int i = 1; i<999; i++ ){
    if ( i%3 ==0 && i%2 == 0)
    r=i;
  }
  System.out.print(r);
}
