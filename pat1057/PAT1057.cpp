#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
using namespace std;
int saver[200][500];
int saver_length[200];
vector<int> stack;

int main(int argc, char** argv) {
    int n,num,counter,index;
    scanf("%d",&n);
    char str[10];
    for(int i = 0;i<n;i++){
        scanf("%s",&str);
        if (str[1]=='u'){
            scanf("%d",&num);
            stack.push_back(num);
            saver[num/500][num%500] += 1;
            saver_length[num/500] += 1;
        }
        else if (str[1]=='e'){
            if(stack.empty()){
                printf("Invalid\n");
            } else{
                counter = 0;
                for(int j=0;j<200;j++){
                    index = j;
                    counter += saver_length[j];
                    if(counter>=(stack.size()+1)/2){
                        counter -= saver_length[j];
                        break;
                    }

                }
                for(int j=0;j<500;j++){
                    counter += saver[index][j];
                    if(counter==(stack.size()+1)/2){
                        printf("%d\n",index*500+j);
                        break;
                    }
                }
            }
        } else if (str[1]=='o'){
            if(!stack.empty()) {
                num = stack[stack.size() - 1];
                stack.pop_back();
                saver[num/500][num%500]-=1;
                saver_length[num/500] -= 1;
                printf("%d\n",num);
            } else{
                printf("Invalid\n");
            }
        }
    }
	return 0;
}
