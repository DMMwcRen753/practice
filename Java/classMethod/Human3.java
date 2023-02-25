package classMethod.human;

public class Human3 {
  public String name;
  public int age;
  public String profession;

  public Human3() {
    this.name = "山田";
    this.age = 20;
    this.profession = "プログラマー";
  }

  public String getprofile() {
    return "年齢は" + this.age + "、職業は" + this.profession;
  }

  public void greet(String friend) {
    if (friend == null) {
      System.out.println("挨拶する友達がわかりません！");
      return;
    }
    System.out.println(friend + "さん、こんにちは！");
  }
}
