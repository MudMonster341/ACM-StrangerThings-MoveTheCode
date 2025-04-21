public class HelloWorld12 {
    public static void main(String[] args) {
        int num = 3210;
        System.out.print("Digits in reverse: ");
        while (num > 0) {
            System.out.print(num % 10 + " ");
            num /= 10;
        }
    }
}
