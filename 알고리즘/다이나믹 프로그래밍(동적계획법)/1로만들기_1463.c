#include <stdio.h>
//미완성임
 
int main(){
	int N, temp, t=0;
	scanf("%d",&N);

	if(N==1){
		printf("0");
		return 0;
	}
	while(N!=1){
		
		if(N%3==0){
			N/=3;
			t+=1;
			temp==0;
		}
		else if((N-1)%3==0 && temp==0){
			N=(N-1)/3;
			t+=2;
			temp==0;
		}
		else if(N%2==0){
			N/=2;
			t++;
			temp==0;
		}
		else{
			N--;
			t++;
			temp++;
		}
	}
	printf("%d",t); 
	
	return 0;
}
