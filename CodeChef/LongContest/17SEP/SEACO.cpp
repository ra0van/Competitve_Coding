#include<stdio.h>

void executeCommand(int *qcount,int q,int up[][3],int i){
    if (up[i][0] == 1)
        qcount[i] += 1;
    else{
        for(int j=up[i][1]-1;j<up[i][2];j++){
            executeCommand(qcount,q,up,j);
        }
    }
    
}

int main(){
    int t;
    scanf("%d",&t);
    while(t--){
        int n,q;
        scanf("%d%d",&n,&q);
        int a[n+1],up[q][3],qcount[q],i,x,y,z;
        
        for(i=0;i<n+1;i++)
            a[i]=0;
        
        for(i=0;i<q;i++){
            qcount[i] = 0;
        }
        
        for(i=0;i<q;i++){
            scanf("%d%d%d",&x,&y,&z);
            up[i][0] = x;
            up[i][1] = y;
            up[i][2] = z;
            
            executeCommand(qcount,q,up,i);
        }
        
        // for(i=0;i<q;i++){
        //     for(int j=0;j<=2;j++){
        //         printf("%d ",up[i][j]);    
        //     }
        //     printf("\n");
        // }
        
        
        // for(i=0;i<q;i++)
        //     printf("%d ",qcount[i]);
        // printf("\n");
        for(i=0;i<q;i++){
            if (qcount[i]>0){
                x = up[i][1]-1;
                y = up[i][2];
                // printf("updating %d %d\n",x,y);
                a[x] += qcount[i];
                a[y] -= qcount[i];
            }
        }
        
        // for(i=0;i<n+1;i++)
        //     printf("%d ",a[i]);
        // printf("\n");
        int prev =0;
        for(i=0;i<n;i++){
            prev += a[i];
            a[i] = prev;
            printf("%d ",a[i]);
        }
        printf("\n");
    }
}