import requests
import re
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
print('Cookies:', cookies)

# 签到
# 签到页面
# https://www.24geban.com/wx/auth/wechat/index.jhtml?userId=1&type=32
url = "https://www.24geban.com/wx/customer/signin.wx"
response = requests.get(url, headers=headers, cookies=cookies)
print('签到:', response.text)

# 获取id
url = 'https://www.24geban.com/wx/customer/sign/index.wx'
response = requests.get(url, headers=headers, cookies=cookies)
result = re.findall('ID:(\d+)</p>', response.text)
loginCustomerId = result[0]
print('id:', loginCustomerId)

# 领券
# 券的详情 https://www.24geban.com/applet/coupon/bag/data.jhtml
url = "https://www.24geban.com/wx/template/coupon/bag/get.jhtml"
data = {
    "fromCustomerId": loginCustomerId,
    "id": "5",
    "userId": "1",
    "appletId": "4",
    "apiToken": "6a8a1f634e38d30e87b450899b31f810",
    "loginCustomerId": loginCustomerId,
    # 可空
    "loginCustomerToken": "",
    "_api_version_": "2",
    "requestFromType": "wechatApplet"
}
response = requests.post(url, headers=headers, data=data)
print('每日领券:', response.text)

# 个人信息
url = "https://www.24geban.com/wechat/applet/user/personalCore.jhtml"
params = {
    "customerId": loginCustomerId,
    "userId": "1",
    "appletId": "4",
    "apiToken": "6a8a1f634e38d30e87b450899b31f810",
    "loginCustomerId": loginCustomerId,
    # 可空
    "loginCustomerToken": "",
    "_api_version_": "2",
    "requestFromType": "wechatApplet"
}
response = requests.get(url, headers=headers, params=params)
j = response.json()
print(f'当前积分:{j["remainScore"]}')
print(f'当前优惠券数目:{j["remainCouponValue"]}')

# 优惠券列表
url = "https://www.24geban.com/wechat/applet/coupon/list.jhtml"
params = {
    "customerId": loginCustomerId,
    "userId": "1",
    "appletId": "4",
    "apiToken": "6a8a1f634e38d30e87b450899b31f810",
    "loginCustomerId": loginCustomerId,
    # 可空
    "loginCustomerToken": "",
    "_api_version_": "2",
    "requestFromType": "wechatApplet"
}
response = requests.get(url, headers=headers, params=params)
for i in response.json()['allCouponList']:
    print(i['coupon']['name'],
          f'{i["coupon"]["minConsume"]}-{i["coupon"]["value"]}')
