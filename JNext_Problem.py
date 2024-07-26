'''DevG likes too much fun to do with numbers. Once his friend Arya came and gave him a challenge, he gave DevG an array of digits which is forming a number currently (will be called as given number). DevG was challanged to find the just next greater number which can be formed using digits of given number. Now DevG needs your help to find that just next greater number and win the challenge.

Input
The first line have t number of test cases (1 <= t <= 100). In next 2*t lines for each test case first there is number n (1 <= n <= 1000000) which denotes the number of digits in given number and next line contains n digits of given number separated by space.

Output
Print the just next greater number if possible else print -1 in one line for each test case.

'''

'''t = int(input())
for _ in range(t):
    n = int(input())
    digits = list(map(int, input().split()))
    # Find the first decreasing digit from the right
    i = n - 2
    while i >= 0 and digits[i] >= digits[i + 1]:
        i -= 1
    if i == -1:
        print(-1)
    else:
        # Find the smallest digit greater than digits[i]
        j = n - 1
        while digits[j] <= digits[i]:
            j -= 1
        # Swap digits[i] and digits[j]
        digits[i], digits[j] = digits[j], digits[i]
        # Reverse the digits after i
        digits[i + 1:] = digits[n - 1:i:-1]
        print(''.join(map(str, digits)))
'''

t=int(input())
for i in range(t):
    n=int(input())
    numList=list(map(int,input().split()))
    index=n-1
    for i in range(n-1,-1,-1):
        if numList[i]>numList[i-1]:
            numList[i],numList[i-1]=numList[i-1],numList[i]
            index=i
            break
    res=[str(ele) for ele in (numList[:index]+(numList[index:])[::-1])]
    print(''.join(res))
