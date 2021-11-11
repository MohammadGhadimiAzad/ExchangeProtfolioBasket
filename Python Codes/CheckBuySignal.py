!pip install mplfinance
!pip install yfinance
import pandas as pd
from pandas_datareader import data, wb
import matplotlib as mpl
import mplfinance
import matplotlib.dates as dates
import datetime
import matplotlib.pyplot as plt
import sys
import yfinance as yf
import matplotlib.pyplot as plt
import urllib.parse
import urllib.request, json

brands = ['خشرق','خودرو','مرقام','چافست','بترانس','دالبر','خكار','پاسا','پتاير','ديران','لابسا','فايرا','فمراد','آپ','ثاخت','وبصادر','وبملت','وتجارت','وسينا','وكار','البرز','وخاور','پارسيان','وپارس','كالا','ونوين','شپارس','ثبهساز','كاما','دانا','وپاسار','ملت','غگرجي','آسيا','غبهنوش','پرداخت','ما','بسويچ','تپمپي','خپارس','خراسان','شبريز','بوعلي','پلاسك','سپ','وپست','نوري','پارس','لخزر','دپارس','شپديس','شيراز','جم پيلن','شخارك','كسرام','شتران','شپنا','قرن','شاراك','شفن','غشاذر','شبندر','شپاكسا','جم','لپارس','غپينو','كپشير','خمحور','ومعادن','تكنو','آبادا','تكالا','كروي','امين','تايرا','دتماد','كوير','چدن','حتايد','كماسه','رتاپ','ثاميد','وتوس','غمهرا','لوتوس','وبشهر','كنور','تنوين','تملت','اميد','ثاباد','كترام','فجام','خچرخش','حفارس','حتوكا','وخارزمح','حپترو','دالبرح','شگلح','جمح','حفاري','دشيميح','غدام','رانفور','وپخش','دفارا','درازك','دلر','شدوص','ددام','دابور','دروز','دلقما','دجابر','دسينا','غدشت','هاي وب','داسوه','دزهراوي','دكوثر','مداران','كطبس','خرينگ','ختور','ختراك','خزاميا','واتي','وخارزم','وساخت','ونيرو','سخزر','سيتا','وبهمن','تاصيكو','ورنا','سخاش','زكوثر','سرود','ونفت','وساپا','ثمسكن','ثشاهد','سصفها','سفار','سنير','انرژي3','وصنعت','ساراب','تاپيكو','ثشرق','ونيكي','وآذر','شفا','وسكاب','تيپيكو','فپنتا','سبجنو','والبر','سيمرغ','وغدير','سبهان','سشمال','سهگمت','سهرمز','وپترو','سيلام','ساربيل','سفارس','وبوعلي','غسالم','لسرما','سمازن','سپاها','سكرد','سدور','وصندوق','سشرق','سخوز','وتوشه','خاذين','ستران','سفانو','وتوكا','سغرب','خپويش','ثامان','سقاين','پرديس','شيران','كسرا','ساروم','خساپا','سصوفي','سكرما','وبانك','واعتبار','وبيمه','وسپه','سيدكو','دسبحان','وتوسم','كگاز','غشهد','غشصفا','قشهد','كهمدا','دشيمي','همراه','غشان','قشكر','فاما','فاذر','سدشت','غبشهر','كخاك','چكاوه','بكاب','كساوه','فارس','كرماشا','غزر','شسينا','خريخت','پسهند','ثفارس','فسازان','دفرا','فرآور','فجر','چفيبر','خزر','كاذر','فولاژ','كفپارس','بفجر','فروس','انرژي2','فخاس','افق','كاوه','فولاد','خفنر','كفرا','فخوز','قپيرا','قلرست','قثابت','قصفها','قمرو','قهكمت','قنيشا','ختوقا','كبورس','كرازي','غچين','كپارس','ركيش','تكمبا','حكشتي','دارو','غاذر','بكام','دكيمي','كحافظ','كسعدي','پكوير','قزوين','خكمك','فاسمين','بالبر','رتكو','كلوند','اكالا','چكارن','شكربن','چكاپا','پترول','وملي','واميد','فسپا','لبوتان','شگل','بركت','وصنا','دسبحا','خگستر','تكشا','غگل','پكرمان','پارسان','وتوصا','رمپنا','وليز','ولساپا','فلوله','ولپارس','شلعاب','فلامي','وايران','ولصنم','بشهاب','غپاك','غالبر','ولغدر','خلنت','دعبيد','خوساز','فسرب','زپارس','شوينده','فملي','خنصير','فاراك','شاملا','غمارگ','خمهر','فباهنر','بموتو','مبين','خموتور','كمنگنز','كبافق','كچاد','اخابر','نبورس','فنورد','شنفت','انرژي','فنوال','بنيرو','شكلر','شسپا','غنوش','ثنوسا','خمحركه','نكالا','سيستم','ولملت']

def GetData(title='آپ'):
  try:
    t = urllib.parse.quote(title.encode('utf-8'))
    with urllib.request.urlopen(f"https://ghadimiazad.ir/arshad/getdata.php?brand={t}&from=1385-01-01&to=1400-08-01") as url:
        return json.loads(url.read().decode())
  except:
    pass

def SaveSignal(title, typ, shdate, gdate):
  try:
    t = urllib.parse.quote(title.encode('utf-8'))
    gd = gdate.date()
    with urllib.request.urlopen(f"https://ghadimiazad.ir/arshad/signal.php?brand={t}&typ={typ}&shdate={shdate}&gdate={gd}") as url:
        pass
  except:
    pass

def signal(df):
  buy_array = []
  sell_array = []
  cols = df.columns.tolist()
  indexes = df.index.tolist()
  Data = df.values
  tenkan_sen_index = cols.index("tenkan_sen")
  kijun_sen_index = cols.index("kijun_sen")
  senkou_span_a_index = cols.index("senkou_span_a")
  senkou_span_b_index = cols.index("senkou_span_b")
  chikou_span_index = cols.index("chikou_span")
  Close_index = cols.index("PClosing")
  date_index = cols.index("DEven")

  for i in range(len(Data)):
    if Data[i, tenkan_sen_index] > Data[i, kijun_sen_index] and \
       Data[i - 1, tenkan_sen_index] < Data[i - 1, kijun_sen_index] and \
       Data[i, Close_index] > Data[i, senkou_span_a_index] and \
       Data[i, Close_index] > Data[i, senkou_span_b_index] and \
       Data[i - 26, chikou_span_index] > Data[i - 26, Close_index]:
        SaveSignal(brand, 'buy', Data[i, date_index], indexes[i])
    
    if Data[i, tenkan_sen_index] < Data[i, kijun_sen_index] and \
       Data[i - 1, tenkan_sen_index] > Data[i - 1, kijun_sen_index] and \
       Data[i, Close_index] < Data[i, senkou_span_a_index] and \
       Data[i, Close_index] < Data[i, senkou_span_b_index] and \
       Data[i - 26, chikou_span_index] < Data[i - 26, Close_index]:
          SaveSignal(brand, 'sell', Data[i, date_index], indexes[i])
    
  lastBuyDate = None
  if len(buy_array) > 0:
    lastBuyDate = buy_array[0]

  lastSellDate = None
  if len(sell_array) > 0:
    lastSellDate = sell_array[0]

  return (lastBuyDate, lastSellDate)

def ichimoku(brand):
  allData = GetData(brand)
  d = pd.json_normalize(allData)
  d['date'] = pd.to_datetime(d['date'])
  d = d.set_index(['date'])

  #*****************************************

  nine_period_high = d['PriceMax'].rolling(window=9).max()
  nine_period_low = d['PriceMin'].rolling(window=9).min()
  d['tenkan_sen'] = (nine_period_high + nine_period_low) /2

  # Kijun-sen (Base Line): (26-period high + 26-period low)/2))
  period26_high = d['PriceMax'].rolling(window=26).max()
  period26_low = d['PriceMin'].rolling(window=26).min()
  d['kijun_sen'] = (period26_high + period26_low) / 2
  # Senkou Span A (Leading Span A): (Conversion Line + Base Line)/2))
  d['senkou_span_a'] = ((d['tenkan_sen'] + d['kijun_sen']) / 2).shift(26)
  # Senkou Span B (Leading Span B): (52-period high + 52-period low)/2))
  period52_high = d['PriceMax'].rolling(window=52).max()
  period52_low = d['PriceMin'].rolling(window=52).min()
  d['senkou_span_b'] = ((period52_high + period52_low) / 2).shift(26)
  # The most current closing price plotted 26 time periods behind (optional)
  d['chikou_span'] = d['PClosing'].shift(-26)

  return signal(d)

for brand in brands:
  try:
    res = ichimoku(brand)
  except:
    pass
