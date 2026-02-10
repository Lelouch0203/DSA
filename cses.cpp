#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;
    long long fsum = 0;
    int num;
    for (int i = 0; i < n - 1; i++)
    {
        cin >> num;
        fsum += num;
    }
    long long sum = (long long)n * (n + 1) / 2;
    cout << sum - fsum;
}
