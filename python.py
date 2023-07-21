# count = 0
# while  count < 10:
#     # print(count)
#     count += 1

# Challenge: convert the while loop to recursive method that counts

def recursive(num = 0):
    if num >= 10:
        return 
    print(num)
    recursive(num + 1)

recursive()


# Practice: 
# count = 0
# def recursive(count):
#     # print(count) => 0, 1, 2, 3, 4
#     if count > 3:
#         return 'done'
#         # when count = 4, it should return 'done'
#     count += 1
#     # without the return keyword we're getting 'none' as we pop off things from the call-stack bc the recursive() function itself does not return anything
#     return recursive(count)
    
# print(recursive(count))