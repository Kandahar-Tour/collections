
public class Mythread implements Runnable {
    public void Run()
    {
        System.out.println("Sami");
    }
    public static void main(String[] args) {
        System.out.println("Sami");
        Thread t = new Thread(new Mythread());
        t.start();
    }

}
