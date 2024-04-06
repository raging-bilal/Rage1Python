x = bool(int(input("Enter truth value for x (0 or 1): ")))
y = bool(int(input("Enter truth value for y (0 or 1): ")))

# Conjunction (AND)
print("Conjunction (AND):")
print("x\ty\tx AND y")
print("-"*22)
print(f"{int(x)}\t{int(y)}\t{int(x and y)}\n")

# Disjunction (OR)0
print("Disjunction (OR):")
print("x\ty\tx OR y")
print("-"*19)
print(f"{int(x)}\t{int(y)}\t{int(x or y)}\n")

# Exclusive OR (XOR)
print("Exclusive OR (XOR):")
print("x\ty\tx XOR y")
print("-"*20)
print(f"{int(x)}\t{int(y)}\t{int(x ^ y)}\n")

# Conditional (IF-THEN)
print("Conditional (IF-THEN):")
print("x\ty\tx -> y")
print("-"*18)
print(f"{int(x)}\t{int(y)}\t{int(not x or y)}\n")

# Bi-Conditional (IF AND ONLY IF)
print("Bi-Conditional (IF AND ONLY IF):")
print("x\ty\tx <-> y")
print("-"*20)
print(f"{int(x)}\t{int(y)}\t{int((not x or y) and (not y or x))}\n")

# Negation (NOT)
print("Negation (NOT):")
print("x\tnot x")
print("-"*12)
print(f"{int(x)}\t{int(not x)}\n")

# NAND
print("NAND:")
print("x\ty\tx NAND y")
print("-"*20)
print(f"{int(x)}\t{int(y)}\t{int(not (x and y))}\n")

# NOR
print("NOR:")
print("x\ty\tx NOR y")
print("-"*19)
print(f"{int(x)}\t{int(y)}\t{int(not (x or y))}\n")

# Exclusive NOR (XNOR or EQV)
print("Exclusive NOR (XNOR or EQV):")
print("x\ty\tx XNOR y")
print("-"*21)
print(f"{int(x)}\t{int(y)}\t{int(not (x ^ y))}\n")
