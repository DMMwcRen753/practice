public class ClassMethod2 {
  public static void main(String[] args) {
    Human2 yamada = new Human2();
    System.out.println("名前は" + yamada.name + "で、年齢は" + yamada.age + "歳です。");

    Human2 sato = new Human2("佐藤", 25);
    System.out.println("名前は" + sato.name + "で、年齢は" + sato.age + "歳です。");
  }
}
