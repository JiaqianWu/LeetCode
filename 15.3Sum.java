import java.util.*;

public class TripletsSum {
/*    public List<List<Integer>> triplet(int[] nums) {
    	if(nums.length == 0) return new ArrayList<List<Integer>>();
    	ArrayList<List<Integer>> result = new ArrayList<List<Integer>>();
        Arrays.sort(nums);
        HashSet<List<Integer>> triplets = new HashSet<List<Integer>>();
        for (int i = 0; i<nums.length; i++) {
            for (int j = i+1; j<nums.length; j++) {
                for (int k = j+1; k<nums.length; k++) {
                    if(nums[i]+nums[j]+nums[k] ==0) {
                        triplets.add(new ArrayList<Integer>(Arrays.asList(nums[i],nums[j],nums[k])));
                    }
                }
                    
            }
        }
        for(List<Integer> i : triplets) {
        	result.add(i);
        }
        return result;
    }*/
    
    public List<List<Integer>> triplet(int[] nums) {
    	if(nums.length == 0) return new ArrayList<List<Integer>>();
    	ArrayList<List<Integer>> result = new ArrayList<List<Integer>>();
        Arrays.sort(nums);
        HashSet<List<Integer>> triplets = new HashSet<List<Integer>>();
        for (int i = 0; i<nums.length-2; i++) {
        	if (nums[i] == nums[i+1]) continue;
        	int j = i + 1;
        	int k = nums.length-1;
        	while(j < k) {
        		int sum = nums[i]+nums[j]+nums[k];
            	if (sum == 0) {
            		triplets.add(new ArrayList<Integer>(Arrays.asList(nums[i],nums[j],nums[k])));
            		j++;
            		k--;
            	}
            	else if (sum < 0) j++;
            	else k--;
        	}
        }
        for(List<Integer> i : triplets) {
        	result.add(i);
        }
        return result;
    }
    
    public static void main(String[] args) {
        TripletsSum a = new TripletsSum();
        System.out.println(a.triplet(new int[] {-1,0,1,2,-1,-4}));
    }
    
}