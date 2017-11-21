// you can use includes, for example:
// #include <algorithm>

// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;
#include <bits/stdc++.h>

int solution(vector<int> &A) {
    // write your code in C++14 (g++ 6.2.0)
    long long ans = 0;
    vector<long long> radius;
    map<long long, long long> m;
    for (long long i = 0; i < (long long) A.size(); i++) {
        radius.push_back(i - A[i]);
        m[i - A[i]]++;
    }
    sort(radius.begin(), radius.end());
    // for (int i = 0; i < (int) A.size(); i++) {
    //     cout << radius[i] << endl;
    // }
    // puts("");
    for (long long i = 0; i < (long long) A.size(); i++) {
        long long found = (long long) (upper_bound(radius.begin(), radius.end(), i + A[i]) - upper_bound(radius.begin(), radius.end(), i - A[i]));
        //cout << found << endl;
        ans += found;
        if (ans > (long long) 1e7) {
            return -1;
        }
    }
    for (auto it = m.begin(); it != m.end(); it++) {
        ans += (long long) ((*it).second) * (long long) ((*it).second - 1) / 2;
        if (ans > (long long) 1e7) {
            return -1;   
        }
    }
    return ans;   
}