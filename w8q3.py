def reflexive(setA, R):
    for a in setA:
        if (a, a) not in R:
            return False
    return True

def symmetric(R):
    for (a, b) in R:
        if (b, a) not in R:
            return False
    return True

def transitive(R):
    for (a, b) in R:
        for (c, d) in R:
            if b == c and (a, d) not in R:
                return False
    return True


def equivalent_or_partial_order(setA, R):
    if reflexive(setA, R) and symmetric(R) and transitive(R):
        print("The relation is an Equivalence Relation")
    elif reflexive(setA, R) and transitive(R):
        print("The relation is a Partial Order Relation")
    else:
        print("The relation is neither an Equivalence Relation nor a Partial Order Relation")

setA = {1, 2, 3, 4}

R = {(1, 1), (2, 2), (3, 3), (4, 4), (1, 3), (3, 1), (2, 4), (4, 2)}

equivalent_or_partial_order(setA, R) 