- [Quickstart](#quickstart)
  - [Output](#output)
- [What does "a priori" mean literally?](#what-does-a-priori-mean-literally)
- [Example](#example)

### Quickstart

```
./apriori_pattern_search.py
```

#### Output

```
   support       itemsets
0      0.8         (Eggs)
1      0.6         (Milk)
2      0.6        (Onion)
3      0.6       (Yogurt)
4      0.6  (Eggs, Onion)
```

### What does "a priori" mean literally?

The term "a priori" comes from Latin, and literally translates to "from the earlier" or "from what comes before". This literal meaning helps understand the concept it represents in various fields like philosophy and logic.

### Example

Let's say you and your friends have a big box of different colored blocks: red, blue, green, and yellow. You all start building towers with these blocks.

The Apriori algorithm is like someone watching you play and noticing that if a tower has a red block, it often also has a blue block. They write this down as a rule: "Red often goes with Blue". They keep watching and notice more rules, like "Green often goes with Yellow", or "Red and Blue often go with Green", and so on.

But they're smart about how they find these rules. They don't waste time looking at combinations that are unlikely to happen. For example, if they hardly ever see a red block and a green block together, they won't bother checking if red, green and blue blocks often appear together. This is the "Apriori" part - it's a principle that says if a block doesn't appear often in a tower, then that block with any other block won't appear often either.

So, in simple terms, the Apriori algorithm is a way of finding out which things often go together, by looking at lots of examples and finding patterns. But it does this in a smart, efficient way, by not wasting time on patterns that are unlikely to happen.