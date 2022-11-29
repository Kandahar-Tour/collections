public class Abs_Enc {
    public static void main(String[] args) {
        System.out.println("Sami");
        car sami = new suzzaki();
        sami.accelarat();
    }

}

abstract class car{
    abstract void accelarat();

}

class suzzaki extends car{
    void accelarat()
    {
        System.out.println("Sami jo");
    }
}
