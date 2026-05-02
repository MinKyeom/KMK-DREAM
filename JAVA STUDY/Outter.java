// public class Outter {
//     // java 7버전
//     public void method1(final int arg){
//         final int localVariable = 1;

//         // arg = 100;
//         // localVariable = 100;

//         class Inner{
//             public void method(){
//                 int result = arg + localVariable;
//             }
//         }
//     }

//     // java 8버전
//     public void method2(int arg){
//         int localVariable = 1;
        
//         // arg = 100;
//         // localVariable = 100;

//         class Inner{
//             public void method(){
//                 int result = arg + localVariable;
//             } 
//         }
//     }
// }

public class Outter{

    String field = "Outer=field";
    void method(){
        System.out.println("Outer-method");
    }

    class Nested{
        String field = "Nested-field";
        void method() {
            System.out.println("Nested-method");
        }

        void print(){
            System.out.println(this.field);
            this.method(); // 중첩 객체 참조
            System.out.println(Outter.this.field); // 바깥 객체 참조
        }
    }
}