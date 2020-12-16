import discord
import os
import requests
import json
from keep_alive import keep_alive

def get_quote():
	'''Get quote from api in json format using GET request'''
	response = requests.get("https://api.quotable.io/random")
	json_data = json.loads(response.text)
	quote = json_data['content']
	author = json_data['author']
	return f'"{quote}" - {author}'

class MyClient(discord.Client):
	async def on_ready(self):
		print('Logged on as', self.user)

	async def on_message(self, message):
		# don't respond to ourselves
		if message.author == self.user:
			return

		msg = message.content

		if msg.startswith('!quote'):
			quote = get_quote()
			await message.channel.send(quote)


if __name__ == "__main__":	
	keep_alive()
	client = MyClient()
	client.run(os.getenv('TOKEN'))