public class Exception_handlig {

    public static void main(String[] args) {
        try{
            int[] number = {1,2,3,4};
            System.out.println(number[10]);
        }
        catch (Exception e)
        {
            System.out.println("Sami is good boy ");
        }
    }

}
