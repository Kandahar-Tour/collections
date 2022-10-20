import java.util.*;
public class HashSetExample{
    public static void main(String args[]){
        ArrayList<string> list=new ArrayList<string>();
        list.add("A");
        list.add("B");
        list.add("C");

        HashSet<string> set=new HashSet(list);
        set.add("D");
        Iterator<string> i=set.iterator();
        while(i.hasNext())
        {
            System.out.println(i.next());
        }
    }
}