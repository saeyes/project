# model.py

import random
import numpy as np
from sklearn.linear_model import LogisticRegression

def generate_data(n=500):
    X, y = [], []
    for _ in range(n):
        t1 = random.randint(1500, 2500)
        t2 = random.randint(1500, 2500)
        diff = t1 - t2
        win = 1 if diff + random.randint(-200, 200) > 0 else 0
        X.append([t1, t2])
        y.append(win)
    return np.array(X), np.array(y)

X, y = generate_data()

model = LogisticRegression()
model.fit(X, y)

def predict_win(team1_mmr, team2_mmr):
    return model.predict_proba([[team1_mmr, team2_mmr]])[0][1]