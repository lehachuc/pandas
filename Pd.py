import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Create a DataFrame with the specified structure
data = {
    'PassengerId': pd.Series(range(1, 892), dtype='int64'),
    'Survived': pd.Series(np.random.randint(0, 2, size=891), dtype='int64'),
    'Pclass': pd.Series(np.random.randint(1, 4, size=891), dtype='int64'),
    'Name': pd.Series(['Name {}'.format(i) for i in range(891)], dtype='object'),
    'Sex': pd.Series(['male' if i % 2 == 0 else 'female' for i in range(891)], dtype='object'),
    'Age': pd.Series(np.concatenate([np.random.uniform(0, 80, 714), [np.nan] * (891 - 714)]), dtype='float64'),
    'SibSp': pd.Series(np.random.randint(0, 6, size=891), dtype='int64'),
    'Parch': pd.Series(np.random.randint(0, 6, size=891), dtype='int64'),
    'Ticket': pd.Series(['Ticket {}'.format(i) for i in range(891)], dtype='object'),
    'Fare': pd.Series(np.random.uniform(5, 500, size=891), dtype='float64'),
    'Cabin': pd.Series(np.concatenate([['Cabin {}'.format(i) for i in range(204)], [np.nan] * (891 - 204)]), dtype='object'),
    'Embarked': pd.Series(['C'] * 2 + ['Q'] * 2 + ['S'] * (889 - 4), dtype='object')
}

df = pd.DataFrame(data)


plt.figure(figsize=(6, 6))
sns.countplot(x='Embarked', data=df, alpha = 0.6)
plt.show()