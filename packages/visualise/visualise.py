import plotly.express as px
import plotly.io as pio
import pandas as pd

def plot_bar(data, x, y, color=None, labels=None, title=None, **kwargs):
    fig = px.bar(data, x=x, y=y, color=color, labels=labels, title=title,
                 **kwargs)
    pio.write_html(fig, file=f'/result/{title}.html')


def plot_histogram(data, x, color=None, marginal='rug', labels=None,
                   title=None, **kwargs):
    fig = px.histogram(data, x=x, color=color, marginal=marginal,
                       labels=labels, title=title, **kwargs)
    fig.update_traces(opacity=0.75)
    pio.write_html(fig, file=f'/result/{title}.html')


def plot_heatmap(data, labels=None, title=None, color_scale='Blues'):
    fig = px.imshow(data,
                    labels=labels,
                    color_continuous_scale=color_scale,
                    title=title)
    pio.write_html(fig, file=f'/result/{title}.html')


def plot_bar_gender(data_path):
    data = pd.read_csv(data_path)
    gender_survival_count = data.groupby(['Sex', 'Survived']).size().reset_index(
        name='Count')
    plot_bar(gender_survival_count, x='Survived', y='Count', color='Sex',
            labels={'Survived': 'Survived', 'Count': 'Count'},
            title='Survival Count by Gender')

def plot_hist_age(data_path):
    data = pd.read_csv(data_path)
    result_path = '/result/hist_age.html'
    plot_histogram(data[data['Survived'] == 1], x='Age', color='Sex',
               marginal='rug', labels={'Age': 'Age', 'count': 'Count'},
               title='Age Distribution of Survivors by Gender')

def plot_hist_fare(data_path):
    data = pd.read_csv(data_path)
    plot_histogram(data[data['Survived'] == 1], x='Fare', color='Sex',
               marginal='rug', labels={'Fare': 'Fare', 'count': 'Count'},
               title='Fare Distribution of Survivors by Gender')

def plot_heat_class_gender(data_path):
    data = pd.read_csv(data_path)
    survival_rate = data.groupby(['Pclass', 'Sex']).mean()['Survived']\
        .reset_index()
    plot_heatmap(
        data=survival_rate.pivot('Pclass', 'Sex', 'Survived').values,
        labels=dict(x="Sex", y="Passenger Class", color="Survival Rate"),
        title='Survival Rate by Passenger Class and Gender',
        color_scale='Blues'
    )