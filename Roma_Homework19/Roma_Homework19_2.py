# 2. დაწერეთ პროგრამა, რომელიც ქმნის რამდენიმე ძაფს (Thread) და იწერს რამდენიმე mp3 ფაილს ინტერნეტიდან.


import requests, concurrent.futures

mus_url = [
    "https://ia902905.us.archive.org/11/items/2pacresurrection/Resurrection/02-Ghost.mp3",
    "https://ia801707.us.archive.org/32/items/allman-brothers-cow-palace-nye-1973-ksan/02.Done%20Somebody%20Wrong.mp3",
    "https://ia601500.us.archive.org/17/items/eagles-the-summit-houston-tx-1976-k101/01-Hotel%20California.mp3",
    "https://ia902305.us.archive.org/0/items/nas-hate-me-now/Hate%20Me%20Now/05-Blaze%20A%2050%20%28Main%29.mp3",
]
def download(url):
    
    mp3_bytes = requests.get(url).content
    mp3_name_before = url.split('/')[-1]
    mp3_name =''.join(filter(str.isalpha, mp3_name_before)) + '.mp3'

    with open(mp3_name, mode='wb') as mp3_file:
        mp3_file.write(mp3_bytes)
        print(f"music: {mp3_name} was downloaded")

print("It takes few seconds, please wait.....")
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download, mus_url)

print('\nDownloads finished')  