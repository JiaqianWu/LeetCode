import java.util.*;
public class GroupAnagrams {
	public List<List<String>> groupAnagrams(String[] strs) {
		if(strs.length == 0) return new ArrayList<List<String>>();
		Map<String,List<String>> m = new HashMap<String, List<String>>();
        for (String s : strs) {
        	char[] a = s.toCharArray();
        	Arrays.sort(a);
        	//System.out.println(a);
        	String key = String.valueOf(a); //Cannot use a.toString(), which took me 20 minutes to find the bug!
        	//String key = a.toString();
        	if(m.containsKey(key)) {
        		m.get(key).add(s);
        		System.out.println(s);
        	}
        	else{
        		List<String> l = new ArrayList<String>();
        		l.add(s);
        		m.put(key,l);
        	}
        }
        return new ArrayList<List<String>> (m.values());
    }
	
	public static void main(String[] args) {
		GroupAnagrams a = new GroupAnagrams();
		//a.groupAnagrams(new String[] {"eat", "tea", "tan", "ate", "nat", "bat"});
        System.out.println(a.groupAnagrams(new String[] {"eat", "tea", "tan", "ate", "nat", "bat"}));
    }
}
