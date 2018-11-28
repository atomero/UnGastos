import pandas as pd
import plotly
import plotly.graph_objs as go


class ExpensesMonth():
    df = None

    def __read_csv__(self):
        df = pd.read_csv('UnGastos/static/data/expenses_per_month.csv')
        df = df.sort_values(by=['Pago'], ascending=True)

        df_greatest = df.head(12)

        self.df = df_greatest

    def generate_graphic(self):
        self.__read_csv__()

        data = [
            go.Bar(
                x=self.df['Pago'],
                y=self.df['Mes'],
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
            title='Gastos por Mês',
            margin=go.layout.Margin(
                l=275,
            )
        )

        config = {'displayModeBar': False}

        plotly.offline.plot({
            "data": data,
            "layout": layout
            },
            filename='UnGastos/main/templates/expenses_per_month.html',
            config=config
        )
