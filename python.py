count = 0
while  count < 10:
    # print(count)
    count += 1

# Challenge: convert the while loop to recursive method that counts

def recursive(n = 0):
    print(n)
    count = 10
    if n > count-2:
        return 
    recursive(n + 1)

recursive()