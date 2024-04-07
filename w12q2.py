import pandas as pd

data = {
    "Name" : ["Amit", "Raza", "Saif", "Rahul", "Priya", "Kanak", "Zeba"],
    "Age" : [23, 67, 8, 34, 56, 5, 70]
}

df = pd.DataFrame(data)

print(df, "\n")

# Define the age ranges for each label
bins = [0, 18, 59, float('inf')]
labels = ['Youth', 'Adult', 'Senior']

# Discretize the 'Age' column into labels
df['Age Label'] = pd.cut(df['Age'], bins=bins, labels=labels)

print(df)