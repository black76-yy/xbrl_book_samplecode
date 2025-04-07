from xb_parser import get_fact,HTMLtag_remove,use_well_taxonomy

# あなたのXBRLファイルのパスを指定(ただコピーしても動きません)
xbrl_file = r"\\xxx\\フォルダ名\\XBRL\\PublicDoc\\XBRLファイル名.xbrl"
tag = "BusinessRisksTextBlock"
context_ref = "FilingDateInstant"

#XBRLファイルと任意のタクソノミをセット
fact = get_fact(xbrl_file,tag,context_ref)

#HTMLタグがついているデータをセット
text = HTMLtag_remove(fact)

#対象のXBRLファイルをセット
well_fact = use_well_taxonomy(xbrl_file)