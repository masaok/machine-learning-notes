#!/usr/bin/env python3

from sklearn.cluster import DBSCAN
from transformers import AutoTokenizer, AutoModel
import torch
import numpy as np

# Initialize Hugging Face tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
model = AutoModel.from_pretrained("distilbert-base-uncased")

# List of sentences to cluster
sentences = [
    "This is a sample sentence.",
    "This is another sample sentence.",
    "Yet another sample sentence.",
]

# Generate embeddings for each sentence
embeddings = []
for sentence in sentences:
    inputs = tokenizer(sentence, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    embeddings.append(outputs.last_hidden_state[:, 0, :].numpy())

# # Reshape embeddings to 2D
# embeddings_2d = np.array(embeddings).reshape(len(embeddings), -1)

# Perform clustering with DBSCAN
clustering = DBSCAN(eps=3, min_samples=2).fit(embeddings)

# Print cluster labels for each sentence
print(clustering.labels_)
