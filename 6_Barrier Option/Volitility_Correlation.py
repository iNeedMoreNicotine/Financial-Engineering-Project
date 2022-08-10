import yfinance as yf
import pandas as pd
from pandas_datareader import data
from datetime import datetime
from dateutil.relativedelta import relativedelta
import matplotlib.pyplot as plt


def calc_historical_volitility(asset_amount, stock_lst):
    yf.pdr_override()   
    end_date = datetime.now()
    delta = relativedelta(years = 1)
    start_date = datetime.now() - delta

    df_dict = dict()
    for i in range(asset_amount):
        df_dict[f'asset{i+1}'] = data.get_data_yahoo([stock_lst[i]], start_date, end_date)['Close']

    sigma_lst = []
    for i in range(asset_amount):
        sigma_lst.append(df_dict[f'asset{i+1}'].std())

    return sigma_lst

def calc_correlation(asset_amount, stock_lst):
    yf.pdr_override()
    end_date = datetime.now()
    delta = relativedelta(years = 1)
    start_date = datetime.now() - delta

    df_dict = dict()
    for i in range(asset_amount):
        df_dict[f'asset{i+1}'] = data.get_data_yahoo([stock_lst[i]], start_date, end_date)['Close']

    rho_lst = []
    for i in range(asset_amount-1):
        for j in range(asset_amount-(i+1)):
            rho_lst.append(df_dict[f'asset{i+1}'].corr(df_dict[f'asset{j+2+i}']))

    return rho_lst




stock_lst = ['GE', 'TSM', 'JPM', 'META', 'KO']
sigma_lst = calc_historical_volitility(5, stock_lst)
print(sigma_lst)

rho_lst = calc_correlation(5, stock_lst)
print(rho_lst)