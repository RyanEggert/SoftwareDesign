def flatten_list(L):
    if type(L[0]) != list:
        return L
    else:
        result = []
        for small in L:
            result += flatten_list(small)
        print result
        return result


list = flatten_list([[[5,60],[7,40],[[6,20],[2,123],[8,234],[4,642],[[2,231],[2,986],[3,133],[6,3125],[6664,9]]]]])

print '\n' *2
print list