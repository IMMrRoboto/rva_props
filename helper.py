
# coding: utf-8

# In[ ]:


import pickle
import pandas as pd


# In[ ]:


def savePickle(dataFrame, pickleName="df_pickle.p"):
    pickle.dump( dataFrame, open( pickleName, "wb" ) )


# In[ ]:


def loadPickle(path_to_pickle):
    return pickle.load( open(path_to_pickle , "rb" ) )


# In[ ]:


def saveCSV(dataFrame, csvName='merged_data.csv'):
    dataFrame.to_csv(csvName)


# In[ ]:


def changeToNumeric(dataFrame, columnArr):
    for col in columnArr:
        dataFrame[col] = pd.to_numeric(dataFrame[col],errors='coerce')
    return dataFrame


# In[ ]:


# Below functions written by StackOverflow user: abw333
# URL: https://stackoverflow.com/a/38216118
def mode(df, key_cols, value_col, count_col):
    '''                                                                                                                                                                                                                                                                                                                                                              
    Pandas does not provide a `mode` aggregation function                                                                                                                                                                                                                                                                                                            
    for its `GroupBy` objects. This function is meant to fill                                                                                                                                                                                                                                                                                                        
    that gap, though the semantics are not exactly the same.                                                                                                                                                                                                                                                                                                         

    The input is a DataFrame with the columns `key_cols`                                                                                                                                                                                                                                                                                                             
    that you would like to group on, and the column                                                                                                                                                                                                                                                                                                                  
    `value_col` for which you would like to obtain the mode.                                                                                                                                                                                                                                                                                                         

    The output is a DataFrame with a record per group that has at least one mode                                                                                                                                                                                                                                                                                     
    (null values are not counted). The `key_cols` are included as columns, `value_col`                                                                                                                                                                                                                                                                               
    contains a mode (ties are broken arbitrarily and deterministically) for each                                                                                                                                                                                                                                                                                     
    group, and `count_col` indicates how many times each mode appeared in its group.                                                                                                                                                                                                                                                                                 
    '''
    return df.groupby(key_cols + [value_col]).size()              .to_frame(count_col).reset_index()              .sort_values(count_col, ascending=False)              .drop_duplicates(subset=key_cols)

def modes(df, key_cols, value_col, count_col):
    '''                                                                                                                                                                                                                                                                                                                                                              
    Pandas does not provide a `mode` aggregation function                                                                                                                                                                                                                                                                                                            
    for its `GroupBy` objects. This function is meant to fill                                                                                                                                                                                                                                                                                                        
    that gap, though the semantics are not exactly the same.                                                                                                                                                                                                                                                                                                         

    The input is a DataFrame with the columns `key_cols`                                                                                                                                                                                                                                                                                                             
    that you would like to group on, and the column                                                                                                                                                                                                                                                                                                                  
    `value_col` for which you would like to obtain the modes.                                                                                                                                                                                                                                                                                                        

    The output is a DataFrame with a record per group that has at least                                                                                                                                                                                                                                                                                              
    one mode (null values are not counted). The `key_cols` are included as                                                                                                                                                                                                                                                                                           
    columns, `value_col` contains lists indicating the modes for each group,                                                                                                                                                                                                                                                                                         
    and `count_col` indicates how many times each mode appeared in its group.                                                                                                                                                                                                                                                                                        
    '''
    return df.groupby(key_cols + [value_col]).size()              .to_frame(count_col).reset_index()              .groupby(key_cols + [count_col])[value_col].unique()              .to_frame().reset_index()              .sort_values(count_col, ascending=False)              .drop_duplicates(subset=key_cols)
            
# mode(scale_test_input, ['key'], 'value', 'count')
'''   key value  count
1    1     B      2
2    3     C      2'''

# modes(scale_test_input, ['key'], 'value', 'count')
'''   key  count   value
1    1      2     [B]
2    3      2  [C, D]'''

