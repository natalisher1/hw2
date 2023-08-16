import streamlit as st
import seaborn as sns
from matplotlib import pyplot as plt
import statsmodels.api as sm

def firstDropDown(data_frame):
    sd = st.selectbox(
        "Выберите 1 переменную:",
        [
            "year",
            "month",
            "passengers"
        ]
    )

    fig = plt.figure(figsize=(20, 6))
    if sd == "year":
        sns.histplot(x='year', y='passengers', data=data_frame)
    elif sd == "month":
        total = data_frame['month'].value_counts().values.sum()
        def fmt(x):
            return '{:.1f}%\n{:.0f}'.format(x, total*x/100)
        plt.pie(data_frame['month'].value_counts().values, labels=data_frame['month'].value_counts().index, autopct=fmt)
    else: 
        sns.violinplot(x="passengers", y="year",data=data_frame)
    st.pyplot(fig)
    
def secondDropDown(data_frame):
    sd = st.selectbox(
        "Выберите 2 переменную:",
        [
            "year",
            "month",
            "passengers"
        ]
    )

    fig = plt.figure(figsize=(20, 6))
    if sd == "year":
        sns.histplot(x='year', y='passengers', data=data_frame)
    elif sd == "month":
        total = data_frame['month'].value_counts().values.sum()
        def fmt(x):
            return '{:.1f}%\n{:.0f}'.format(x, total*x/100)
        plt.pie(data_frame['month'].value_counts().values, labels=data_frame['month'].value_counts().index, autopct=fmt)
    else: 
        sns.violinplot(x="passengers", y="year",data=data_frame)
    st.pyplot(fig)

def dropDown(data_frame):
    sd = st.selectbox(
        "Выберите гипотезу:",
        [
            "A/B тестирование",
            "t-test"
        ]
    )

    if sd == "A/B тестирование":
        ax = data_frame.boxplot(by='month', column='passengers',
                           figsize=(4, 4))
        ax.set_xlabel('months')
        ax.set_ylabel('passengers')
        plt.suptitle('')
        st.pyplot(plt)
    elif sd == "t-test":
        tstat, pvalue, df = sm.stats.ttest_ind(
            data_frame[data_frame.month == 'Jan'].passengers, 
            data_frame[data_frame.month == 'May'].passengers, 
            usevar='unequal', alternative='smaller')
        st.write(f'p-value: {pvalue:.4f}')
        
def run():
    st.title("Flights")
    data_frame = sns.load_dataset("flights")
    if data_frame is None:
        st.write("Нельзя загрузить датасет")
    else:
        st.write("Датасет успешно загружен")
        st.dataframe(data_frame)

    firstDropDown(data_frame=sns.load_dataset('flights'))
    secondDropDown(data_frame=sns.load_dataset('flights'))
    dropDown(data_frame=sns.load_dataset('flights'))

run()