import java.util.*;

public class ValidAnagram {
    public boolean isAnagram(String s, String t) {
        char[] s1 = s.toCharArray();
        Arrays.sort(s1);
        char[] t1 = t.toCharArray();
        Arrays.sort(t1);
        if(String.valueOf(s1).equals(String.valueOf(t1))) return true;
        else return false;
    }
    public static void main(String[] args) throws Exception {
    	ValidAnagram a = new ValidAnagram();
        System.out.println(a.isAnagram("abcd","badc"));
    }
}
