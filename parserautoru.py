import requests, json
from BD import *

def page(data):
    for items in data['offers']:
        print('Автомобиль добавлен')
        try:
            price = items['price_info']['price']
        except:
            price = '0'

        if price != '0':
            try:
                description = items['description']
            except:
                description = ''

            salon = 0

            if ('dealer_id' in items['salon']):
                salon = 1

            year = items['documents']['year']
            mile = items['state']['mileage']
            #tax = items['owner_expenses']['transport_tax']['tax_by_year']
            img = items['state']['image_urls'][0]['sizes']['1200x900']

            pull = items['vehicle_info']

            mark_info = pull['mark_info']['name']
            mark_info = mark_info.replace(' ', '_')

            mark_code = pull['mark_info']['code']

            model_info = pull['model_info']['name']
            model_code = pull['model_info']['code']

            rudder = pull['steering_wheel']
            if rudder == 'LEFT':
                rudder = 'Левый'
            else:
                rudder = 'Правый'

            motor = pull['tech_param']['human_name']
            trans = pull['tech_param']['transmission']
            gear_type = pull['tech_param']['gear_type']

            saleid = items['saleId']
            href = f'https://auto.ru/cars/used/sale/{mark_code.lower()}/{model_code.lower()}/{saleid}'

            entities = [ mark_info, model_info, salon, price, mile, year, motor, rudder, trans, gear_type, href, img, description  ]
            add_ads(*entities)

        else:
            print('Автомобиль продан')





headers = """
Host: auto.ru
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0
Accept: */*
Accept-Language: ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate, br
Referer: https://auto.ru/cars/used/?page=2
x-client-app-version: bf88d40e30
x-page-request-id: 648ac50764b7df33dd61e44a06af06a0
x-client-date: 1616064240139
x-csrf-token: d01d8edcb23f841f309369d798a196f185918a5fb2af99e2
x-requested-with: fetch
content-type: application/json
Origin: https://auto.ru
Content-Length: 45
Connection: keep-alive
Cookie: autoru_sid=a%3Ag604e8fd02fjff1ahbfbsng5n493umm5.958cb475087b0af4a4c3604519f8db56%7C1615761360887.604800.N-oNX1h3iOxCfa8Z7z9WDg.xtI5-VB5L1oPZW8bM7AMS6gKe-rsUUgaWrdXVQzinlQ; autoruuid=g604e8fd02fjff1ahbfbsng5n493umm5.958cb475087b0af4a4c3604519f8db56; suid=0f9cfdf65bd667fa7ffb1190da1060e2.25d639971c66a1f054a91ec480dc4f2d; salon_phone_utms=utm_medium%3Ddesktop%26utm_source%3Dauto_wizard%26utm_campaign%3Dcommon%26utm_content%3Dlisting; yuidlt=1; yandexuid=4758047171615761357; crookie=qQsVB7ozvIcIvcZFWhKgzeJM91WXoaxFR3lyLima8QTkISHiG1KDlUu5KzZo0dOLFic4uL5XVG1Bh4iIaI6HxCEHbaU=; cmtchd=MTYxNTc2MTM2MzcxMA==; _ym_uid=1615761365958596926; _ym_d=1616062997; cycada=yeAfbfRpzgqT7n27RAepOdNrz5jVz6MT4h3PMBKFTp8=; autoru-visits-count=2; panorama_press_and_spin_closed=true; _ym_isad=2; gids=; mmm-search-accordion-is-open-cars=%5B1%5D; _csrf_token=d01d8edcb23f841f309369d798a196f185918a5fb2af99e2; from_lifetime=1616062997048; from=direct; X-Vertis-DC=sas; gdpr=0""".strip().split("\n")

dict_headers = {}
for header in headers:
    key, value = header.split(': ')
    dict_headers[key] = value

for x in range(1, 99):
    param = {"category":"cars","section":"used","page":x}
    url = "https://auto.ru/-/ajax/desktop/listing/"
    response = requests.post(url, json=param, headers = dict_headers)
    data = response.json()
    page(data)
