public class Enca {

    private int id ;
    private String name ;
    private int age ;


    public String getNAme()
    {
        return name;
    }
    public int Getid ()
    {
        return id;
    }
    public int Getage ()
    {
      return age;
    }

    public int Setage(int NEwage )
    {
    age =NEwage;
    }
    public int setId(int newid )
    {
        id =newid;
    }
    public String setName(String NewNAme)

    {
        name=NewNAme;
    }

    public static void main(String[] args) {
        Enca sami = new Enca();
        sami.setId(12);
        sami.setName("Samiullah rasas");
        sami.Setage(34);

        System.out.println("Name "+sami.getNAme() + "Id "+sami.getId() + "Age "+ sami.getNAme());
    }
}