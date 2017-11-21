// you can use includes, for example:
// #include <algorithm>

// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;
#include <bits/stdc++.h>

int solution(int N) {
    int ans = 0;
    int count = 0;
    bool flag = false;
    while (N) {
        if (N & 1) {
            if (!flag) {
                flag = true;
                count = 0;
            } else {
                ans = max(ans, count);
                count = 0;
            }
        } else {
            count += (flag);
        }
        N >>= 1;
    }
    return ans;
}