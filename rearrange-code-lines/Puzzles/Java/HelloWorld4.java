public class HelloWorld4 {
    public static void main(String[] args) {
        String str = "Java is fun to learn";
        int count = 0;

        for (int i = 0; i < str.length(); i++) {
            if (str.charAt(i) == ' ')
                count++;
        }

        System.out.println("Spaces: " + count);
    }
}
