class RELATION:
    def __init__(self, n, rel):
        self.n = n
        self.rel = rel

    def is_reflexive(self):
        for i in range(self.n):
            if self.rel[i][i] != 1:
                return False
        return True

    def is_symmetric(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.rel[i][j] != self.rel[j][i]:
                    return False
        return True

    def is_antisymmetric(self):
        for i in range(self.n):
            for j in range(self.n):
                if i != j and self.rel[i][j] == 1 and self.rel[j][i] == 1:
                    return False
        return True

    def is_transitive(self):
        for i in range(self.n):
            for j in range(self.n):
                for k in range(self.n):
                    if self.rel[i][j] == 1 and self.rel[j][k] == 1 and self.rel[i][k] != 1:
                        return False
        return True


# Example usage
n = 3
rel = [[1, 0, 1],
       [0, 1, 0],
       [1, 0, 1]]
print(rel)
r = RELATION(n, rel)
print("Reflexive: ", r.is_reflexive())     # False
print("Symmetric: ", r.is_symmetric())     # True
print("Anti-Symmetric: ",r.is_antisymmetric()) # False
print("Transitive: ",r.is_transitive())    # True
