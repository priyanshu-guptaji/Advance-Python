set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

print("Set 1:", set1)
print("Set 2:", set2)


union_set = set1 | set2
print("\nUnion (Set1 | Set2):", union_set)
print(set1.union(set2))
print()


intersection_set = set1 & set2
print("Intersection (Set1 & Set2):", intersection_set)


difference_set1 = set1 - set2
difference_set2 = set2 - set1
print("Difference (Set1 - Set2):", difference_set1)
print("Difference (Set2 - Set1):", difference_set2)

symmetric_diff = set1 ^ set2
print("Symmetric Difference (Set1 ^ Set2):", symmetric_diff)



print("\nUsing Set Methods:")
print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Difference:", set1.difference(set2))
print("Symmetric Difference:", set1.symmetric_difference(set2))
