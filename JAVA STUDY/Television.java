public class Television implements RemoteControl {

    private int volume;

    public void turnOn(){
        System.out.println("on");
    }

    public void turnOff(){
        System.out.println("off");
    }

    //public void setVolume(int volume);

    public void setVolume(int volume){
        System.out.println(this.volume);
        System.out.println(volume);
    }

}

