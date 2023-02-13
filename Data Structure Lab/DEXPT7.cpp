#include <iostream>
using namespace std;
#define size 10

class stkexp
{
    int top;
    char stk[size];

public:
    stkexp()
    {
        top = -1;
    }
    void push(char x)
    {
        top = top + 1;
        stk[top] = x;
    }
    char pop()
    {
        char s;
        s = stk[top];
        top = top - 1;
        return s;
    }
    int isFull()
    {
        if (top == size)
        {
            return 1;
        }
        else
        {
            return 0;
        }
    }
    int isEmpty()
    {
        if (top == -1)
        {
            return 1;
        }
        else
            return 0;
    }
};

int main()
{
    stkexp s1;
    char exp[20], ch;
    int i = 0;
    cout << "_______Parenthesis Checking System________" << endl;
    cout << "Enter Your Expression:: ";
    cin >> exp;

    if (exp[0] == ')' || exp[0] == '}' || exp[0] == ']')
    {
        cout << "INVALID EXPRESSION!!!" << endl;
        return 0;
    }
    else
    {
        while (exp[i] != '\0')
        {
            ch = exp[i];
            switch (ch)
            {
            case '(':
                s1.push(ch);
                break;
            case '[':
                s1.push(ch);
                break;
            case '{':
                s1.push(ch);
                break;
            case ')':
                s1.pop();
                break;
            case ']':
                s1.pop();
                break;
            case '}':
                s1.pop();
                break;
            }
            ++i;
        }

    }
    if(s1.isEmpty()){
        cout<<"Expression is well Parenthised.";
    }
    else{
        cout<<"Invlaid Expression Or its not well Parenthised.!";
    }

    return 0;
}