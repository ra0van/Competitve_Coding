#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--){
		int x=0,y=0;
		
		cin>>x>>y;	
	
		int a[x][y];
		for (int i=0;i<x;i++){
			for(int j=0;j<y;j++){
				cin>>a[i][j];
			}
		}
	
		
		for(int i=1;i<x;i++){
			for(int j=0;j<y;j++){
				int m1=0,m2=0,m3=0;
				m1 = a[i-1][j];
				
				if(j-1>=0){
					m2 = a[i-1][j-1];
				}
				
				if(j+1<=y-1){
					m3=a[i-1][j+1];
				}
				
				int v = (m1>m2)? (m1>m3?m1:m3):(m2>m3?m2:m3);
				// cout<<v<<endl;
				a[i][j] += v;
			}
		}
		int m = a[x-1][0];
		for(int i=0;i<y;i++){
			if (a[x-1][i] > m){
				m = a[x-1][i];
			}
			// cout<<a[x-1][i]<<" ";
		}
		cout<<m<<endl;
	}
	
	return 0;
}
