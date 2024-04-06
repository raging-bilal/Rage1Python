import itertools

class SetOperations:
    def __init__(self):
        self.set1 = set(map(int, input("Enter elements of set 1 (separated by spaces): ").split()))
        self.set2 = set(map(int, input("Enter elements of set 2 (separated by spaces): ").split()))

    def is_subset(self):
        if self.set1.issubset(self.set2):
            print("Set 1 is a subset of Set 2.")
        elif self.set2.issubset(self.set1):
            print("Set 2 is a subset of Set 1.")
        else:
            print("Neither set is a subset of the other.")

    def union(self):
        print("Union of Set 1 and Set 2:", self.set1.union(self.set2))

    def intersection(self):
        print("Intersection of Set 1 and Set 2:", self.set1.intersection(self.set2))

    def complement(self):
        universal_set = set(map(int, input("Enter elements of the Universal set (separated by spaces): ").split()))
        print("Complement of Set 1 with respect to the Universal set:", universal_set.difference(self.set1))

    def set_difference(self):
        print("Set difference of Set 1 and Set 2 (Set1 - Set2):", self.set1.difference(self.set2))
        print("Set difference of Set 2 and Set 1 (Set2 - Set1):", self.set2.difference(self.set1))

    def symmetric_difference(self):
        print("Symmetric difference of Set 1 and Set 2:", self.set1.symmetric_difference(self.set2))

    def cartesian_product(self):
        print("Cartesian product of Set 1 and Set 2:")
        for i in itertools.product(self.set1, self.set2):
            print(i)

set_ops = SetOperations()

set_ops.is_subset()

set_ops.union()

set_ops.intersection()

set_ops.complement()

set_ops.set_difference()
set_ops.symmetric_difference()

set_ops.cartesian_product()
