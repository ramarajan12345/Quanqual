class Univariate():
    def quanqual(dataset):
        qual=[]
        quan=[]
        for columnName in dataset.columns:
            #print(columnName)
            if(dataset[columnName].dtype=='object'):
                #print("qual")
                qual.append(columnName)
            else:
               # print("quan")
                quan.append(columnName)
        return quan, qual
