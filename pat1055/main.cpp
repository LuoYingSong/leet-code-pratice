#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
using namespace std;

struct data{
    string name;
    int money;
    int age;
};

int cmp(const data& list1,const data& list2){
    if (list1.money!=list2.money){
        return list1.money > list2.money;
    }
    if (list1.age!=list2.age){
        return list1.age < list2.age;
    }
    return list1.name<list2.name;

}

int main(int argc, char** argv) {
    int n,m;
    scanf("%d%d",&n,&m);
    vector<data> saver;
    for(int i=0;i<n;i++){
        string name;
        int age, money;
        data man;
        cin>>name;
        scanf("%d%d",&age,&money);
        man.name=name;
        man.money = money;
        man.age = age;
        saver.push_back(man);
    }
    for(int i = 0;i<m;i++){
        int line,start,end;
        scanf("%d%d%d",&line,&start,&end);
        vector<data> datas;
        for(int j = 0;j<n;j++){
            if(saver[j].age>=start && saver[j].age <=end){
                datas.push_back(saver[j]);
            }
        }
        cout<<"Case #"<<i+1<<":"<<endl;
        if(datas.empty()){
            cout<<"None"<<endl;
        } else{
            sort(datas.begin(),datas.end(),cmp);
            for(int i = 0; i<line&i<datas.size();i++){
                cout<<datas[i].name<<" "<<datas[i].age<<" "<<datas[i].money<<endl;
            }
        }
    }
	return 0;
}
