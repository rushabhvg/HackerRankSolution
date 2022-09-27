#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    // Create a stack
    stack<int> stackVar;
    cin>>n;
    while(n--) {
        // This is the query type
        int opNum;
        cin>>opNum;
        // If the query is of insert type:
        if(opNum==1) {
            //Take the value to be inserted
            int insValue;
            cin>>insValue;
            // stackVar.size() gives the size
            // If it is 0, it means stack is empty
            if (stackVar.size()>0) {
                // If the value to be inserted is greater than top's element
                // Push it into the stack
                // else random push
                if(insValue>stackVar.top()) stackVar.push(insValue);
                else stackVar.push(stackVar.top());
            } else stackVar.push(insValue);
            // Remember, in this stack we are only pushing the max value
            // For case:
            /*
                1 97
                2
                1 20
                2
                1 26
                1 20
                2
                3
                1 91
                3
            */
            // Stack will be
            /*
                97
                empty
                20
                empty
                26
                26 26
                26
                print 26
                26 91
                print 91
            */
            // Basically instead of pushing 20 earlier we had pushed 26
            // Because the top most element of stack will be maximum
        }
        // If the query is of pop type:
        else if(opNum==2) stackVar.pop();
        // If the query is of max type:
        else cout<<stackVar.top()<<endl;
    }
    return 0;
}
