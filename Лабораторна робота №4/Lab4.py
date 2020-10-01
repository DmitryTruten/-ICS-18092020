import json
import os
import codecs
from dataclasses import dataclass


@dataclass
class Market:
    code: int
    name: str


@dataclass
class Data:
    date: str
    market_code: int
    market_potato: int
    market_cabbage: int
    market_onion: int


def print_data(data):
    ''' 
    Функція виводить об'єкт Data
    з назвами полів та значеннями
    '''

    print("Дата {date} Код ринку {market_code} Ціна Картопля {market_potato} Ціна Капуста {market_cabbage} Ціна Цибуля {market_onion}"
          .format(date=data.date, market_code=data.market_code, market_potato = data.market_potato, market_cabbage= data.market_cabbage , market_onion= data.market_onion))


market1 = Market(100, "Бесарабський")
market2 = Market(200, "Житній")
market3 = Market(300, "Володимирський")

markets = [market1, market2, market3]


data1 = Data("02.11.2016", 100, 45, 50, 70)
data2 = Data("02.11.2016", 200, 35, 30, 50)
data3 = Data("02.11.2016", 300, 35, 30, 45)
data4 = Data("14.11.2016", 100, 45, 45, 60)
data5 = Data("14.11.2016", 200, 40, 40, 50)
data6 = Data("14.11.2016", 300, 35, 35, 45)
data7 = Data("22.11.2016", 100, 40, 40, 60)
data8 = Data("22.11.2016", 200, 40, 40, 50)
data9 = Data("22.11.2016", 300, 40, 40, 60)
datas = [data1, data2, data3, data4, data5, data6, data7, data8, data9]

print_data(data2)
