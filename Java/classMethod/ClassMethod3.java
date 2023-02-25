package classMethod;

import classMethod.human.Human3;

public class ClassMethod3 {
  public static void main(String[] args) {
    Human3 yamada = new Human3();

    System.out.println("私の名前は" + yamada.name + "です。");
    String.profile = yamada.getprofile();
    System.out.println(profile + "です。");

    yamada.greet("田辺");
    yamada.greet(null);
  }
}
