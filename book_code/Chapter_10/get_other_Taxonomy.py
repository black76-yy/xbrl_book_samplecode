from arelle import ModelManager
from arelle import Cntlr
import os, time, glob, re
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import japanize_matplotlib

"""
提出者別タクソノミを含めた企業情報を取得する関数
"""
def make_edinet_company_info_list(xbrl_files):
    edinet_company_info_list = []
    for index, xbrl_file in enumerate(xbrl_files):
        company_data = {"会計年度": "", "コンテンツ資産": ""}
        
        ctrl = Cntlr.Cntlr()
        model_manager = ModelManager.initialize(ctrl)
        model_xbrl = model_manager.load(xbrl_file)
        print("XBRLファイルを読み込んでいます", ":", index + 1, "/", len(xbrl_files))

        for fact in model_xbrl.facts:
            if fact.concept.qname.localName == 'FiscalYearCoverPage':
                company_data["会計年度"] = fact.value
            elif fact.concept.qname.localName == 'ContentAssetsNCAIFRS' :
                if fact.contextID == 'CurrentYearInstant':
                    company_data["コンテンツ資産"] = fact.value

        edinet_company_info_list.append([
            company_data["会計年度"],
            company_data["コンテンツ資産"],
        ])

    return edinet_company_info_list

def graph_plot(data):
    df = pd.DataFrame(data, columns=["会計年度", "コンテンツ資産"])
    df["コンテンツ資産"] = pd.to_numeric(df["コンテンツ資産"], errors='coerce')
    df = df.dropna()

    plt.figure(figsize=(10, 5))
    plt.plot(df["会計年度"], df["コンテンツ資産"], marker='o')
    plt.title("コンテンツ資産の推移")
    plt.xlabel("会計年度")
    plt.ylabel("コンテンツ資産")
    plt.grid(True)

    # 数値を3桁区切りで表示
    ax = plt.gca()
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f"{x:,.0f}"))

    plt.show()



def main():
	# あなたのXBRLファイルのパス(ただコピーしても動きません)
    xbrl_file = glob.glob(r'*フォルダ名\\*\\*\\XBRL\\PublicDoc\\*.xbrl')

    company_info = make_edinet_company_info_list(xbrl_file)
    for info in company_info:
        print(info)

    graph_plot(company_info)
if __name__ == "__main__":
    main()