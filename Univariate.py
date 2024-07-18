class Univariate():
    def quanQual(dataset):
      quan=[]
      qual=[]

      for colName in dataset.columns:
        #print(colName)
        if(dataset[colName].dtype=='O'):
          #print(colName)
          qual.append(colName) 
        else:
          #print(colName)
          quan.append(colName)
      return quan,qual 

    def Univariate(dataset,quan):
        descriptive=pd.DataFrame(index=["Mean","Median","Mode","Q1:25%","Q2:50%","Q3:75%","99%","Q4:100%","IQR","1.5Rule","Lesser","Greater","Min","Max"],columns=quan)
        for colName in quan:
            descriptive[colName]["Mean"]=dataset[colName].mean()
            descriptive[colName]["Median"]=dataset[colName].median()
            descriptive[colName]["Mode"]=dataset[colName].mode()[0]
            descriptive[colName]["Q1:25%"]=dataset.describe()[colName]["25%"]
            descriptive[colName]["Q2:50%"]=dataset.describe()[colName]["50%"]
            descriptive[colName]["Q3:75%"]=dataset.describe()[colName]["75%"]
            descriptive[colName]["99%"]=np.percentile(dataset[colName],99)
            descriptive[colName]["Q4:100%"]=dataset.describe()[colName]["max"]
            descriptive[colName]["IQR"]=descriptive[colName]["Q3:75%"]-descriptive[colName]["Q1:25%"]
            descriptive[colName]["1.5Rule"]=1.5*descriptive[colName]["IQR"]
            descriptive[colName]["Lesser"]=descriptive[colName]["Q1:25%"]-descriptive[colName]["1.5Rule"]
            descriptive[colName]["Greater"]=descriptive[colName]["Q3:75%"]+descriptive[colName]["1.5Rule"]
            descriptive[colName]["Min"]=dataset[colName].min()
            descriptive[colName]["Max"]=dataset[colName].max()
        return descriptive

     def outliers(colName,quan):
        lesser=[]
        greater=[]
        
        for colName in quan:
            if(descriptive[colName]["Min"]<descriptive[colName]["Lesser"]):
                lesser.append(colName)
            if(descriptive[colName]["Max"]>descriptive[colName]["Greater"]): 
                greater.append(colName)
        return lesser,greater

    def replaceoutliers(colName,dataset):
        for colName in lesser:
          dataset[colName][dataset[colName]<descriptive[colName]["Lesser"]]=descriptive[colName]["Lesser"]
        for colName in greater:
          dataset[colName][dataset[colName]>descriptive[colName]["Greater"]]=descriptive[colName]["Greater"]
        return lesser,greater
    