!wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz
!tar -xzvf ta-lib-0.4.0-src.tar.gz
%cd ta-lib
!./configure --prefix=/usr
!make
!make install
!pip install Ta-Lib
import pandas as pd
import requests
import talib
from talib import RSI,MA_Type

def coincheck(market="BTCUSDT",typ="5min",limit=60):
    result = requests.get('https://api.coinex.com/v1/market/kline?market={market}&type={type}&limit={limit}'.format(market=market,type=typ,limit=limit),
    headers={'Content-Type': 'application/json; charset=utf-8','Accept': 'application/json','User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'})
    get_result = pd.json_normalize(result.json(), ['data'])
    get_result.columns = ['time', 'open', 'close', 'high', 'low', 'volume', 'amount']
    # df=get_result
    # x=df.iloc[48]
    # print(x)
    return get_result


def BolingerBand(dataframe,period=20,deviation=2):
    df = dataframe.copy()
    df['BB_MA']= df['close'].rolling(period).mean()
    df['BB_up'] =df['BB_MA'] + deviation * dataframe['close'].rolling(period).std() 
    df['BB_down']=df['BB_MA'] - deviation * dataframe['close'].rolling(period).std()
    df.dropna(inplace=True)
    return df  


def RSI(dataframe,timePeriod=14):    
    #rsi0=online      rsi1=back candle        rsi2=back 2candle
    L = len(dataframe)    
    dataframe=talib.RSI(dataframe["close"],timeperiod=timePeriod)
    
    rsi0=dataframe.iloc[L-1]
    rsi1=dataframe.iloc[L-2]
    rsi2=dataframe.iloc[L-3]
    return rsi0,rsi1,rsi2

data = coincheck(market="ETHUSDT",typ='1day',limit=30)
result = BolingerBand(data)
print(result)
print(RSI(data))
