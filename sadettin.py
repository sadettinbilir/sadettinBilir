import json
dosya=open('myfile.json',"r")
json_dosya=json.load(dosya)
print("Kullanıcı adı :",json_dosya["kimlik"][0]["ad"])
print("Kullanıcı soyadı :",json_dosya["kimlik"][1]["soyad"])