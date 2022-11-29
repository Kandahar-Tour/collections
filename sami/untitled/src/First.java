public class First {


    public static void main(String[] args) {

        First sami= new First(2,4,5);
         sami.mansor(2, 4);
        sami.sami();
        shakir dod = new shakir(5);

    }
    First ( int h , int s)
    {
        System.out.println("equal "+ h+s);
    }

    First ( int h , int s, int g)
    {
        System.out.println("equal "+ h+s+g);
    }
     void mansor(int s , int a )
     {
         System.out.println(s+a);

     }



    void sami()
    {
        System.out.println("HI shakir ");
    }


}
class shakir {

    shakir (){
        System.out.println("shakir is a dog ");
    }
    shakir (int a){
        this();
        System.out.println("shakir is a dog ");

    }
}
