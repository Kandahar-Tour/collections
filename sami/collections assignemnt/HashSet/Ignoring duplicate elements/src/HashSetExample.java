import java.util.;

public class HashSetExample{
    public static void main(String[] args){
        //Creating HashSet and adding elements
        HashSet<string> set=new HashSet<string>();
        set.add("A");
        set.add("B");
        set.add("A");
        set.add("C");
        //Traversing elements
        Iterator<string> itr=set.iterator();
        while(itr.hasNext()){
            System.out.println(itr.next());
        }
    }
}