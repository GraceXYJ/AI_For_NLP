import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
ontent = pd.read_csv('/Users/mqgao/Workspace/Lecture/datasource/titanic/train.csv')
content = content.dropna()
age_with_fares = content[
    (content['Age'] > 22) & (content['Fare'] < 400) & (content['Fare'] > 130)
]
sub_fare = age_with_fares['Fare']
sub_age = age_with_fares['Age']