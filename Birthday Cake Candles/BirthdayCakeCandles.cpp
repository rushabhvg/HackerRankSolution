/*
BY RUSHABH GALA
rushabhvg

GitHub :
https://github.com/rushabhvg

StackOverflow :
https://stackoverflow.com/users/16571212/rushabhvg

LinkedIn:
https://www.linkedin.com/in/rushabhvg/
*/

#include <bits/stdc++.h>
using namespace std;

#define ll long long int

int main() {
    ll n, i, maxH=0;
    ll temp;
    vector<ll> candles(10000001, 0);
    cin>>n;
    for(i=0; i<n; i++) {
        cin>>temp;
        candles[temp]++;
        if(maxH<temp) {
            maxH=temp;
        }
        // cout<<endl<<temp<<"\t"<<candles[temp];
    }
    cout<<candles[maxH];
    return 0;
}

/*
BY RUSHABH GALA
rushabhvg

GitHub :
https://github.com/rushabhvg

StackOverflow :
https://stackoverflow.com/users/16571212/rushabhvg

LinkedIn:
https://www.linkedin.com/in/rushabhvg/
*/
