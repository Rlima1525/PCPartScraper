import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL_gpu = "https://www.amazon.com/EVGA-RTX-2070-Black-08G-P4-1071-KR/dp/B07J9L4HC2/ref=sxin_0_ac_d_pm?keywords=RTX&pd_rd_i=B07J9L4HC2&pd_rd_r=bd6b7a76-0f57-4e22-94cf-7d8c992a5a66&pd_rd_w=mRbR9&pd_rd_wg=UxoAK&pf_rd_p=64aaff2e-3b89-4fee-a107-2469ecbc5733&pf_rd_r=JENSPA5G28TEQ7ZZMAAM&qid=1562370838&s=books"

URL_psu = "https://www.amazon.com/EVGA-Modular-Warranty-Supply-210-GQ-1000-V1/dp/B017ICWP82/ref=sr_1_3?keywords=power+supply&qid=1562422465&s=gateway&sr=8-3"

URL_cpu = "https://www.amazon.com/Intel-i9-9900K-Desktop-Processor-Unlocked/dp/B005404P9I/ref=sr_1_3?keywords=9900k&qid=1562426103&s=gateway&sr=8-3"

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'}

def check_price_gpu():
    page = requests.get(URL_gpu, headers=headers)

    soup = BeautifulSoup(page.content, 'lxml')

    title_gpu = soup.find(id="productTitle").get_text()

    price_gpu = soup.find(id="priceblock_ourprice").get_text()

    printed_title = title_gpu.strip()

    converted_price = float(price_gpu[1:5])

    print(f"You are looking at {printed_title}, \nthe price is {price_gpu}\n")

    if converted_price < 400:
        send_mail_gpu()
    else:
        print("Price does not meet requirements, too expensive!\n")

def check_price_psu():
    page = requests.get(URL_psu, headers=headers)

    soup = BeautifulSoup(page.content, 'lxml')

    title_psu = soup.find(id="productTitle").get_text()

    price_psu = soup.find(id="priceblock_ourprice").get_text()

    printed_title = title_psu.strip()

    converted_price = float(price_psu[1:5])

    print(f"You are looking at {printed_title}, \nthe price is {price_psu}\n")

    if converted_price < 120:
        send_mail_psu()
    else:
        print("Price does not meet requirements, too expensive!\n")
   
def check_price_cpu():
    page = requests.get(URL_cpu, headers=headers)

    soup = BeautifulSoup(page.content, 'lxml')

    title_cpu = soup.find(id="productTitle").get_text()

    price_cpu = soup.find(id="priceblock_ourprice").get_text()

    printed_title = title_cpu.strip()

    converted_price = float(price_cpu[1:5])

    print(f"You are looking at {printed_title}, \nthe price is {price_cpu}\n")

    if converted_price < 450:
        send_mail_cpu()
    else:
        print("Price does not meet requirements, too expensive!\n")


def send_mail_gpu():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('rlima262@gmail.com','dbymutwrymdezvcn')

    subject = 'Price Dropped on Graphics Card (RTX 2070)'
    body = "Check out the link! https://www.amazon.com/EVGA-RTX-2070-Black-08G-P4-1071-KR/dp/B07J9L4HC2/ref=sxin_0_ac_d_pm?keywords=RTX&pd_rd_i=B07J9L4HC2&pd_rd_r=bd6b7a76-0f57-4e22-94cf-7d8c992a5a66&pd_rd_w=mRbR9&pd_rd_wg=UxoAK&pf_rd_p=64aaff2e-3b89-4fee-a107-2469ecbc5733&pf_rd_r=JENSPA5G28TEQ7ZZMAAM&qid=1562370838&s=books"

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'rlima262@gmail.com',
        'rlima262@gmail.com',
        msg
    )

    print("Hey email has been sent")

    server.quit()

def send_mail_psu():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("rlima262@gmail.com", "dbymutwrymdezvcn")

    subject = "The price for the PSu has dropped!"
    body = "Check out the link! https://www.amazon.com/EVGA-Modular-Warranty-Supply-210-GQ-1000-V1/dp/B017ICWP82/ref=sr_1_3?keywords=power+supply&qid=1562422465&s=gateway&sr=8-3"
    
    msg = f"Subject: {subject} \n\n{body}"

    server.sendmail(
        'rlima262@gmail.com',
        'rlima262@gmail.com',
        msg
    )

    print("PSU mail has been sent")

    server.quit()

def send_mail_cpu():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("rlima262@gmail.com", "dbymutwrymdezvcn")

    subject = "The price of the CPU has dropped!"
    body = "Check out the link!  https://www.amazon.com/Intel-i9-9900K-Desktop-Processor-Unlocked/dp/B005404P9I/ref=sr_1_3?keywords=9900k&qid=1562426103&s=gateway&sr=8-3"

    msg = f"Subject: {subject} \n\n{body}"

    server.sendmail(
        'rlima262@gmail.com',
        'rlima262@gmail.com',
        msg
    )

    print("CPU mail has been sent!")

    server.quit()

check_price_gpu()

check_price_psu()

check_price_cpu()