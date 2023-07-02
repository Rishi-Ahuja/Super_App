import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

bridge_types=('Arch','Beam','Truss','Cantilever','Tied Arch','Suspension','Cable')
bridge_df=pd.DataFrame(bridge_types, columns = ['bridge_types'])

'''
#convert the colum into category codes
bridge_df['bridge_types']=bridge_df['bridge_types'].astype('category')

#assign a numerical value to the codes and stored them into a new column
bridge_df['bridge_types_cat']=bridge_df['bridge_types'].cat.codes

'''
#create instance of the Label Encoder
labelencoder=LabelEncoder()
onehotencoder = OneHotEncoder(handle_unknown='ignore')

bridge_df['bridge_types_cat'] = labelencoder.fit_transform(bridge_df['bridge_types'])

print(bridge_df)

#pass the bridge types

onehotencoder_df=pd.DataFrame(onehotencoder.fit_transform(bridge_df[['bridge_types_cat']]).toarray())

#merge with the data
bridge_df=bridge_df.join(onehotencoder_df)

print(bridge_df)
