
import classMethod.human.Human2;

public class ClassMethod2 {
  public static void main(String[] args) {
    Human2 yamada = new Human2();
    System.out.println("名前は" + yamada.name + "で年齢は" + yamada.age + "です");

    Human2 sato = new Human2("佐藤", 25);
    System.out.println("名前は" + sato.name + "で年齢は" + sato.age + "です");
  }
}
