

public class DivideTwoIntegers {
	public int divide(int dividend, int divisor) throws Exception {
		if (divisor == 0) {
			throw new Exception("Devisor Zero Error!");
		}
		if (dividend == 0) {
			return 0;
		}
		if(dividend == -2147483648 && divisor == -1){
			return 2147483647;
		}

		if (dividend > Integer.MAX_VALUE || dividend < Integer.MIN_VALUE) return Integer.MAX_VALUE;
		int sign = (dividend > 0 && divisor > 0) || (dividend < 0 && divisor < 0) ? 1 : -1;
		long dividendNew = Math.abs((long)dividend);
		long divisorNew = Math.abs((long)divisor);
        int quotient = (int) half(dividendNew, divisorNew)[0];
        int remainder = (int) half(dividendNew, divisorNew)[1];
        while(remainder >= divisorNew) {
        	int q = (int) half(remainder,divisorNew)[0];
        	remainder = (int) half(remainder,divisorNew)[1];
        	quotient += q;
        }
        return (sign == 1) ? quotient : -quotient;
    }
	
	private long[] half(long dividend, long divisor) {
		int quotient = 1;
		if (dividend < divisor) {
			quotient = 0;
		}
		if (dividend == divisor) return new long[] {1,0};
        while(dividend - divisor - divisor >= 0) {
        	quotient = quotient + quotient;
        	divisor = divisor + divisor;
        }
        return new long[] {quotient, dividend - divisor};
	}
	public static void main(String[] args) throws Exception {
		DivideTwoIntegers a = new DivideTwoIntegers();
        System.out.println(a.divide(-2147483648,1));
    }
}
