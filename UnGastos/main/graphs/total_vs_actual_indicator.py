import pandas as pd
import plotly


class TotalVsActual():

    total = 1087000000
    df = None

    def __read_csv__(self):
        df = pd.read_csv('UnGastos/static/data/payments.csv')
        df = df.sort_values(by=['Pago'], ascending=True)

        self.df = df

    def generate_graphic(self):
        self.__read_csv__()
        actual = self.df['Pago'].sum()

        labels = ['Gasto', 'Restante']

        layout = {
            'title': 'Valor gasto versus Valor do orçamento restante'
        }

        data = {
            'values': [actual, self.total - actual],
            'labels': labels,
            'hoverinfo': 'label+percent',
            'hole': .4,
            'type': 'pie',
            }

        config = {'displayModeBar': False}

        plotly.offline.plot(
            {'data': [data], 'layout': layout},
            filename='UnGastos/main/templates/total_vs_actual_indicator.html',
            config=config)






