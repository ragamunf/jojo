import java.util.Scanner;

public class SecondTask {
    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        System.out.println("Введите имя: ");
        String name = in.nextLine();
        var rightName = name.toUpperCase().charAt(0) + name.substring(1).toLowerCase();
        System.out.printf("Привет, %s!", rightName);
        in.close();

    }
}
