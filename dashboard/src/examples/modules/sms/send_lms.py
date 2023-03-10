import json
from src.lib import message

# 한번 요청으로 1만건의 메시지 발송이 가능합니다.
if __name__ == '__main__':
    data = {
        'messages': [
            {
                'to': '01000000001',
                'from': '029302266',
                'text': '한글 45자, 영자 90자 이상 입력되면 자동으로 LMS타입의 문자메시지가 발송됩니다. 0123456789 ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            },
            {
                'to': '01000000002',
                'from': '029302266',
                'subject': 'LMS 제목',  # 제목을 지정할 수 있습니다.
                'text': '한글 45자, 영자 90자 이상 입력되면 자동으로 LMS타입의 문자메시지가 발송됩니다. 0123456789 ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            },
            {
                'type': 'LMS',  # 타입을 명시할 수 있습니다.
                'to': '01000000003',
                'from': '029302266',
                'text': '내용이 짧아도 LMS로 발송됩니다.'
            },
            {
                'to': '01000000004',
                'from': '029302266',
                'text': '한글 45자, 영자 90자 이하는 자동으로 SMS타입의 문자가 발송됩니다.'
            },
            {
                'to': ['01000000005', '01000000006'],  # 수신번호를 array로 입력하면 같은 내용을 여러명에게 보낼 수 있습니다.
                'from': '029302266',
                'subject': 'LMS 제목',
                'text': '한글 45자, 영자 90자 이상 입력되면 자동으로 LMS타입의 문자메시지가 발송됩니다. 0123456789 ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            }
            # ...
            # 1만건까지 추가 가능
        ]
    }
    res = message.send_many(data)
    print(json.dumps(res.json(), indent=2, ensure_ascii=False))
