import java.util.*;

public class AdjacentCell {
	private int len=0;
	public boolean exist(char[][] board, String word) {
		int rowSize = board.length;
		int colSize = board[0].length;
		char[][] newBoard = new char[rowSize+2][rowSize+2];
		for (int i=0; i < rowSize; i++) {
			for (int j=0; j < colSize; j++) {
				newBoard[i+1][j+1] = board[i][j];
			}
		}
		ArrayList<Boolean> result = new ArrayList<Boolean>();
		for(int j=1; j < rowSize+2; j++) {
			for(int k=1; k < colSize+2; k++) {
				if (result.add(searchAround(board,word, 0, j, k))){
					return true;
				}
			}
		}
		boolean flag = false;
		for (boolean i : result) {
			if (i) return true;
		}
		return flag;
    }
	
	public boolean searchAround(char[][] board, String word,int index,int row, int col) {
		if(len>word.length()) {
			char w = word.charAt(len);
			if (row-1<0||col-1<0||row+1>board.length||col+1>board[0].length) {
				return false;
			}
			if (board[row][col] == w) {
				boolean a = searchAround(board,word, word.charAt(++len), row-1, col-1);
				boolean b = searchAround(board,word, word.charAt(++len), row-1, col+1);
				boolean c = searchAround(board,word, word.charAt(++len), row+1, col-1);
				boolean d = searchAround(board,word, word.charAt(++len), row+1, col+1);
				return a||b||c||d;
			}
			else { return false;}
		}
		else return false;	
	}
}
