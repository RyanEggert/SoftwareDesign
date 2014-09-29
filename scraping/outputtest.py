import time, sys
for i in range(50):
    if (i+1)%5 == 0:
        sys.stdout.write("\rSearching %i potential locations..." % (i+1))
        sys.stdout.flush()
        time.sleep(.3)
