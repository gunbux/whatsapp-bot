# whatsapp-bot
A simple, inefficient whatsapp bot using the selenium module in Python


First project repository on Github. 

The whatsapp bot is a way for people to automate messages without needing an API since Whatsapp doesn't offer a public API. The concept is simple: Using the Selenium module, open up a webbrowser to https://web.whatsapp.com . Afterwards, manually sign in and click on the chat you want the script to listen to. Now, whenever a command is typed and sent into the group, the bot will automatically respond.

<h1>Review of Code</h1>

The code is obviously very sloppy, being the first time web scraping, and a lot of it is spaghetti code and bad error handling just so the script actually works. 
Things to note for future reference: 
<ol>
  <li>The script runs EXTREMELY SLOWLY. I'm not sure whether the script itself is inefficient or that the Selenium modul takes a long time to parse the html elements, but its SLOW.</li>
  
  <li>Its buggy and very bad code. While the code itself works pretty well given that whatsapp does not have an API, it has its drawbacks. For one, because whatsapp web doesn't load all messages, sometimes the command message would've hidden while the output isn't, resulting in the bot not sending an output the next time the command is called since it thinks it has already sent the output</li>
  
  <li>It is very limited at what it can do. (For now) Since I have not added any other API into the script, currently the bot is limited to sending text messages. However, I do plan to change this in future versions</li>
  
</ol>

<h1>Reflections</h1>

All in all, I'm pretty proud of this project, given that this is my first personal project that I actually completed, and that I have never touched Selenium before. Sure the code is extremely sloppy, but its really a learning experience, and it's really not that bad compared to the intial prototype, where I used little to no abstraction, making the code abnormally tedious.

<h1>Todo:</h1>
<ol>
  <li>Connect the Notion API so it can parse infomation from Notion over to Whatsapp</li>
  <li>Connect a Youtube API so that it can send youtube links based on a search result given in Whatsapp</li>
  <li>Connect the script to Google so that the script can run google searches and image searches</li>
</ol>
