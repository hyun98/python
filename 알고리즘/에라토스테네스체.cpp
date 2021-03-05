#include <stdio.h>

int era(int N);
int main(){
	int t,i,n;
	for(i=0;i<t;i++){
		scanf("%d",&n);
	}
	return 0;
}
int era(int N){
	int i, j, count=0;
	int che[250000]={0, };
	che[1] = 1;
	for(i=2;i<=2*N;i++){
		if(che[i]==0){
			if(i>N){
				count++;
			}
			for(j=1;i*j<=2*N;j++){
				che[i*j]=1;
			}
		}
	}
}

int gold(int N){
	int i,j;
	for(i=0;i<)
}

