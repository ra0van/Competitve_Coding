#include <iostream>
using namespace std;

bool findArea(int a1,int b1,int a2,int b2,int a,int b){
	int d_a1 = a1+a2;
	int d_b1 = b1+b2;
	
	int d_a2 = a1+b2;
	int d_b2 = b1+a2;
	
	if(d_a1<=a && b1<=b && b2<=b){
		//cout<<d_a1<<" "<<d_b1;
		return true;
	}
	else if(d_a1<=b && b1<=a && b2<=a){
		//cout<<d_a1<<" "<<d_b1;
		return true;
	}
	else if(d_b1<=a && a1<=b && a2<=b){
		//cout<<d_a1<<" "<<d_b1;
		return true;
	}
	else if(d_b1<=b && a1<=a && a2<=a){
		//cout<<d_a1<<" "<<d_b1;
		return true;
	}
	else if(d_a2<=a && b1<=b && a2<=b){
		//cout<<d_a1<<" "<<d_b1;
		return true;
	}
	else if(d_a2<=b && b1<=a && a2<=a){
		//cout<<d_a1<<" "<<d_b1;
		return true;
	}
	else if(d_b2<=a && a1<=b && b2<=b){
		//cout<<d_a1<<" "<<d_b1;
		return true;
	}
	else if(d_b2<=b && a1<=a && b2<=a){
		//cout<<d_a1<<" "<<d_b1;
		return true;
	}
	return false;
}


int main() {
	// your code goes here
	
	int a,b;
	cin>>a>>b;
	int v = a*b;
	
	int a1,b1;
	cin>>a1>>b1;
	int v1=a1*b1;
	
	int a2,b2;
	cin>>a2>>b2;
	int v2=a2*b2;
	
	if(v < v1+v2){
		cout<<"NO"<<endl;
	}
	else{
		if(findArea(a1,b1,a2,b2,a,b)){
			cout<<"YES"<<endl;
		}
		else
			cout<<"NO"<<endl;
	}
	
	
	
	return 0;
}