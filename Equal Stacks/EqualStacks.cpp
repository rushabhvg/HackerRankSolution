#include <bits/stdc++.h>
using namespace std;
#define ll long long
int main() {
    int n1, n2, n3;
    cin>>n1>>n2>>n3;
    
    int maxLen;
    maxLen=max(n1, n2);
    maxLen=max(maxLen, n3);
    
    stack<int> arr1, arr2, arr3;
    vector<int> num1, num2, num3;
    
    for(int i=0; i<n1; i++) {
        int temp;
        cin>>temp;
        num1.push_back(temp);
    }
    arr1.push(num1[n1-1]);
    for(int i=n1-2; i>=0; i--) {
        arr1.push(num1[i]+arr1.top());
    }
    
    for(int i=0; i<n2; i++) {
        int temp;
        cin>>temp;
        num2.push_back(temp);
    }
    arr2.push(num2[n2-1]);
    for(int i=n2-2; i>=0; i--) {
        arr2.push(num2[i]+arr2.top());
    }
    
    for(int i=0; i<n3; i++) {
        int temp;
        cin>>temp;
        num3.push_back(temp);
    }
    arr3.push(num3[n3-1]);
    for(int i=n3-2; i>=0; i--) {
        arr3.push(num3[i]+arr3.top());
    }
    
    for(int i=0; i<n1+n2+n3; i++) {
        if(arr1.empty() or arr2.empty() or arr3.empty()) {
            cout<<0;
            return 0;
        } else if(arr1.top()>arr2.top()) arr1.pop();
        else if(arr1.top()>arr3.top()) arr1.pop();
        else if(arr2.top()>arr1.top()) arr2.pop();
        else if(arr2.top()>arr3.top()) arr2.pop();
        else if(arr3.top()>arr2.top()) arr3.pop();
        else if(arr3.top()>arr1.top()) arr3.pop();
    }
    cout<<arr1.top()<<endl;
    return 0;
}
