package project;
import java.util.*;

public class 나도알바퇴사하고싶다 {
   static int n; //전역변수 어디서나 참조 가능한 n (퇴직까지 남은 일)
   static int [] t; //상담에 필요한 날
   static int [] p; // 수익
   static int maxp; //최대수익 

public static void x(int i, int totalp) { //아래 사용한 x의 구조를 정의 받아오는 첫 값은 0, 0
   if(i >= n) { //n값보다 i가 크다면
      if(maxp <totalp) {
         maxp = totalp;//maxp 값이.
      }
      return;
      
   }
   
   if(i + t[i] <= n) {
      x(i+t[i], totalp+p[i]);
   }
   if(i + 1 <= n) {
      x(i + 1, totalp);
   }
}

   public static void main(String[] args) {
      Scanner scanner = new Scanner(System.in); // 입력을 받기위한 scanner 선언
      n = scanner.nextInt(); //정수형으로 입력을 받음
      int totalp = 0; //초기 값 0      
      t = new int [n]; // n의 크기만큼 리스트 선언
      p = new int [n];
      
      for(int i = 0; i < n; i++) { //for문으로 반복 입력
         t[i] = scanner.nextInt();
         p[i] = scanner.nextInt();
      }
      System.out.println(maxp);
      x(0,0); //필요한 입력을 모두 받고 계산을 위한 코드로 연결 
      System.out.println(maxp);//x의 결과 출력
   }

}