public class Chapter07 {
    public static void main(String[] args) {
        int distance = 2;
        if (distance <= 5) {
            System.out.println("とても近い");
        } else if (distance <= 10) {
            System.out.println("近い");
        } else if (distance <= 15) {
            System.out.println("遠い");
        } else {
            System.out.println("とても遠い");
        }
        
        String color = "red";
        switch (color) {
            case "red":
                System.out.println("赤");
                break;
            case "blue":
                System.out.println("青");
                break;
            case "yellow":
                System.out.println("黄色");
                break;
            default:
                System.out.println("信号の色ではない");
        }
    }
}