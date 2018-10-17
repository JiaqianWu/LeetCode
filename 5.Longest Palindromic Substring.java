import java.util.*;
public class LongestSubstring {
    public int lengthOfLongestSubstring(String s) {
    	int max = 0;
    	HashSet<Character> charSet = new HashSet<Character>();
    	if(s.length()==1) {
    		return 1;
    	}
        for(int i=0; i < s.length()-1;i++ ) {
        	charSet.add(s.charAt(i));
        	for(int j=i+1; j<s.length();j++) {
        		if (charSet.contains(s.charAt(j))) {
        			if(j-i > max) {
        				max = j-i;
        			};
        			charSet = new HashSet<Character>();
        			break;
        		}
        		if (j == s.length()-1) {
        			if(j-i+1 > max) {
        				max = j-i+1;
        			};
        			break;
        		}
        		charSet.add(s.charAt(j));
        	}
        }
        return max;
    }
    
    public class Solution1 {
        public int lengthOfLongestSubstring(String s) {
            int n = s.length();
            int ans = 0;
            for (int i = 0; i < n; i++)
                for (int j = i + 1; j <= n; j++)
                    if (allUnique(s, i, j)) ans = Math.max(ans, j - i);
            return ans;
        }

        public boolean allUnique(String s, int start, int end) {
            Set<Character> set = new HashSet<>();
            for (int i = start; i < end; i++) {
                Character ch = s.charAt(i);
                if (set.contains(ch)) return false;
                set.add(ch);
            }
            return true;
        }
    }
    
    //slide window
    public class Solution2 {
	    public int lengthOfLongestSubstring(String s) {
	        int n = s.length(), ans = 0;
	        Map<Character, Integer> map = new HashMap<>(); // current index of character
	        // try to extend the range [i, j]
	        for (int j = 0, i = 0; j < n; j++) {
	            if (map.containsKey(s.charAt(j))) {
	                i = Math.max(map.get(s.charAt(j)), i);
	            }
	            ans = Math.max(ans, j - i + 1);
	            map.put(s.charAt(j), j + 1);
	        }
	        return ans;
	    }
    }
    
    
    
    
    public static void main(String[] args) {
    	LongestSubstring a = new LongestSubstring();
    	System.out.println(a.lengthOfLongestSubstring("dvdf"));
    }
}

