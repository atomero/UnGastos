import pandas as pd
import plotly
import plotly.graph_objs as go


class DetailedNature():
    df = None

    def __read_csv__(self):
        df = pd.read_csv('UnGastos/static/data/detailed_nature.csv')
        df = df.sort_values(by=['Pago'], ascending=False)

        df_greatest = df.head(10)

        self.df = df_greatest

    def generate_graphic(self):
        self.__read_csv__()

        data = [
            go.Bar(
                x=self.df['Pago'],
                y=self.df['Nome Natureza Detalhada'],
                marker=dict(
                    color='rgb(158,202,225)',
                    line=dict(
                        color='rgb(8, 48 ,107)',
                        width=1.5)
                ),
                orientation='h'
            ),
        ]

        layout = go.Layout(
            title='Gastos por Natureza',
            margin=go.layout.Margin(
                l=325,
            )
        )

        config = {'displayModeBar': False}

        plotly.offline.plot({
            "data": data,
            "layout": layout
            },
            filename='UnGastos/main/templates/detailed_nature.html',
            config=config
        )
