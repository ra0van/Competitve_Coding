#include<stdio.h>

int main(){
    int t;
    scanf("%d",&t);
    while(t--){
        int n,u;
        scanf("%d%d",&n,&u);
        int a[n+1],val,low,high,i;
        for(i=0;i<n+1;i++)
            a[i]=0;
        // printf("%d \n",u);
        for(i=0;i<u;i++){
            scanf("%d%d%d",&low,&high,&val);
            a[low] += val;
            a[high+1] -= val;
            
        }
        
        int prev = 0;
        for(i=0;i<n;i++){
            prev += a[i];
            a[i] = prev;
        }
        
        int q;
        scanf("%d",&q);
        for(i=0;i<q;i++){
            scanf("%d",&val);
            printf("%d \n",a[val]);
        }
        
    }
}