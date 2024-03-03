Machine Learning examples

- [Quickstart](#quickstart)
- [VSCode Notes](#vscode-notes)
- [Machine Learning Overview](#machine-learning-overview)
  - [Classical vs. Reinforcement Learning :bike:](#classical-vs-reinforcement-learning-bike)
  - [Ensemble Methods :family:](#ensemble-methods-family)
  - [Neural Nets :dog:](#neural-nets-dog)
    - [Neural Nets vs. Deep Learning :banana: :apple:](#neural-nets-vs-deep-learning-banana-apple)
- [Credit](#credit)

## Quickstart

- Install `pipx`: https://pipx.pypa.io/stable/installation/
- Install `poetry`: https://python-poetry.org/docs/#installation

```
poetry shell               # Start the Poetry virtual environment
poetry env info            # Check the environment (optional)
poetry install --no-root   # Install packages without dependencies
./classical-learning/unsupervised/clustering/clustering_hugging_face.py
```

https://python-poetry.org/docs/cli/

## VSCode Notes

`CTRL + SHIFT + P` > `Python: Select Interpreter`

Pick the one labeled `Poetry` so VSCode matches the virtual environment.

## Machine Learning Overview

![image](https://github.com/masaok/machine-learning-examples/assets/1320083/ab4e42ea-1846-43fa-a137-c2b17ca50948)

Source: https://vas3k.com/blog/machine_learning/index.html#the-map-of-the-machine-l

### Classical vs. Reinforcement Learning :bike:

Let's use the example of learning to ride a bike:

**Classical Machine Learning (like Supervised Learning)**: This is like when your mom or dad teaches you how to ride a bike. They tell you what to do: "Put your feet on the pedals, hold the handlebars, push off, and start pedaling." They might even hold the bike steady for you at first. You're learning from their instructions and the examples they give you. In programming, this is like giving the computer a bunch of examples (data) with the right answers (labels), and it learns to predict the right answer for new examples.

**Reinforcement Learning**: This is like learning to ride a bike all by yourself. You don't know how to do it at first, so you try different things. Maybe you push off too hard and fall over, or you don't pedal fast enough and the bike doesn't move. But each time you try, you learn a little more about what works and what doesn't. Eventually, you figure out how to balance, pedal, and steer all at the same time. In programming, this is like letting the computer try different solutions to a problem. It gets "rewards" or "penalties" based on how well it does, and it uses this feedback to improve over time.

### Ensemble Methods :family:

**Ensemble methods** in machine learning are like asking a bunch of your friends to help you with your homework. Each of your friends is smart in their own way and will give you their own answer. Some might be good at math, some might be good at history, and so on.

Now, instead of just taking one friend's answer, you decide to take all their answers and combine them. There are a few ways you could do this.

1. You could just take the most common answer (this is like Voting).
1. You could ask each friend how confident they are in their answer, and give more weight to the answers from friends who are more confident (this is like Weighted Voting).
1. You could even ask a few friends first, and then based on their answers, decide which other friends to ask next (this is like Boosting).

By combining all your friends' answers, you're likely to get a better result than if you just asked one friend. That's what ensemble methods do in machine learning - they combine the predictions from multiple models to get a better prediction.

### Neural Nets :dog:

Imagine you're trying to learn how to recognize dogs. You have a big book full of pictures of different animals, and your task is to figure out which ones are dogs.

A **neural network** is like your brain in this situation. It starts with no knowledge about what a dog looks like. But as you show it more and more pictures, pointing out which ones are dogs, it starts to learn. Maybe it notices that dogs have four legs, or that they have fur, or that they have a certain shape of ears. Each of these observations is like a neuron in the network, and they all work together to help the network recognize dogs.

Now, imagine you want to recognize not just dogs, but all kinds of animals. You'd need to notice more details - like the shape of the nose, the size of the animal, the kind of tail it has, and so on. This is like a deep neural network. It has many layers of neurons, each layer learning to recognize more and more complex features.

So, in simple terms, a **neural network** is like a brain that learns from examples, and a **deep neural network** is like a very smart brain that can recognize complex things by building up from simple features.

#### Neural Nets vs. Deep Learning :banana: :apple:

Imagine you're learning to recognize different types of fruits.

A **neural network** is like your brain when it's just starting to learn. At first, you might only be able to tell the difference between very different fruits, like bananas and apples, because they have different shapes and colors.

**Deep learning**, on the other hand, is like your brain after you've learned a lot more. Now, not only can you tell the difference between a banana and an apple, but you can also tell the difference between different types of apples. You've learned to notice smaller details, like the color, size, and shape of the spots on the apple.

So, the main difference is that **neural networks** are simpler and can learn to recognize simple patterns, while deep learning uses more complex networks (deep neural networks) that can learn to recognize more complex patterns.

## Credit

Github Copilot Chat for all explanations.

https://docs.github.com/en/copilot/github-copilot-chat/about-github-copilot-chat