import json
import sys

import json
import sys

sys.path.append('../../../lib')

import message
# from src.lib import message

# 한번 요청으로 1만건의 메시지 발송이 가능합니다.
if __name__ == '__main__':
    data = {
        'messages': [
            {
                'to': '01089391001',
                'from': '01089391001',
                'text': '한글 45자, 영자 90자 이하 '
            }
        ]
    }
    res = message.send_many(data)
    print(json.dumps(res.json(), indent=2, ensure_ascii=False))
