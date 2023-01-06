import requests
from requests import post, get

print("\nMake by TUF47")
phone = input("\n - 𝙿𝙷𝙾𝙽𝙴 : ")
number = input("\n - 𝙽𝚄𝙼𝙱𝙴𝚁 : ")

carsome = {
  "url": "https://www.carsome.co.th/website/login/sendSMS",
  "data": {
    "username": f"{phone}",
    "optType": "0"
  },
  "headers": {
    "Host": "www.carsome.co.th",
    "content-length": "37",
    "x-language": "th",
    "x-token": "",
    "sec-ch-ua-mobile": "?1",
    "user-agent": "Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Mobile Safari/537.36",
    "content-type": "application/json",
    "accept": "application/json, text/plain, */*",
    "country": "TH",
    "x-amplitude-device-id": "",
    "sec-ch-ua-platform": "Android",
    "origin": "https://www.carsome.co.th",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://www.carsome.co.th/"
  }
}

request = post(carsome.url, json={
  carsome.data
}, headers={
  carsome.headers
})

print(request.text)