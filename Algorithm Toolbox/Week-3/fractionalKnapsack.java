import java.util.*;

public class FractionalKnapsack {
    static class ItemValue{
        Double cost;
        double wt, val, ind;

        public ItemValue(int wt, int val, int ind){
            this.wt = wt;
            this.val = val;
            this.ind = ind;
            cost = (double)val/wt;
        }
    }
    private static double getOptimalValue(int capacity, int[] values, int[] weights) {
        ItemValue[] kanp_val = new ItemValue[weights.length];

        //Adding items to the ItemValue class declared above
        for(int i=0; i<weights.length; i++){
            kanp_val[i] = new ItemValue(weights[i],values[i],i);
        }

        //Sorting the items value by value
        Arrays.sort(kanp_val, new Comparator<ItemValue>() {
            @Override
            public int compare(ItemValue o1, ItemValue o2) {
                return o2.cost.compareTo(o1.cost);
            }
        });

        double value = 0d;

        for(ItemValue i: kanp_val){
            int currentWeight = (int) i.wt;
            int currentValue = (int) i.val;

            if(capacity - currentWeight >= 0){
                capacity = capacity - currentWeight;
                value += currentValue;
            }
            else
            {
                double fraction = ((double)capacity/(double)currentWeight);
                value += (currentValue*fraction);
                capacity = (int) (capacity - (currentWeight*fraction));
                break;
            }
        }
        return value;
    }

    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int capacity = scanner.nextInt();
        int[] values = new int[n];
        int[] weights = new int[n];
        for (int i = 0; i < n; i++) {
            values[i] = scanner.nextInt();
            weights[i] = scanner.nextInt();
        }
        System.out.println(getOptimalValue(capacity, values, weights));
    }
}
