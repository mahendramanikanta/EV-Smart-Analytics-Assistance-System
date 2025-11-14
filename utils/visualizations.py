# utils/visualizations.py

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("darkgrid")

def plot_range_distribution(df):
    fig, ax = plt.subplots(figsize=(8,4))
    sns.histplot(df["Electric Range"], kde=True, ax=ax)
    ax.set_title("EV Range Distribution")
    return fig

def plot_top_makes(df):
    fig, ax = plt.subplots(figsize=(8,4))
    top = df["Make"].value_counts().head(10)
    sns.barplot(x=top.values, y=top.index, ax=ax)
    ax.set_title("Top 10 Manufacturers")
    return fig

def plot_range_by_year(df):
    fig, ax = plt.subplots(figsize=(10,5))
    sns.boxplot(data=df, x="Model Year", y="Electric Range", ax=ax)
    plt.xticks(rotation=45)
    ax.set_title("Range by Model Year")
    return fig
