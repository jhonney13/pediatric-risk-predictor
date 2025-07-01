import pandas as pd
import numpy as np

np.random.seed(42)
data = pd.DataFrame({
    'age': np.random.randint(0, 12, 200),
    'weight': np.random.uniform(2, 30, 200),
    'diagnosis': np.random.choice(['ASD', 'VSD', 'TOF', 'PDA'], 200),
    'surgery_duration': np.random.randint(60, 300, 200),
    'oxygen_level': np.random.uniform(80, 100, 200),
    'heart_rate': np.random.randint(80, 180, 200),
    'risk_level': np.random.choice(['Low', 'Medium', 'High'], 200)
})
data.to_csv('pediatric_surgery_data.csv', index=False)
