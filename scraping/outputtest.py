# import time, sys
# for i in range(50):
#     if (i+1)%5 == 0:
#         sys.stdout.write("\rSearching %i potential locations..." % (i+1))
#         sys.stdout.flush()
#         time.sleep(.3)


A = [5, 2, 6, 10, 3]
b= 5
while True:
    if b not in A:
        A.append(b)
        break

print 'done'