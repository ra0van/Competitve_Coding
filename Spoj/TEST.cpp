#include <iostream>
using namespace std;

int main()
{
int nums[100] = {0};

int ch;
for (int i = 0; ;i++)
{
if(!(cin >> ch))
break;
nums[i] = ch;
}

for(int j = 0; (nums[j] != 42 && j < 100); j++)
{cout << nums[j] << endl;}

return 0;
} 
