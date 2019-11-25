# coding: utf-8

# Katlego Madisha's seaborn visualisation simplification attempt package
# https://github.com/katlegomfx


#Visualisations
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os, shutil

def dist_plot(df,group=None):
    fig = plt.figure(figsize=(20, 10))
    sns_plot =sns.distplot(df[group])
    fig=sns_plot.get_figure()
    plt.title('Distribution plot of '+group)
    plt.ylabel('frequency')
    plt.xticks(rotation='45')
    plt.savefig('distribution plot of '+group+'.png', transparent=True)
    plt.show()
    print('min= ', np.min(df[group]))
    print('mean=', np.mean(df[group]))
    print('standard_deviation= ',np.std(df[group]))
    print('max= ', np.max(df[group]))

def scat_plot(df,group=None,group1=None):
    fig = plt.figure(figsize=(20, 10))
    sns_plot =plt.scatter(x=df[group], y=df[group1])
    fig=sns_plot.get_figure()
    plt.title('Scatter plot of '+group+' vs '+group1)
    plt.xlabel(group)
    plt.ylabel(group1)
    plt.xticks(rotation='45')
    plt.savefig('scatter plot of'+group+group1+'.png', transparent=True)
    plt.show()
    
def swarm_vio_plot(df,group=None,group1=None):
    fig = plt.figure(figsize=(10, 10))
    sns_plot =sns.violinplot(data = df, x = group, y=group1)
#     sns_plot1 =sns.swarmplot(data = df, x = group, y=group1, color = 'k', alpha = 0.6)
    fig=sns_plot.get_figure()
#     fig=sns_plot1.get_figure()
    plt.title('Swarm Violin plot of '+group + ' vs ' + group1)
    plt.xlabel(group)
    plt.ylabel(group1)
    plt.xticks(rotation='45')
    plt.show()
    
def box_plot(df,group=None, group1=None):
    fig = plt.figure(figsize=(20, 10))
    sns_plot =sns.boxplot(data = df, x = group, y=group1)
    fig=sns_plot.get_figure()
    plt.title('Box plot of '+group + ' vs ' + group1)
    plt.xlabel(group)
    plt.ylabel(group1)
    plt.xticks(rotation='45')
    plt.show()
    
def count_plot(df,group=None):
    df = df.sort_values(group)
    fig = plt.figure(figsize=(20, 10))
    sns_plot =sns.countplot(data = df, x = group)
    fig=sns_plot.get_figure()
    plt.title('Count plot of '+ group)
    plt.xlabel(group)
    plt.xticks(rotation='45')
    plt.savefig('count plot of '+group+'.png', transparent=True)
    plt.show()
    
def bar_plot(df,group=None,group1=None,compare=None):
    df = df.sort_values(group)
    fig = plt.figure(figsize=(20, 10))
    sns_plot =sns.barplot(x=group, y =group1,hue=compare,data=df)
    fig=sns_plot.get_figure()
    plt.title('Bar plot of '+group+' vs '+group1)
    plt.xlabel(group)
    plt.ylabel(group1)
    plt.xticks(rotation='45')
    plt.savefig('bar plot of '+group+group1+'.png', transparent=True)
    plt.show()