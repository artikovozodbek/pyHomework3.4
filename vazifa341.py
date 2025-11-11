set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8, 9}

yigindi = sum(set1.intersection(set2))
print(yigindi - sum(set1 - set2))
