# Discord Bot

A simple discord bot that generates quotes.

## Usage

`!quote` - generate random quotes

### How Discord.py library works

Revolves around the concept of events. An event is something you listen to and then respond to. For example, when a message happens in discord, you will receive an event about it that you can respond to. With that, you can make a bot that listens to specific events and replies a message.

The library is asynchronous, so things are done with callbacks. Callback is a function that is called when something else happens. 

### async & await

Defining a method with `async def` makes it a coroutine. A coroutine in python is a function or method that pauses it's execution and resumes at a later point. Any task that needs to run asynchronously needs to be a coroutine.

A couroutine must be invovked with `await`(>= python 3.5). When Python encounters an `await`, it stops the function's execution and works on other things until it comes back to that point and finishes the execution. This allows the program to be working on multiple things at the same time (without using threads or multiprocessing). Note that `await` can only be used inside `async def` functions.

A good way to think of `async` / `await` is as an API for asynchronous programming 

## References
* [FreeCodeCamp video](https://www.youtube.com/watch?v=SPTfmiYiuok&t=624s) 
* [repl](https://repl.it/@BeauCarnes/Encourage-Bot#main.py)

## resources
* [quotable api github](https://github.com/lukePeavey/quotable)
* [discord.py GitHub](https://github.com/Rapptz/discord.py)
* [discord.py documentation](https://discordpy.readthedocs.io/en/latest/index.html)
* [async-await article](https://snarky.ca/how-the-heck-does-async-await-work-in-python-3-5/)