#!/usr/bin/env python3

import torch
from transformers import AutoTokenizer, AutoModel
from sklearn.cluster import KMeans
import kneed
import matplotlib.pyplot as plt

from pprint import pprint

tokens = [
    "potato",
    "tomato",
    "hamburger",
    "french fries",
    "pizza",
    "spaghetti",
    "pasta",
    "beef",
    "chicken",
    "pork",
    "fish",
    "salad",
    "lettuce",
]

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-mpnet-base-v2")
model = AutoModel.from_pretrained("sentence-transformers/all-mpnet-base-v2")

# Vectorize the sentences
embeddings = []
for token in tokens:
    print()
    print(f"Token: {token}")
    encoded_token = tokenizer(token, return_tensors="pt")
    pprint(encoded_token)
    with torch.no_grad():
        output = model(**encoded_token)
    embedding = output.last_hidden_state[:, 0].detach().cpu().numpy()

    print("Embedding (vector) shape: ", embedding.shape)

    embeddings.append(embedding[0])

# Use kneed package to find magically cluster number
num_clusters_to_test = range(1, 10)
num_clusters = [i for i in num_clusters_to_test]
distortions = []
for k in num_clusters_to_test:
    kmeanModel = KMeans(n_clusters=k)
    kmeanModel.fit(embeddings)
    distortions.append(kmeanModel.inertia_)

print("Distortions: ", distortions)

# sensitivity = 1.0
# sensitivity = 0.5
sensitivity = 0.01
kneedle = kneed.KneeLocator(
    num_clusters, distortions, S=sensitivity, curve="convex", direction="decreasing"
)
print(kneedle.knee)
print(kneedle.elbow)

num_clusters = 4

print("Performing k-means clustering with n clusters: ", num_clusters)

# Perform k-means clustering with n clusters
kmeans = KMeans(n_clusters=num_clusters)
kmeans.fit(embeddings)

clusters = {}
# Print the cluster labels for each token
for i, token in enumerate(tokens):
    cluster_id = kmeans.labels_[i]

    # print(f"Sentence: {sentence}")
    # print(f"Cluster: {cluster_id}")

    if cluster_id not in clusters:
        clusters[cluster_id] = []
    clusters[cluster_id].append(token)
print(clusters)
