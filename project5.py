import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
transaction_data = pd.read_csv(r'C:\Users\User\Desktop\InputFolder\transaction_data.csv')
print(transaction_data)
# 5315 rows x 3 columns
print(transaction_data.dtypes)
transactions = transaction_data['transaction'].value_counts()
#sns.barplot(x = transactions.index, y = transactions, hue=transactions.index)
#plt.show()

# number of transaction for users
transact_user = (transaction_data.query('transaction == "successfull"') \
    .groupby('name') \
    .agg({'transaction':'count'}) \
    .rename(columns={'transaction':'total_transaction'}))
#print(transact_user)
#sns.histplot(data = transact_user)
#plt.show()
#print(transact_user.describe())
transaction_data_upd = pd.read_csv(r'C:\Users\User\Desktop\InputFolder\transaction_data_updated.csv')
print(transaction_data_upd)
transaction_data_upd['date'] = pd.to_datetime(transaction_data_upd['date'])
transaction_data_upd['minute_right'] = transaction_data_upd['date'].dt.minute + transaction_data_upd['date'].dt.hour*60
print(transaction_data_upd)
#user_vs_minute_pivot = transaction_data_upd[]
summary = transaction_data_upd.groupby(['name','minute_right'], as_index=False) \
    .agg({'transaction':'count'})
user_vs_minute_pivot = summary.pivot(columns='name', index='minute_right', values='transaction') \
    .fillna(0)
minute_trans = user_vs_minute_pivot.sum(axis=1)
plt.figure(figsize=(16,7))
sns.barplot(minute_trans)
plt.show()