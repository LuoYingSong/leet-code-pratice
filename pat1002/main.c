#include <stdio.h>

int main() {
    int a,b;
    float c;
    float d[1000] = {0.0};
    int total = 0;
    int key[100];
    float value[100];
    for (int i = 0; i < 2; ++i) {
        scanf("%d",&a);
        for (int j = 0; j < a; ++j) {
            scanf(" %d",&b);
            scanf(" %f",&c);
            d[b] = d[b] + c;
        }
    }
    for(int i = 999;i>=0;i--){
        if (d[i]){
            key[total] = i;
            value[total] = d[i];
            total+=1;
        }
    }
    printf("%d",total);
    for (int k = 0; k < total; ++k) {
        printf(" %d",key[k]);
        printf(" %.1f",value[k]);
    }
    return 0;
}
