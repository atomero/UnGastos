import pandas as pd
import plotly
import plotly.graph_objs as go


class ResourceSource():
    df = None

    id_use = {
        '1': 'Contrapartida - BIRD',
        '2': 'Contrapartida - BID',
        '3': 'Contrapartida de empréstimos com enfoque setorial amplo',
        '4': 'Contrapartida de outros empréstimos',
        '5': 'Contrapartida de doações',
        '6': 'Recursos não destinados a contrapartida (saúde)',
        '7': 'Recursos não destinados a contrapartida (ensino)',
        '8': 'Transferências e convênios do estado',
        '9': 'Transferências e convênios da união'
    }

    resource_source_destination = {
        '1': 'Recursos do Tesouro – Exercício Corrente',
        '2': 'Recursos de Outras Fontes – Exercício Corrente',
        '3': 'Recursos do Tesouro – Exercícios Anteriores',
        '4': 'Recursos de Outras Fontes – Exercícios Anteriores',
        '5': 'Recursos Condicionados'
    }

    def __read_csv__(self):
        df = pd.read_csv('UnGastos/static/data/resource_source.csv')
        df = df.sort_values(by=['Pago'], ascending=True)
        df['Fonte de Recurso'] = df['Fonte de Recurso'].astype(str)

        self.df = df

    def __parse_resource_source_to_string__(self):

        for resource_source_code in self.df['Fonte de Recurso']:
            # print(resource_source_code[0])
            if resource_source_code[1] in self.resource_source_destination:
                self.df.replace(
                    resource_source_code,
                    self.resource_source_destination[resource_source_code[1]],
                    inplace=True)
            else:
                self.df.replace(resource_source_code, 'Outros', inplace=True)

    def generate_graphic(self):
        self.__read_csv__()
        self.__parse_resource_source_to_string__()

        labels = self.df['Fonte de Recurso']
        values = self.df['Pago']

        trace = go.Pie(labels=labels, values=values)

        config = {'displayModeBar': False}

        filename = 'UnGastos/main/templates/expenses_per_resource_source.html'

        plotly.offline.plot(
            [trace],
            filename=filename,
            config=config)
