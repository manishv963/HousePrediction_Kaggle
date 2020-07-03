# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np
from num2words import num2words


filename = 'housePredictorUsingRandomFores.pkl'
classifier = pickle.load(open(filename, 'rb'))

app = Flask(__name__)


@app.route('/')
def home():
	return render_template('index.html')



@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        #MasVnrArea = int(request.form['MasVnrArea'])
        
        
        #BsmtFinSF1 = float(request.form['BsmtFinSF1'])
        #TotalBsmtSF = float(request.form['TotalBsmtSF'])
        #FirststFlrSF  = float(request.form['1stFlrSF'])
        #SecondFlrSF  = float(request.form['2ndFlrSF'])
        #GrLivArea = float(request.form['GrLivArea'])
        #GarageYrBlt = float(request.form['GarageYrBlt'])
        #GarageArea = float(request.form['GarageArea'])
        #PoolArea= float(request.form['PoolArea'])
        #PoolQC = int(request.form['PoolQC'])
        #LotArea = float(request.form['LotArea'])
        #YrSold=float(request.form['YrSold'])
        
        overAllQuality = str(request.form['overAllQuality'])
        mszoning = int(request.form['mszoning'])
        MSZoning_RL=0
        if(mszoning == 1):
            MSZoning_RL=1
        
        TotalBsmtSF = float(request.form['TotalBsmtSF'])
        SecondFlrSF  = float(request.form['2ndFlrSF'])
        bldgType = int(request.form['BldgType'])
        BldgType_2fmCon = 0
        if(bldgType == 1 ):
            BldgType_2fmCon= 1
        exteriorQuality= str(request.form['exteriorQuality'])
        ExterQual_Fa = 0
        ExterQual_TA = 0
        ExterQual_Gd=0
        if(exteriorQuality == "ExterQual_Gd"):
            ExterQual_Gd=1
        elif(exteriorQuality == "ExterQual_TA"):
            ExterQual_TA=1
        else:
            ExterQual_Fa=1
        Heating_GasW =0
        Heating_Wall  = 0
        heatingQuality = str(request.form['heatingQuality'])
        if(heatingQuality == "Heating_GasW"):
            Heating_GasW=1
        else:
            Heating_Wall=1
        SaleType_CWD    =   0
        SaleType_Con    =   0
        SaleType_ConLD =      0
        SaleType_New     =    0
        saleType = str(request.form['saleType'])
        if(saleType == "SaleType_CWD"):
            SaleType_CWD=1
        elif(saleType == "SaleType_Con"):
            SaleType_Con=1
        elif(saleType == "SaleType_ConLD"):
            SaleType_ConLD=1
        else:
            SaleType_New=1

        Street_Pave = 0
        streetType= str(request.form['streetType'])
        if(streetType == "SaleType_CWD"):
            Street_Pave=1
        data = np.array([[overAllQuality, TotalBsmtSF, SecondFlrSF, MSZoning_RL, BldgType_2fmCon, ExterQual_Fa,ExterQual_Gd,ExterQual_TA,Heating_GasW,Heating_Wall,SaleType_CWD,
        SaleType_Con ,SaleType_ConLD,SaleType_New,Street_Pave]])
        my_prediction = classifier.predict(data)
        print(my_prediction)



        #mtFlrSF = str(request.form['streetType'])
        #lotShape = str(request.form['lotShape'])
        #Neighborhood = str(request.form['Neighborhood'])
        
        
        #bldgType = str(request.form['bldgType'])
        ##HouseStyle = str(request.form['HouseStyle'])
        #overALlQuality = str(request.form['overALlQuality'])
        #yearBuilt = int(request.form['yearBuilt'])
        #roofStyle = str(request.form['roofStyle'])
        #LowQualFinSF = int(request.form['LowQualFinSF'])
        #FullBath = int(request.form['FullBath'])
        #HalfBath = int(request.form['HalfBath'])
        #Bedrooms = int(request.form['Bedrooms'])
        #kitchenNumber = int(request.form['kitchenNumber'])
        #kitchenQuality = str(request.form['kitchenQuality'])
        #firePlaceQuality = str(request.form['firePlaceQuality'])
        #garageQuality = str(request.form['garageQuality'])
        #fenceeQuality= str(request.form['fenceeQuality'])
        #MiscFeature= str(request.form['MiscFeature'])
        #MiscVal  = float(request.form['MiscVal'])
        #                monthSold= float(request.form['monthSold'])
        #                SaleCondition= str(request.form['SaleCondition'])
        #                SaleType= str(request.form['SaleType'])
        
        #yearSOld = int(request.form['yearSold'])
        predictioninNum =round(float(my_prediction))
        
        my_prediction = (num2words(predictioninNum)).capitalize()
        return render_template('result.html', prediction=my_prediction,predictioninNum=predictioninNum)
        

    
if __name__ == '__main__':
	app.run(debug=True)