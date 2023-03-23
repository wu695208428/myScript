import requests

# 需要fromUserName


headers = {
    "Host": "www.24geban.com",
    "Accept": "application/json",
    "User-Agent": "Mozilla/5.0 (Linux; Android 12; Redmi K30 5G Build/SKQ1.220303.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/4435 MMWEBSDK/20230202 Mobile Safari/537.36 MMWEBID/8118 MicroMessenger/8.0.33.2320(0x28002135) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 miniProgram/wxf39b37290cbb1722",
    "X-Requested-With": "XMLHttpRequest",
    "Referer": "https://www.24geban.com/wx/customer/sign/index.wx",
}
cookies = {}
fromUserName = ''

# 登录
url = f'https://www.24geban.com/wx/auth/login.jhtml?id=1&fromUserName={fromUserName}&userId=1&firstShop=Y&gotoUrl=/wx/customer/sign/index.wx&fromWechatAuth=Y'
response = requests.get(url, headers=headers,
                        cookies=cookies, allow_redirects=False)
cookies = response.cookies.get_dict()
print(cookies)

# 签到
# 签到页面
# https://www.24geban.com/wx/auth/wechat/index.jhtml?userId=1&type=32
url = "https://www.24geban.com/wx/customer/signin.wx"
response = requests.get(url, headers=headers, cookies=cookies)
print(response.text)
