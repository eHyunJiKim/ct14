import requests
r=requests.get('https://www.vox.com/2018/9/25/17901082/trump-un-2018-speech-full-text')
r.encoding='utf8'
data=str(r.text)
begin=data.find("Madam President, Mr. Secretary-General,")
end=data.rfind('Thank you very much. Thank you. (Applause.)')
a=data[begin:end]
a=a.replace('</body></html>','') ; a=a.replace("phonographEvents.push(['pageload',", '') ; a=a.replace('null;', '') ; a=a.replace(':','')
a=a.replace('<p id="g9nuW5">','') ; a=a.replace('</p>', ''); a=a.replace('<p id="68hVhn">', '') ; a=a.replace('<p id="Aogf2Y">','') ; a=a.replace('<p id="ADSChO">','') ; a=a.replace('<p id="uCDYdn">','') ; a=a.replace('<p id="WPa6ga">','') ; a=a.replace('<p id="oeG0df">','') ; a=a.replace('<p id="D3FUVt">','') ;a=a.replace('<p id="UirOEx">','') ; a=a.replace('<p id="rmQW8I">','') ; a=a.replace('<p id="YLkHwj">','') ; a=a.replace('<p id="vwedBc">','') ; a=a.replace('<p id="2LeMOG">','') ; a=a.replace('<p id="TFia8t">','') ; a=a.replace('<p id="TyBHek">','') ; a=a.replace('<p id="mD77Vc">','') ; a=a.replace('<p id="ygqENp">','') ;a=a.replace('<p id="ifFWwQ">','') ;a=a.replace('<p id="U0le6t">','');a=a.replace('<p id="LtvQ0U">','');a=a.replace('<p id="JG31ve">','')
a=a.replace('<p id="z5XIGd">', '') ; a=a.replace('<p id="EdgTnP">',''); a=a.replace('<p id="aCKAHN">','') ; a=a.replace('<p id="aCKAHN">','') ; a=a.replace('<p id="BkmM5D">',''); a=a.replace('<p id="G97hic">',''); a=a.replace('<p id="YfDLjI">',''); a=a.replace('<p id="5fGqFK">',''); a=a.replace('<p id="nWbjqU">','') ; a=a.replace('<p id="oOzvaJ">',''); a=a.replace('<p id="l4j77s">','') ; a=a.replace('<p id="K4iZDx">','')
a=a.replace('<p id="vbWlzm">','') ; a=a.replace('<p id="LoDnTZ">','') ; a=a.replace('<p id="PJ58ub">',''); a=a.replace('<p id="w5LkMz">','') ;a=a.replace('<p id="gl0t4E">','') ; a=a.replace('<p id="mg3pQw">','') ; a=a.replace('<p id="3TruLu">','') ; a=a.replace('<p id="cF26si">','') ; a=a.replace("'",' ') ; a=a.replace(",", ' ') ; a=a.replace('.',' ') ; a=a.replace('<p id="ho9d9B">','')
a=a.replace('<p id="VyREAn">','') ;a=a.replace('<p id="HHfKGw">','') ; a=a.replace('<p id="oNMPwE">','') ; a=a.replace('<p id="U032US">','') ; a=a.replace('<p id="arUKY9">','') ; a=a.replace('<p id="aAhymi">','') ; a=a.replace('<p id="n2wvR5">','') ; a=a.replace('<p id="jAAkq5">','') ; a=a.replace('<p id="FXgaQ3">','') ; a=a.replace('<p id="rIO8UR">','') ;a=a.replace('<p id="8zjfzm">','') ; a=a.replace('<p id="j1YjtQ">','') ; a=a.replace('<p id="DTq7Xx">','') ; a=a.replace('<p id="HP7bJv">','') ;a=a.replace('<p id="YQiJ1M">','') ; a=a.replace('<p id="a7faPp">','') ; a=a.replace('<p id="bFDksK">','') ; a=a.replace('<p id="spVgTc">','') ; a=a.replace('<p id="ATCHk0">','') ; a=a.replace('<p id="GBwq44">','') ;a=a.replace('<p id="IXbqpy">','') ; a=a.replace('<p id="YyHi6Q">','') ; a=a.replace('<p id="Z7D9wR">','') ; a=a.replace('<p id="MF6Aj5">','') ; a=a.replace('<p id="BEZFrh">','') ; a=a.replace('<p id="aofXQa">','') ; a=a.replace('<p id="JaUr5K">','') ; a=a.replace('<p id="I5B3we">','') ; a=a.replace('<p id="fxkrxd">','') ; a=a.replace('<p id="dvYzvh">','') ; a=a.replace('<p id="qpJZur">','') ; a=a.replace('<p id="GrpRT3">','') ; a=a.replace('<p id="gmX2pq">','') ; a=a.replace('<p id="kG57U3">','') ; a=a.replace('<p id="ACghpr">','')
a=a.replace('<p id="6wgp7q">','') ; a=a.replace('<p id="1JN4WY">','') ; a=a.replace('<p id="a1fKja">',''); a=a.replace('<p id="uMK9dI">','');a=a.replace('<p id="64m7Jf">','') ; a=a.replace('<p id="hyZJgK">','')
a=a.replace('<p id="gM44HV">',''); a=a.replace('<p id="q3GM7z">','') ;a=a.replace('<p id="KGCi8L">','') ;a=a.replace('<p id="cR5RV5">','') ; a=a.replace('<p id="GiwrL6">','') ;a=a.replace('<p id="KsUeUC">','') ;a=a.replace('<p id="YDEq81">','') ; a=a.replace('<p id="Z6I5bq">','') ;a=a.replace('<p id="u2riPc">','') ;a=a.replace('<p id="Yx0P4B">','') ;a=a.replace('<p id="npbK00">','') ;a=a.replace('<p id="PmWmMj">','') ; a=a.replace('<p id="5PzzoY">','') ; a=a.replace('<p id="hyZJgK">','')
a=a.replace('-–',' ') ;  a=a.replace('<p id="mgVOrt">','') ; a=a.replace('(',' ') ; a=a.replace(')',' '); a=a.replace('[',' ') ; a=a.replace(']',' ') ; a=a.replace('<p id="64ZSXC">','') ; a=a.replace('<p id="wtVDOX">','') ; a=a.replace('"',' ')

mydict={}
a=a.split()
for w in a:
    if w in mydict:
        mydict[w]+=1
    else:
        mydict[w]=1
i=0
for k in sorted(mydict, key=mydict.__getitem__, reverse=True):
        print('%s: %s'%(k,mydict[k]))
        i+=1
        if i>19:
            break


        








