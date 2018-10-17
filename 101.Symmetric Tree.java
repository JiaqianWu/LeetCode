
public class IsSymmetric {
	public class TreeNode {
		int val;
		TreeNode left;
		TreeNode right;
		TreeNode(int x) { val = x; }
	}
	public boolean solution(TreeNode root) {
        if(root == null) {
            return true;
        }
        TreeNode a = root.left;
        TreeNode b = root.right;
        return symmetricNode(a,b);
        
    }
    public boolean symmetricNode(TreeNode a, TreeNode b) {
    	if (a == null && b == null) {
            return true;
        }
    	
        if (a.val == b.val) {
            if (a != null && b != null) {
                return(a.val == b.val && symmetricNode(a.left,b.right) && symmetricNode(a.right,b.left));
            }
            else {
                return false;
            }
        }
        else {
        	return false;
        }
    }
}
