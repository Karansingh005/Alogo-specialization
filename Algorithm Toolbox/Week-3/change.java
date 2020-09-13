import java.util.Scanner;

public class Change {
    private static int getChange(int m) {
        int count = 0, remainder=m, local=0;
        if (remainder>=10){
            count += remainder/10;
            remainder -= remainder%10;
        }
        if (remainder>=5){
            count += remainder/5;
            remainder -= remainder%5;
        }
        else
        {
            count += remainder;
        }
        return count;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int m = scanner.nextInt();
        System.out.println(getChange(m));

    }
}
