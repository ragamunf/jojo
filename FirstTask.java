import java.util.Scanner;

public class FirstTask {
    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);

        System.out.println("Введите первую строку: ");
        String first = in.nextLine();
        System.out.println("Введите вторую строку: ");
        String second = in.nextLine();

        in.close();

        System.out.println(isEndedWith(first, second));

    }

    static boolean isEndedWith(String first, String second) {
        return first.endsWith(second);
    }
}