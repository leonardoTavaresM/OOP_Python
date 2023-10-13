class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatada(self):

        if (self.dia and self.mes and self.ano):
            print("{}/{}/{}".format(self.dia, self.mes,self.ano))
        else:
            print('precisa adicionar uma data no objeto')

d = Data(21,11,2007)
d.formatada()

