#!/usr/bin/env python3

from sklearn.cluster import DBSCAN
from transformers import AutoTokenizer, AutoModel
import torch
import numpy as np
from pprint import pprint

# List of sentences to cluster
# sentences = [
#     "This is a sample sentence.",
#     "This is another sample sentence.",
#     "Yet another sample sentence.",
# ]

sentences = [
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

# Initialize Hugging Face tokenizer and model
# tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
# model = AutoModel.from_pretrained("distilbert-base-uncased")


# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-mpnet-base-v2")
model = AutoModel.from_pretrained("sentence-transformers/all-mpnet-base-v2")

# Generate embeddings for each sentence
embeddings = []
for sentence in sentences:
    inputs = tokenizer(sentence, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    embeddings.append(outputs.last_hidden_state[:, 0, :].numpy())

# Reshape embeddings to 2D
embeddings_2d = np.array(embeddings).reshape(len(embeddings), -1)

# Perform clustering with DBSCAN
clustering = DBSCAN(eps=2, min_samples=2).fit(embeddings_2d)

# Print cluster labels for each sentence
pprint(clustering.labels_)

clusters = {}
# Print the cluster labels for each sentence
for i, sentence in enumerate(sentences):
    cluster_id = clustering.labels_[i]

    # print(f"Sentence: {sentence}")
    # print(f"Cluster: {cluster_id}")

    if cluster_id not in clusters:
        clusters[cluster_id] = []
    clusters[cluster_id].append(sentence)
pprint(clusters)
