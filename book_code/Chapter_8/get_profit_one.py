from arelle import ModelManager
from arelle import Cntlr
import os
import glob

"""
取得する項目をリストとして格納するための関数
"""
def make_edinet_company_info_list(xbrl_file):
    edinet_company_info_list = []
    company_data = {
        "EDINETCODE": "",
        "企業名": "",
        "営業利益(IFRS)": "",
    }

    ctrl = Cntlr.Cntlr()
    model_manager = ModelManager.initialize(ctrl)

    model_xbrl = model_manager.load(xbrl_file)

    # 実データを探して取得
    for fact in model_xbrl.facts:

        # EDINETコードを探す
        if fact.concept.qname.localName == 'EDINETCodeDEI':
            company_data["EDINETCODE"] = fact.value

        # 企業名を探す
        elif fact.concept.qname.localName == 'FilerNameInJapaneseDEI':
            company_data["企業名"] = fact.value

        # 営業利益(IFRS)を探す
        elif fact.concept.qname.localName == 'OperatingProfitLossIFRS':
            if fact.contextID == 'CurrentYearDuration':
                company_data["営業利益(IFRS)"] = fact.value

    # 見つけたデータをリストに入れる
    edinet_company_info_list.append([
        company_data["EDINETCODE"],
        company_data["企業名"],
        company_data["営業利益(IFRS)"],
    ])

    return edinet_company_info_list

"""
元データのパスを指定し、すべての処理を実行する関数
"""
def main():
    # あなたのXBRLファイルのパスを指定(ただコピーしても動きません)
    xbrl_file = r"\\xxx\\フォルダ名\\XBRL\\PublicDoc\\XBRLファイル名.xbrl"

    company_info = make_edinet_company_info_list(xbrl_file)
    for info in company_info:
        print(info)

    print("extract finish")

if __name__ == "__main__":
    main()