import json
dosya=open('myfile.json',"r")
json_dosya=json.load(dosya)
print("devnet ödev1")
print("API-KEY :",json_dosya["access_token"])
print("Kullanıcı adı :",json_dosya["kimlik"][0]["ad"])
print("Kullanıcı soyadı :",json_dosya["kimlik"][1]["soyad"])