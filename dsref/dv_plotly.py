#%%
#basic imports 
import plotly.offline as py   # Everything should work the same if you want online, just change to plotly.plotly as py (need to check)
import plotly.graph_objs as go
from plotly import __version__
print(f'Plotly loaded - version {__version__}')

#%%
import numpy as np
x = np.random.randn(2000)
y = np.random.randn(2000)
py.iplot(
    [
        go.Histogram2dContour(x=x, y=y, contours=dict(coloring='heatmap')),
        go.Scatter(x=x, y=y, mode='markers', marker=dict(color='white',size=3,opacity=0.3))
    ],
    show_link=False
)
