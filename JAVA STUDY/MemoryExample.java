public class MemoryExample {

    // ==============================
    // [Method Area]
    // 클래스 정보와 함께 static 변수는 Method Area에 저장된다.
    // ==============================
    static int staticValue = 100;

    // ==============================
    // 객체의 인스턴스 변수는 Heap 영역에 저장된다.
    // ==============================
    int instanceValue;

    public MemoryExample(int value) {
        // this는 Heap에 생성된 객체 자신을 가리킨다.
        this.instanceValue = value;
    }

    public static void main(String[] args) {

        // ==============================
        // [Stack 영역]
        // main 메서드가 호출되면 Stack에 main 프레임이 생성된다.
        // ==============================

        int localValue = 10; 
        // 기본형 지역 변수는 Stack에 저장된다.

        MemoryExample obj1 = new MemoryExample(20);
        // obj1 (참조 변수)는 Stack에 저장된다.
        // new MemoryExample(20) 로 생성된 객체는 Heap에 저장된다.
        // instanceValue = 20 도 Heap에 저장된다.

        MemoryExample obj2 = obj1;
        // obj2는 Stack에 저장된다.
        // obj1과 obj2는 Heap의 같은 객체를 참조한다.

        changeValue(obj1);

        System.out.println("localValue: " + localValue);
        System.out.println("obj1.instanceValue: " + obj1.instanceValue);
        System.out.println("staticValue: " + staticValue);
    }

    public static void changeValue(MemoryExample obj) {
        // ==============================
        // changeValue 메서드가 호출되면
        // Stack에 새로운 프레임이 생성된다.
        // ==============================

        obj.instanceValue = 999;
        // obj는 Stack에 저장된 참조 변수
        // instanceValue는 Heap에 있는 객체의 값이 변경된다.

        int temp = 50;
        // temp는 changeValue 메서드의 지역 변수
        // Stack 영역에 저장된다.
    }
}