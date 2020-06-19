import pandas as pd

train_df = pd.read_csv('./datasets/train_preprocessed.csv')

print('Corelation between all the columns:')
print(train_df.corr())

print('Corelation between Sex and Survived:',train_df['Sex'].corr(train_df['Survived']))

