import pandas as pd
import plotly
import plotly.graph_objs as go


class DetailedNature():
    df = None

    def __read_csv__(self):
        df = pd.read_csv('UnGastos/static/data/detailed_nature.csv')
        self.df = df

    def generate_graphic(self):
        self.__read_csv__()

        data = [
            go.Bar(
                x=self.df['Nome Natureza Detalhada'],
                y=self.df['Pago'],
                marker=dict(
                    color='rgb(158,202,225)',
                    line=dict(
                        color='rgb(8, 48 ,107)',
                        width=1.5)
                ))
        ]

        plotly.offline.plot({
            "data": data,
            "layout": go.Layout(title="Gastos por Natureza")
            },
            filename='UnGastos/main/templates/detailed_nature.html'
        )
