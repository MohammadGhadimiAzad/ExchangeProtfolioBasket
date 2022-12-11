!pip install yfinance
import sys
from numpy import mean
from numpy import std
from numpy import amax
from numpy.random import randn
from numpy.random import seed
from matplotlib import pyplot
from scipy.stats import pearsonr
import pandas as pd
import json
import datetime
import yfinance as yf
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from scipy import stats

def GetSlope(usd_name):
  def GetData(usd, startDate, endDate):
      fromDate = startDate
      toDate = endDate
      df = yf.download(usd, fromDate, toDate, interval = "1d")[['Close']]#, 'Open', 'Low', 'High', 'Volume']]
      return df.to_json()

  from datetime import datetime
  sDate = datetime.fromisoformat('2021-10-01')
  eDate = datetime.fromisoformat('2022-11-01')

  dataCoin = GetData(usd_name+'-USD', sDate, eDate)

  dataset = pd.read_json(dataCoin)
  data_set = dataset.iloc[:, 0:1].values

  sc = MinMaxScaler(feature_range = (0, 1))
  data_set_scaled = sc.fit_transform(data_set)

  L = len(data_set_scaled)

  plt.figure(figsize=(10,5))
  plt.plot(data_set_scaled, color = '#666666', label = 'Price')
  x = list(range(0, L))
  y = [i[0] for i in data_set_scaled]

  slope, intercept, r, p, std_err = stats.linregress(x, y)

  def myfunc(x):
    return slope * x + intercept

  mymodel = list(map(myfunc, x))

  plt.title(usd_name)
  # plt.scatter(x, y)
  plt.plot(x, mymodel)
  plt.legend()
  plt.show()
  plt.savefig('/content/sample_data/Images2/'+usd_name+'.png', format = 'png', transparent=True)

  return (slope)

coins = ['ETH','BNB']#,'USDT','SOL1','ADA','XRP','USDC','DOT1','HEX','DOGE','AVAX','SHIB','CRO','LUNA1','LTC','UNI3','MATIC','LINK','BCH','ALGO','MANA','EGLD','AXS','XLM','VET','ICP1','FIL','FTT1','TRX','THETA','DAI1','SAND','ETC','HBAR','ATOM1','FTM','GRT2','HNT1','XMR','XTZ','MIOTA','EOS','LRC','FLOW1','ZEC','ENJ','AAVE','CAKE','MKR','RUNE','ONE2','BSV','KDA','KSM','NEO','CHZ','QNT','AMP1','STX1','BAT','CRV','HOT1','BTT1','WAVES','DASH','AR','CELO','TFUEL','COMP','IOTX','XEM','QTUM','DCR','WAXP','ZEN','TUSD','CTC1','XDC','ANKR','ICX','SC','OMG','ROSE','VGX','STORJ','YFI','RVN','HIVE','ZIL','CEL','BTG','OMI','CCXX','ZRX','SUSHI','BNT','DFI','VLX','CKB','SNX','UMA','ONT','SKL','RAY','KAVA','IOST','SRM','WIN1','XWC','1INCH','DGB','CELR','NANO','GLM','GNO','C98','FET','NU','LSK','RSR','CTSI','SXP','ZEL','MED','XVG','TWT','CVC','VTHO','OXT','NKN','COTI','SNT','ARRR','SYS','BCD','ARDR','STMX','XCH','RLC','ACH','ZNN','EWT','STEEM','VRA','TOMO','ARK','STRAX','ABBC','MCO','SAPP','ETN','BAND','REP','ERG','NMR','MAID','DAG','FUN','DERO','MIR1','DIVI','ANT','MTL','MLN','META','WAN','PHA','HNS','XHV','POA','RBTC','CLV','BTS','BAL','IRIS','AVA','ATRI','KMD','KIN','TT','AION','MONA','DNT','NYE','XAS','XNC','FIRO','ADX','CUDOS','MWC','GAS','ELA','NRG','DMCH','BTM','REV','WTC','GRS','PAC','FIO','WOZX','RDD','SBD','BCN','DGD','FRONT','APL','BEAM','CET','MARO','AE','BEPRO','CRU','VITE','PIVX','NULS','VSYS','NIM','VERI','FSN','AXEL','SOLVE','GXC','XCP','NXS','GAME','SERO','GO','CTXC','PPT','CUT','PCX','LOKI','WICC','KRT','PPC','VTC','GRIN','ZANO','MHC','OBSR','GBYTE','SRK','NVT','NAV','VAL1','NMC','ADK','WABI','QASH','QRL','HC','NAS','SCP','LBC','PART','XSN','AMB','NEBL','MASS','RSTR','CHI','RINGX','BIP','MAN','PAI','FCT','ETP','FO','NXT','DTEP','HTML','PZM','PAY','DCN','SALT','TRUE','PI','BTC2','DMD','YOYOW','MRX','BHP','LCC','PLC','NLG','EMC2','HPB','DNA1','SCC3','UBQ','BLOCK','XDN','ACT','DYN','IDNA','SFT','AEON','POLIS']
for c in coins:
  try:
    print(c)
    data = GetData(c+'-USD', sDate, eDate)
    print(GetSlope(c))
  except:
    pass
