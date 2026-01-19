import pandas as pd
import numpy as np

data = pd.DataFrame({
    "Кузов": np.random.choice(["Седан", "Универсал", "Хэтчбэк"], 1000),
    "Рейтинг": np.random.choice(["Высокий", "Низкий"], 1000, p=[0.6, 0.4])
})

pd.crosstab(data["Кузов"], data["Рейтинг"], normalize="index")