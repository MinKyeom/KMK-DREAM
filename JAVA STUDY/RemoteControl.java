public interface RemoteControl {

    public int MAX_VOLUME = 10;
    public int MIN_VOLUME = 0; 


    // 메소드 선언부이며, 추상 메소드
    public void turnOn();
    public void turnOff();
    public void setVolume(int volume);
}


