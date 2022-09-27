#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);





// CODE WRITTEN BY ME
string isBalanced(string s) {
    // As it is a stack based question, I am using stack
    stack<string> stackVar;
    // By default brackets are balanced
    string ans="YES";
    // Iterating over each character of string
    for (char ch : s) {
        // Pushing all the opening brackets
        // And, in case the closing bracket is not matching the topmost bracket
        // The ans will be no, as the brackets are unbalanced
        // If closing brackets are matching the top most opening brakets
        // It is poped from the stack
        if(ch=='{' or ch=='(' or ch=='[') {
            stackVar.push(string(1, ch));
        } else if(ch=='}' and stackVar.top()!="{") {
            ans="NO";
        } else if(ch==')' and stackVar.top()!="(") {
            ans="NO";
        } else if(ch==']' and stackVar.top()!="[") {
            ans="NO";
        } else {
            stackVar.pop();
        }
    }
    return ans;
}
//END OF CODE






int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string t_temp;
    getline(cin, t_temp);

    int t = stoi(ltrim(rtrim(t_temp)));

    for (int t_itr = 0; t_itr < t; t_itr++) {
        string s;
        getline(cin, s);

        string result = isBalanced(s);

        fout << result << "\n";
    }

    fout.close();

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}
