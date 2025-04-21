public class HelloWorld5 {
    public static void main(String[] args) {
        int num = 121, reversed = 0, original = num;

        while (num != 0) {
            reversed = reversed * 10 + num % 10;
            num /= 10;
        }

        if (original == reversed)
            System.out.println(original + " is a palindrome");
        else
            System.out.println(original + " is not a palindrome");
    }
}
