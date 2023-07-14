#include <bits/stdc++.h>

using namespace std;

vector<int> slidingMaximum(const vector<int> &A, int B)
{
    deque<int> q;
    int i;
    for (i = 0; i < B; i++)
    {
        while (!q.empty() && A[i] > A[q.back()])
            q.pop_back();
        cout << i << endl;
        q.push_back(i);
    }
    vector<int> v;
    while (i < A.size())
    {
        cout << q.front() << endl;
        v.push_back(A[q.front()]);
        while (!q.empty() && q.front() < i - B)
            q.pop_front();
        while (!q.empty() && A[i] > A[q.back()])
            q.pop_back();
        q.push_back(i);
        i++;
    }
    v.push_back(A[q.front()]);
    return v;
}

int main()
{
    vector<int> v = {1, 3, -1, -3, 5, 3, 6, 7};
    vector<int> ans = slidingMaximum(v, 3);
    for (auto i : ans)
        cout << i << " ";
    cout << endl;
    return 0;
}
