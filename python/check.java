import java.io.*;
import java.math.*;
import java.text.*;
import java.util.*;
import java.util.regex.*;

public class Solution {

    /*
     * Complete the runningMedian function below.
     */
    static double[] runningMedian(int[] a) {
        /*
         * Write your code here.
         */
        
        int N = a.length;
        double[] medians = new double[N];
        Queue<Integer> maxPQ = new PriorityQueue<>(N/2 + 1, Collections.reverseOrder());
        Queue<Integer> minPQ = new PriorityQueue<>(N/2 + 1);
        double median = 0;
        for(int i = 0; i < a.length; i++){
            if (a[i] <= median) {
                        maxPQ.add(a[i]);
                } else {
                        minPQ.add(a[i]);
                }

                if (minPQ.size() > maxPQ.size()+1) {
                        maxPQ.add(minPQ.poll());
                        minPQ.poll();
                }
                if (maxPQ.size() > minPQ.size()+1) {
                        minPQ.add(maxPQ.poll());
                        maxPQ.poll();
                }

                if (minPQ.size() == maxPQ.size()) {
                    
                    median = (double)(maxPQ.peek() + minPQ.peek())/2.0;
                } else if(minPQ.size() > maxPQ.size()) {
                        median = (double)minPQ.peek();
                } else if (minPQ.size() < maxPQ.size()) {
                        median = (double)maxPQ.peek();
                }
                medians[i] = median;
        }
        return medians;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int aCount = Integer.parseInt(scanner.nextLine().trim());

        int[] a = new int[aCount];

        for (int aItr = 0; aItr < aCount; aItr++) {
            int aItem = Integer.parseInt(scanner.nextLine().trim());
            a[aItr] = aItem;
        }

        double[] result = runningMedian(a);
        for (int resultItr = 0; resultItr < result.length; resultItr++) {
            bufferedWriter.write(String.valueOf(result[resultItr]));

            if (resultItr != result.length - 1) {
                bufferedWriter.write("\n");
            }
        }

        bufferedWriter.newLine();

        bufferedWriter.close();
    }
}
