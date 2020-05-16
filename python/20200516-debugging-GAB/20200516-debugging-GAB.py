import ipdb
for x in range(5):
    if x > 2:
        ipdb.set_trace()
    print(x)
    ipdb.set_trace()
    print(10*x)
    