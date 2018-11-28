import pandas as pd


class CreditorsInfo():
    df = None
    creditors = []

    def __read_csv__(self):
        df = pd.read_csv('UnGastos/static/data/credores_natureza_pago.csv')

        df_greatest = df.head(10)

        df_greatest['Pago'] = df_greatest['Pago'].round()

        self.df = df_greatest

    def generate_data(self):
        self.__read_csv__()

        for index, row in self.df.iterrows():
            creditor = Creditor()

            creditor.name = row['Credor']
            creditor.nature = row['Natureza Detalhada']
            creditor.paid = row['Pago']
            creditor.pos = index + 1

            self.creditors.append(creditor)


class Creditor():
    name = None
    nature = ''
    paid = 0
    pos = 0
