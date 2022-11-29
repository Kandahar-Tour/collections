public class Threaading extends Thread{
    public void run()
    {
        System.out.println("Sami is from kandhar ");
    }

    public static void main(String[] args)
    {
     Threaading sami = new Threaading();
        sami.run();


    }
}
