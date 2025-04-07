# parser.py
from bs4 import BeautifulSoup
import re

"""
タグを指定して抽出を行う関数
"""
def get_fact(xbrl_file:str,tag:str,context_ref:str=None,unit_ref:str=None):
    with open(xbrl_file, encoding="utf-8") as doc:
        soup = BeautifulSoup(doc, "lxml-xml")

    conditions = {}
    if context_ref:
        conditions["contextRef"] = context_ref
    if unit_ref:
        conditions["unitRef"] = unit_ref

	# 実際にXBRLから条件に合うインスタンスを探す
    fact = soup.find(tag, conditions)
    fact = fact.text

    return fact


"""
htmlタグを除去する関数
"""
def htmltag_remove(text):
    # 空白（\s）除去
    text = re.sub(r'\s', '', text).strip()
    # HTMLタグ（<.*?>）の除去
    soup = BeautifulSoup(text, "html.parser")
    cleansing_text = soup.get_text()

    return cleansing_text

"""
よく使用するタクソノミのインスタンスをゲットする
"""
def use_well_taxonomy(xbrl_file):
    with open(xbrl_file, encoding="utf-8") as doc:
        soup = BeautifulSoup(doc, "lxml-xml")

    tags = ["FilerNameInJapaneseDEI","AccountingStandardsDEI"
                ,"BusinessRisksTextBlock"]

    instance_list = []
    for tag in tags:
        instance = soup.find(tag)
        instance = instance.text
        instance = htmltag_remove(instance)
        instance_list.append(instance)

    return instance_list