public class HelloWorld6 {
    public static void main(String[] args) {
        String text = "JavaRocks";
        System.out.println("Characters at even positions:");
        for (int i = 0; i < text.length(); i += 2) {
            System.out.println(text.charAt(i));
        }
    }
}
