def filter_character(dataframe,column,filter):
    if filter[0]=='>':
        filt_df=dataframe[dataframe[column]>filter[1]]
    if filter[0]=='<':
        filt_df=dataframe[dataframe[column]<filter[1]]
    if filter[0]=='=':
        filt_df=dataframe[dataframe[column]==filter[1]]
    return filt_df