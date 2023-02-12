#personal_acess_token = 'patozxeRPKKz3erQn.1decaad7be28f5ed0c96d6b32c735474065324988634e3ba53470ebffc095480'
import requests
import json
########## Airtable ###############
base_id = 'appssITu2KHnI0zUO'
table_id = 'tblLGqfVdDK7C1YH3'
url = "https://api.airtable.com/v0/" + base_id + "/" + table_id
params = {"maxRecords" : 50}

api_key = 'keyl1hCA8uM5W73Bl' #★★★API Key
headers = {'Authorization': 'Bearer ' + api_key}

response = requests.get(url, params=params, headers=headers)
airtable_response = response.json()
####################################


airtable_records = airtable_response['records']
members = [x for x in airtable_records if x['fields']['Status'] == '유료']
print(members)
# print(members['fields']['이름'])
phonelist = []
for p in members:
    print(p['fields']['이름'])
    print(p['fields']['전화번호_010'])
    phonelist.append(p['fields']['전화번호_010'])
print(phonelist)

########### Solapi ###############
# import json
import time
import datetime
import uuid
import hmac
import hashlib
# import requests
# apiKey, apiSecret 입력 필수
apiKey = 'NCSGSSAS9KEDGZID'
apiSecret = 'CWBJSXRAHISCKW65W7UBNX3CIQ5XNETT'
# 아래 값은 필요시 수정
protocol = 'https'
domain = 'api.solapi.com'
prefix = ''
def unique_id():
    return str(uuid.uuid1().hex)
def get_iso_datetime():
    utc_offset_sec = time.altzone if time.localtime().tm_isdst else time.timezone
    utc_offset = datetime.timedelta(seconds=-utc_offset_sec)
    return datetime.datetime.now().replace(tzinfo=datetime.timezone(offset=utc_offset)).isoformat()
def get_signature(key, msg):
    return hmac.new(key.encode(), msg.encode(), hashlib.sha256).hexdigest()
def get_headers(apiKey, apiSecret):
    date = get_iso_datetime()
    salt = unique_id()
    data = date + salt
    return {
      'Authorization': 'HMAC-SHA256 ApiKey=' + apiKey + ', Date=' + date + ', salt=' + salt + ', signature=' +
                             get_signature(apiSecret, data),
      'Content-Type': 'application/json; charset=utf-8'
    }
def getUrl(path):
    url = '%s://%s' % (protocol, domain)
    if prefix != '':
        url = url + prefix
    url = url + path
    return url

def sendMany(data):
    return requests.post(getUrl('/messages/v4/send-many'), headers=get_headers(apiKey, apiSecret), json=data)

# 한번 요청으로 1만건의 메시지 발송이 가능합니다.
if __name__ == '__main__':
    data = {
        'messages': [
          {
            'to': phonelist,
            'from': '01089391001',
            'text': '한글 45자, '
          }
        ]
    }
    res = sendMany(data)
    print(json.dumps(res.json(), indent=2, ensure_ascii=False))
    sms_response = res.json()
            # sms_records = sms_response['records']
    print("sms=====>", sms_response)
    print(sms_response['log'])
    log_list = sms_response['log']
    for k in log_list:
        print(k['message'])

##################################


# print(airtable_records[0]['fields']['Status'])
# members = airtable_records['Status']
# members = [x for x in airtable_records if x['id']['fields']['Status'] == 'To do']
# for p in airtable_records:
#     if p['fields']['Status'] == 'To do'
#         filtered +=
    # print(p['fields'])
    # print(p['fields']['Status'])
#     if p['id']['fields']['Status'].lower():
#         result.append(p)
# filtered = list(filter(lambda x: x[0][2][6] == 'To do', airtable_records))
# print(airtable_records[0]['fields']['Status'])
# print(filtered)
# print(airtable_records)

# params = ()
# airtable_records = []
# run = True
# while run is True:
#   response = requests.get(url, params=params, headers=headers)
#   airtable_response = response.json()
#   airtable_records += (airtable_response['records'])
  # if 'offset' in airtable_response:
  #    run = True
  #    params = (('offset', airtable_response['offset']),)
  # else:
  #    run = False

# print(airtable_records[1]['fields']['Status'])