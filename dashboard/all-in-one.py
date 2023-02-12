import json
import time
import datetime
import uuid
import hmac
import hashlib
import requests
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
        'to': '01089391001',
        'from': '01089391001',
        'text': '한글 45자, 영자 90자 이하 입력되면 자동으로 SMS타입의 메시지가 추가됩니다.'
      }
    ]
  }
  res = sendMany(data)
  print(json.dumps(res.json(), indent=2, ensure_ascii=False))
