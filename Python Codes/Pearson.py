!pip install yfinance
from numpy import mean
from numpy import std
from numpy import amax
from numpy.random import randn
from numpy.random import seed
from matplotlib import pyplot
from scipy.stats import pearsonr

import json
import datetime
import yfinance as yf

correlationList = []

def GetData(usd, startDate):
    fromDate = startDate-datetime.timedelta(days=14)
    toDate = startDate
    df = yf.download(usd, fromDate, toDate, interval = "1d")[['Close']]#, 'Open', 'Low', 'High', 'Volume']]
    return df['Close'].values

def Pearson(a, usd, b):
  # calculate Pearson's correlation
  corr, _ = pearsonr(a, b)
  max = amax(b[1:])
  grow = ((max - b[0])/b[0]) * 100
  # print("Grow percentage " + usd + ": \t %.3f" % grow )
  correlationList.append({"name":usd, "correlation": corr, "grow": grow, "firstPrice": b[0], "maxPrice": max})
  # print('Pearsons correlation '+usd+':\t %.3f' % corr)
  return corr

currentDate = datetime.datetime.now()

dataBTC = GetData('BTC-USD', currentDate)

coins = ['ETH','BNB','USDT','SOL1','ADA','XRP','USDC','DOT1','HEX','DOGE','AVAX','SHIB','CRO','LUNA1','LTC','UNI3','MATIC','LINK','BCH','ALGO','MANA','EGLD','AXS','XLM','VET','ICP1','FIL','FTT1','TRX','THETA','DAI1','SAND','ETC','HBAR','ATOM1','FTM','GRT2','HNT1','XMR','XTZ','MIOTA','EOS','LRC','FLOW1','ZEC','ENJ','AAVE','CAKE','MKR','RUNE','ONE2','BSV','KDA','KSM','NEO','CHZ','QNT','AMP1','STX1','BAT','CRV','HOT1','BTT1','WAVES','DASH','AR','CELO','TFUEL','COMP','IOTX','XEM','QTUM','DCR','WAXP','ZEN','TUSD','CTC1','XDC','ANKR','ICX','SC','OMG','ROSE','VGX','STORJ','YFI','RVN','HIVE','ZIL','CEL','BTG','OMI','CCXX','ZRX','SUSHI','BNT','DFI','VLX','CKB','SNX','UMA','ONT','SKL','RAY','KAVA','IOST','SRM','WIN1','XWC','1INCH','DGB','CELR','NANO','GLM','GNO','C98','FET','NU','LSK','RSR','CTSI','SXP','ZEL','MED','XVG','TWT','CVC','VTHO','OXT','NKN','COTI','SNT','ARRR','SYS','BCD','ARDR','STMX','XCH','RLC','ACH','ZNN','EWT','STEEM','VRA','TOMO','ARK','STRAX','ABBC','MCO','SAPP','ETN','BAND','REP','ERG','NMR','MAID','DAG','FUN','DERO','MIR1','DIVI','ANT','MTL','MLN','META','WAN','PHA','HNS','XHV','POA','RBTC','CLV','BTS','BAL','IRIS','AVA','ATRI','KMD','KIN','TT','AION','MONA','DNT','NYE','XAS','XNC','FIRO','ADX','CUDOS','MWC','GAS','ELA','NRG','DMCH','BTM','REV','WTC','GRS','PAC','FIO','WOZX','RDD','SBD','BCN','DGD','FRONT','APL','BEAM','CET','MARO','AE','BEPRO','CRU','VITE','PIVX','NULS','VSYS','NIM','VERI','FSN','AXEL','SOLVE','GXC','XCP','NXS','GAME','SERO','GO','CTXC','PPT','CUT','PCX','LOKI','WICC','KRT','PPC','VTC','GRIN','ZANO','MHC','OBSR','GBYTE','SRK','NVT','NAV','VAL1','NMC','ADK','WABI','QASH','QRL','HC','NAS','SCP','LBC','PART','XSN','AMB','NEBL','MASS','RSTR','CHI','RINGX','BIP','MAN','PAI','FCT','ETP','FO','NXT','DTEP','HTML','PZM','PAY','DCN','SALT','TRUE','PI','BTC2','DMD','YOYOW','MRX','BHP','LCC','PLC','NLG','EMC2','HPB','DNA1','SCC3','UBQ','BLOCK','XDN','ACT','DYN','IDNA','SFT','AEON','POLIS']

for c in coins:
  print(c)
  data = GetData(c+'-USD', currentDate)
  Pearson(dataBTC, c, data)

# # summarize
# print('data1: mean=%.3f stdv=%.3f' % (mean(data1), std(data1)))
# print('data2: mean=%.3f stdv=%.3f' % (mean(data2), std(data2)))

print(correlationList)

# plot
# pyplot.scatter(dataBTC, dataDOGE, color = 'red')
# pyplot.show()
