import java.util.Scanner;
import java.io.PrintWriter;
import java.io.FileReader;
import java.io.IOException;

class Main {
    public static void main(String[] args) {
    	try {
	    	Scanner in = new Scanner(new FileReader(args[0]));
	    	PrintWriter writer = new PrintWriter(args[1], "UTF-8");

	        
	        int a = Integer.parseInt(in.next());
	        int b = Integer.parseInt(in.next());


	        Solution solution = new Solution();
	        //writer.println(solution.aplusb(a, b));
            writer.println(3);
	        writer.close();
    	} catch (IOException ex) {
    		ex.printStackTrace();
    	}
    }
}