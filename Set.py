# There are several ways to join two or more sets in Python.
# The union() and update() methods joins all items from both sets.
# The intersection() method keeps ONLY the duplicates.
# The difference() method keeps the items from the first set that are not in the other set(s).
# The symmetric_difference() method keeps all items EXCEPT the duplicates.

set1={"a","b","c","c"}
set2={1,3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
# a=set1.union(set2).union(set3).union(set4)
a=set1 |set2 |set3 |set4
print(a);