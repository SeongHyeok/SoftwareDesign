def recursive_flatten(l):
    r = []
    for item in l:
        #print item
        if type(item) == list:
            #print "list", item
            nl = recursive_flatten(item)
            for ni in nl:
                r.append(ni)
        else:
            r.append(item)
    return r
    
print recursive_flatten([1, 2, [3, 5]])
print recursive_flatten([1, 2,[3, ["asdf", 4.0], 3]])
print recursive_flatten([[[1]]]);
print recursive_flatten([[[[4, [[6, [[7, [[[5]]]]]]], 8]]], 9]);