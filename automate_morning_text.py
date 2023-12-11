# #from credentials import mobile_number
# import requests
# import schedule
# import time

# def send_message():
#     resp = requests.post('https://textbelt.com/text', {
#         'phone' : '+917569540512',
#         'message': 'Hey, Good morning',
#         'key': 'textbelt'
#     })
#     print(resp.json())

# # schedule.every() .day.at('06:00').do(send_message)
# schedule.every(10).seconds.do(send_message)

# while True:
#     schedule.run_pending()
#     time.sleep(1)


# import pywhatkit


# pywhatkit.sendwhatmsg("+917569540512","Hi hello adab",8,27)

# import pywhatkit
# import time

# print("Starting WhatsApp automation...")
# pywhatkit.sendwhatmsg("+917569540512", "Hi hello It's working", 8, 51,10,True)
# print("Message sent. Waiting...")
# time.sleep(30)
# print("WhatsApp automation completed.")
