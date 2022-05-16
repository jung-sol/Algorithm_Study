A, B = map(int, input().split())


if A > B:
    result = '>'
elif B > A:
    result = '<'
else:
    result = '=='
    
print(result)