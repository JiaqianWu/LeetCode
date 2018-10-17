
public class LongestPalindrome {
	private int a, b;
	public void search(String s, int start, int end) {
		while (start >= 0 && end < s.length() && s.charAt(start) == s.charAt(end)) {
			start=start-1;
			end=end+1;
		}
		if (b < end - start - 1) {
			a = start + 1;
			b = end - start - 1;
		}
	}

	public String longestPalindromes(String s) {
		int len = s.length();
		if (len < 2)
			return s;
	    for (int i = 0; i < len-1; i++) {
	     	search(s, i, i);  
	     	search(s, i, i+1); 
	    }
	    return s.substring(a, a + b);
	}
	public static void main(String[] args) {
		LongestPalindrome a = new LongestPalindrome();
        System.out.println(a.longestPalindromes("abcbada"));
    }	
}

