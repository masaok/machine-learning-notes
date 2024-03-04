- [Quickstart](#quickstart)
  - [Output](#output)
- [What does "a priori" mean literally?](#what-does-a-priori-mean-literally)
- [Example](#example)
- [The Code](#the-code)
  - [What is `min_support`?](#what-is-min_support)

### Quickstart

```
./**Apriori**_pattern_search.py
```

#### Output

```
Boolean matrix:
array([[False, False,  True, False,  True,  True,  True, False,  True],
       [False, False,  True, False, False,  True,  True, False,  True],
       [ True, False,  True, False,  True, False, False, False, False],
       [False,  True, False, False,  True, False, False,  True,  True],
       [False,  True,  True,  True, False, False,  True, False, False]])
DataFrame:
   Apple   Corn   Eggs  Ice cream   Milk  Nutmeg  Onion  Unicorn  Yogurt
0  False  False   True      False   True    True   True    False    True
1  False  False   True      False  False    True   True    False    True
2   True  False   True      False   True   False  False    False   False
3  False   True  False      False   True   False  False     True    True
4  False   True   True       True  False   False   True    False   False
Frequent itemsets:
   support       itemsets
0      0.8         (Eggs)
1      0.6         (Milk)
2      0.6        (Onion)
3      0.6       (Yogurt)
4      0.6  (Onion, Eggs)
```

### What does "a priori" mean literally?

The term "a priori" comes from Latin, and literally translates to "from the earlier" or "from what comes before". This literal meaning helps understand the concept it represents in various fields like philosophy and logic.

### Example

Let's say you and your friends have a big box of different colored blocks: red, blue, green, and yellow. You all start building towers with these blocks.

The **Apriori** algorithm is like someone watching you play and noticing that if a tower has a red block, it often also has a blue block. They write this down as a rule: "Red often goes with Blue". They keep watching and notice more rules, like "Green often goes with Yellow", or "Red and Blue often go with Green", and so on.

But they're smart about how they find these rules. They don't waste time looking at combinations that are unlikely to happen. For example, if they hardly ever see a red block and a green block together, they won't bother checking if red, green and blue blocks often appear together. This is the **"Apriori"** part - it's a principle that says if a block doesn't appear often in a tower, then that block with any other block won't appear often either.

So, in simple terms, the **Apriori** algorithm is a way of finding out which things often go together, by looking at lots of examples and finding patterns. But it does this in a smart, efficient way, by not wasting time on patterns that are unlikely to happen.

### The Code

#### What is `min_support`?

In the context of **Apriori** pattern search, which is a popular algorithm used for mining frequent itemsets for boolean association rules, `min_support` is a user-defined parameter that determines the minimum support of an itemset to be considered frequent.

Let's break it down:

An **itemset** is a set of one or more items. For example, in a supermarket scenario, an itemset could be {milk, bread} meaning that milk and bread are bought together.

The **support** of an itemset is the proportion of transactions in the database in which the itemset appears. For example, if out of 100 transactions, milk and bread are bought together 10 times, the support for the itemset {milk, bread} is 10/100 = 0.1.

The **min_support** is the minimum threshold that we set for the support. If an itemset's support is less than min_support, then it's not considered a frequent itemset and is discarded from further analysis.

So, in simple terms, `min_support` is a way to tell the **Apriori** algorithm to only pay attention to itemsets that occur together relatively frequently in the dataset. It helps to filter out less common itemsets and focus on the more prevalent patterns.