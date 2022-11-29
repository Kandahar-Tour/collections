public class Exapmle implements Runnable
{
    public static void main(String[] args) {
        Thread E1 = new Thread("Samo1");
        Thread E2 = new Thread("Samo");
        E1.start();
        E2.start();
        System.out.println("Threaeds are following ");
        System.out.println(E1.getName());
        System.out.println(E2.getName());
    }

    @Override
    public void run() {

    }
}
