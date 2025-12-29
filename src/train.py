import torch
import torch.nn as nn
import torch.optim as optim
from model import AutoEncoder

def train_model(X, epochs=10, lr=0.001):
    X = torch.tensor(X.toarray(), dtype=torch.float32)

    model = AutoEncoder(X.shape[1])
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=lr)

    for epoch in range(epochs):
        optimizer.zero_grad()
        output, _ = model(X)
        loss = criterion(output, X)
        loss.backward()
        optimizer.step()

        print(f"Epoch {epoch+1}/{epochs} - Loss: {loss.item():.4f}")

    return model

