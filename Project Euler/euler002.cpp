// https://www.hackerrank.com/contests/projecteuler/challenges/euler002
// https://projecteuler.net/problem=2
#include <iostream>
using namespace std;

int main(){
    int t;
    cin>>t;
    while(t--){
        long n;
        long c,a=1,b=1;
        cin>>n;
        long long sum=0;
                    c=b;
            b=a+b;
            a=c;
        while(b<=n){
            if(b%2==0) sum+=b;
            c=b;
            b=a+b;
            a=c;
        }
        cout<<sum<<endl;
    }
}