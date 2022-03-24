import numpy as np
import plotly.graph_objects as go
import pandas as pd
#from mpl_toolkits.mplot3d import Axes3D

if __name__ == '__main__':
    z_data = pd.read_csv("../../../FachProjekt/Aufgabe2/OberflächentopographieDatei.txt", sep=' ', header=None)

    z = z_data.values
    sh_0, sh_1 = z.shape

    fig = go.Figure(data=[go.Surface(z=z_data.values)])

    fig.update_layout(title='demo', autosize=False,
                      width=800, height=800,
                      scene=dict(
                          # 1373 x 441
                          #  429 x 292
                          xaxis=dict(nticks=1, range=[0, 429], ),
                          yaxis=dict(nticks=1, range=[0, 292], ),
                          zaxis=dict(nticks=1, range=[-0.35, 0.35], ), ),
                          #xaxis=dict(nticks=1, range=[0, 441], ),
                          #yaxis=dict(nticks=1, range=[0, 1373], ),
                          #zaxis=dict(nticks=1, range=[-0.1, 0.1], ), ),
                          margin=dict(l=65, r=50, b=65, t=90)
                      )





    fig.show()
