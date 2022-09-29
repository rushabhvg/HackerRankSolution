#include <bits/stdc++.h>
using namespace std;

int main() {
    int as=0, bs=0;
    int a[3], b[3];
    cin>>a[0]>>a[1]>>a[2];
    cin>>b[0]>>b[1]>>b[2];
    for(int i=0; i<3; i++) {
        // cout<<a[i]<<" "<<b[i]<<endl;
        if(a[i]>b[i]) as+=1;
        if(b[i]>a[i]) bs+=1;
    }
    cout<<as<<" "<<bs;
    return 0;
}
