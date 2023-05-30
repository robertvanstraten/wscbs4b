import matplotlib.pyplot as plt
import pandas as pd

test_data = pd.read_csv("data/test.csv")
prediction = pd.read_csv("data/submission.csv")

test_full = pd.merge(test_data, prediction, on='PassengerId')

survivors_by_gender = test_full.groupby('Sex')['Survived'].sum()

# Plot the bar plot
plt.bar(survivors_by_gender.index, survivors_by_gender.values)
plt.xlabel('Gender')
plt.ylabel('Number of Survivors')
plt.title('Survivors by Gender')
plt.show()
