import matplotlib.pyplot as plt
from dissect.analysis.data_processing import get_all, filter_df
from dissect.analysis.widgets import get_choices
from ipywidgets import widgets, interact, fixed
from IPython.display import display

def violin(df, feature):
    plt.figure(figsize=(12,8), dpi=100, facecolor='w', edgecolor='k')
    plt.violinplot([df[feature].tolist()])
    plt.show()

def normalized_barplot(
        ax,
        df,
        param,
        feature,
        modifier=lambda x: x,
        title=None,
        tick_spacing=0,
        xlab="Values",
        ylab="Normalized count",
        drop_timeouts=True,
):
    # make a copy of the dataframe, drop timeouts if eligible and apply the modifier function to the feature row
    df2 = df.copy(deep=False)
    if drop_timeouts:
        df2 = df2[df2[feature] != "NO DATA (timed out)"]
    df2[feature] = df2[feature].apply(modifier)

    # classify entries and count them
    std = df2[df2["standard"] == True]
    sim = df2[df2["standard"] == False]
    if len(df2) == 0:
        return
    df2_counts = df2[feature].value_counts() / len(df2)

    # choose suitable x-axis ticks
    if tick_spacing == 0:
        ticks = sorted(list(df2_counts.index))
        locs = range(len(ticks))
        labels = ticks
    else:
        low = min(df2_counts.index) - (min(df2_counts.index) % tick_spacing)
        high = (
                max(df2_counts.index)
                - (max(df2_counts.index) % tick_spacing)
                + tick_spacing
        )
        ticks = range(low, high + 1)
        locs = [i for i in range(len(ticks)) if i % tick_spacing == 0]
        labels = [t for t in ticks if t % tick_spacing == 0]

    # create the normalized barplot
    if not len(std) == 0:
        std_counts = std[feature].value_counts() / len(std)
        ax.bar(
            std_counts.index.map(ticks.index) - 0.2,
            std_counts.values,
            width=0.4,
            label=f"Standard curves n={len(std)}",
        )
    if not len(sim) == 0:
        sim_counts = sim[feature].value_counts() / len(sim)
        ax.bar(
            sim_counts.index.map(ticks.index) + 0.2,
            sim_counts.values,
            width=0.4,
            label=f"Simulated curves n={len(sim)}",
        )
    if len(param) > 0 and title is None:
        p, v = param.popitem()
        # title = f"Normalized barplot of {feature} for {p}={v[0]}"
        title = f"{p}={v[0]}"
        ax.title.set_text(title)
    ax.set_xticks(locs)
    ax.set_xticklabels(labels)
    ax.legend()
    ax.set_xlabel(xlab)
    ax.set_ylabel(ylab)


def multiplot(height, width, columns, trait_df, filtering_widgets, modifier=None, tick_spacing=None):
    custom_modifier = True if modifier != None else False
    results = get_all(trait_df, get_choices(filtering_widgets))
    nrows = len(results) // columns + 1
    fig, axes = plt.subplots(figsize=(width, height), nrows=nrows, ncols=columns)
    if nrows == 1 and columns == 1:
        axes = [axes]
    fig.tight_layout(pad=4.0, rect=[0, 0.03, 1, 0.95])
    if nrows > 1 and columns > 1:
        axes = [item for sublist in axes for item in sublist]
    for ax in axes[len(results):]:
        fig.delaxes(ax)
    for result, ax in zip(results, axes):
        df, param, feature, picked_modifier, modifier_name = result
        picked_modifier = modifier if custom_modifier else picked_modifier
        picked_tick_spacing = tick_spacing if tick_spacing != None else 0
        normalized_barplot(ax, df, param, feature, picked_modifier, tick_spacing=picked_tick_spacing)
    modifier_title = "custom" if custom_modifier else modifier_name
    title = f"Normalized barplot of {feature} with modifier: {modifier_title}"
    fig.suptitle(title)
    return fig


def change_size(figure, width, height):
    figure.set_figheight(height)
    figure.set_figwidth(width)
    display(figure)


def interact_multiplot(trait_df, filtering_widgets, modifier=None, tick_spacing=0, columns=1):
    def_height, def_width = 10, 7
    fig = multiplot(def_height, def_width, columns, trait_df, filtering_widgets, modifier=modifier,
                    tick_spacing=tick_spacing)
    plt.close()
    heightSlider = widgets.IntSlider(description='height', min=1, max=30, step=1, value=10)
    widthSlider = widgets.IntSlider(description='width', min=1, max=30, step=1, value=7)
    ui = widgets.HBox([heightSlider, widthSlider])
    out = widgets.interactive_output(change_size, {'width': widthSlider, 'height': heightSlider, 'figure': fixed(fig)})
    display(ui, out)
    return filter_df(trait_df, get_choices(filtering_widgets))
