#include <iostream>
using namespace std;

int main(){
	float arr[277];
	arr[0] = 0.0;
	int i=1;
	for(i=1;;i++){
		arr[i] = arr[i-1] + 1.00/(i+1);
		if(arr[i]>=5.20)
			break;

	}

	while(1){
		float num;
		cin>>num;
		if(num==0.0)
			break;

		for(i=1;;i++){
			if(arr[i]>=num)
				break;
		}

		cout<<i<<" card(s)"<<endl;
	}
}
