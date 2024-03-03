#!/usr/bin/env python3

import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from pprint import pprint

# This is your dataset
dataset = [
    ["Milk", "Onion", "Nutmeg", "Eggs", "Yogurt"],
    ["Onion", "Nutmeg", "Eggs", "Yogurt"],
    ["Milk", "Apple", "Eggs"],
    ["Milk", "Unicorn", "Corn", "Yogurt"],
    ["Corn", "Onion", "Onion", "Ice cream", "Eggs"],
]

# The TransactionEncoder transforms our dataset into a boolean matrix
te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
print("Boolean matrix: ")
pprint(te_ary)

# We convert the matrix into a DataFrame for better readability
df = pd.DataFrame(te_ary, columns=te.columns_)
print("DataFrame: ")
pprint(df)

# Now we can apply the apriori algorithm to find frequent itemsets
frequent_itemsets = apriori(df, min_support=0.6, use_colnames=True)
print("Frequent itemsets:")
print(frequent_itemsets)
