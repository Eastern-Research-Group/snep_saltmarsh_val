import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from typing import Dict, List
from matplotlib.colors import ListedColormap
import contextily as cx
import rioxarray as rx

# Function to convert to sentence case
def to_sentence_case(s):
    return s.capitalize()

def add_missing_cats(df: pd.DataFrame, keys: list[str], var_wanted:str) -> pd.DataFrame:
    """Add missing inundation categories to dataframe for plotting

    Args:
        df (pd.DataFrame): _description_
        keys (list[str]): _description_
        var_wanted (str): _description_

    Returns:
        pd.DataFrame: dataframe with empty categories for graphing
    """
    missing_keys = set(keys) - set(df['inun_freq_leg'].unique())
    extra_df = pd.DataFrame([
        {
            'inun_freq_leg': missing_key,
            var_wanted: 0,
            'year': df["year"].iloc[0],
            'marsh': 'no marsh'
        }
    for missing_key in missing_keys])
    df_full = pd.concat([df, extra_df])
    return df_full


def create_categorical_cmap(colorDict: Dict[str, str], categories: List[str], sort: bool = True) -> ListedColormap:
    """Creates categorical color map

    Args:
        colorDict (Dict[str, str]): _description_
        categories (List[str]): _description_

    Returns:
        ListedColormap: _description_
    """
    if sort:
        return ListedColormap([colorDict[x] for x in sorted(categories)])
    return ListedColormap([colorDict[x] for x in categories])

def plot_stack_bar(combined_wanted:pd.DataFrame, var_wanted:str, title:str, xlabel:str, output_path:str):
    """Plot a stacked bar graph of inundation frequency results

    Args:
        combined_wanted (pd.DataFrame): specific sea level rise and year for the marsh
        var_wanted (str): what variable you're plotting
        title (str): plot title
        xlabel (str): x axis label
        output_path (str): output path to save the plot

    Returns:
        _type_: plot
    """
    
    # Set naming convention for categories
    inun_freq_key_list = [
        [0, 'Always',], 
        [1, 'At least every 30-days',], 
        [2, 'At least every 60-days'], 
        [3, 'At least every 90-days'], 
        [4, '10-year storm surge'], 
        [5, '100-year storm surge'], 
        [8, 'protected by dikes']
    ]

    inun_freq_key_df = pd.DataFrame(inun_freq_key_list, columns=['inun_freq_code', 'inun_freq_leg'])
    combined_wanted = combined_wanted.merge(inun_freq_key_df, on='inun_freq_code', how='left')

    # set order of bar plot
    order = [
        'Always', 
        'At least every 30-days',
        'At least every 60-days',
        'At least every 90-days',
        '10-year storm surge',
        '100-year storm surge'
    ]

    # Make sure all categories are in the dataframe
    complete_df = add_missing_cats(combined_wanted, order, var_wanted)
    
    # prepare dataframe for plotting
    complete_df['marsh'] = complete_df['marsh'].apply(to_sentence_case)
    complete_df = complete_df[complete_df['inun_freq'] != 'protected by dikes']
    complete_df['marsh'] = complete_df['marsh'].str.replace(' ', '\n')
    pivoted_df = complete_df.groupby(["marsh", "inun_freq_leg"])[var_wanted].sum().unstack()
    order_idxs = [idx for val in order for idx in np.where(pivoted_df.columns == val)[0]]

    # plot the stacked bar graph
    fig, ax = plt.subplots(figsize=(15, 10))
    pivoted_df.iloc[:, order_idxs].plot(
        ax=ax, 
        kind="barh", 
        stacked=True,
        #cmap=create_categorical_cmap(inun_colors, complete_df["inun_freq"].unique()),
        color=['#A50026', '#EA5739', '#FDBF71', '#FEFFC0', '#BDE2EE', '#6399C7'],
        ylabel=''
    )
    plt.title(title, fontsize=16)
    plt.xlabel(xlabel, fontsize=24)
    plt.xticks(fontsize=24)
    plt.yticks(fontsize=24)
   # ax.set_xticklabels(['{:,}'.format(int(x)) for x in ax.get_xticks().tolist()])
    ax.spines[['right', 'top']].set_visible(False)
    legend = plt.legend(title = "Flooding Frequency", fontsize=18, bbox_to_anchor = (1,0.5), frameon=False)
    legend.get_title().set_fontsize('20')

    # save the figure
    fig.savefig(output_path, dpi=350, bbox_inches="tight")
    
    return pivoted_df


def make_map(rast_file_path, map_zoom, output_path):

    # read in tif file
    rast_file = rx.open_rasterio(rast_file_path)

    # make map
    fig, ax = plt.subplots(figsize=(15, 10))
    rast_file.plot(ax=ax, levels=[0,1,2,3,4,5,6,8,9],cmap="RdYlBu_r", alpha=0.5)
    cx.add_basemap(ax, source=cx.providers.CartoDB.Positron, zoom=map_zoom, crs=rast_file.rio.crs)
    ax.set_xticks([])
    ax.set_yticks([])

    # save map
    fig.savefig(output_path, dpi=350, bbox_inches="tight")

    return fig

