#! python3
# whatsapp_bot.pyw - Checks for command quotes on the whatsapp web html page, then executes a set of instructions based on what the commands are

# Instructions:
# Run the code, log in into whatsapp web from the browser, and click on the chat you want the script to listen to, then just let it run in the background

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# TODO: Get Browser
##browser = webdriver.Chrome()
##browser.get('https://web.whatsapp.com')

# TODO: Class abstractions of the commands and input

class Input(object):

    input_checker = 'Type a message'

    def __init__(self,browser):
        
        self.input_xpath = '''//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'''
        self.input_field = None
        self.browser = browser

    def getInputfield(self):

        return self.input_field

    def getXpath(self):

        return self.input_xpath

    def findInputfield(self):
    #Make sure to nest this is some kind of loop, probably a while loop.
        try:
            self.input_field = self.browser.getBrowser().find_element_by_xpath(self.input_xpath)

        except NoSuchElementException:

            pass

    def setInput(self,message):

        assert self.input_field != None
        self.input_field.send_keys(message + Keys.RETURN)
        print('Message Sent')

        
class Browser(object):

    def __init__(self, webpage):

        self.browser = webdriver.Chrome()
        self.webpage = webpage
        self.msgs = None

    def getWebpage(self):

        return self.browser.get(self.webpage)

    def setMsgs(self):

        assert self.webpage == 'https://web.whatsapp.com'
        self.msgs = self.browser.find_elements_by_xpath('''//*[@id="main"]/div[3]/div/div/div[3]//descendant::div''')
        pass

    def getMsgs(self):

        assert self.msgs != None
        self.setMsgs()
        return self.msgs
    
    def getBrowser(self):

        return self.browser



class Command(object):

    def __init__(self,command,input):

        self.command = command
        self.description = 'No description yet.'
        self.counter = 0
        self.execute = 0
        self.input = input
        self.output = None
        

    def setCounter(self,int):

        self.counter = int
        pass

    def getCounter(self):

        return self.counter

    def setExecute(self,int):

        self.execute = int
        pass

    def getExecute(self):

        return self.execute

    def resetCounters(self):

        self.setCounter(0)
        self.setExecute(0)

        pass

    def __str__(self):

        return self.command
    
    def run(self):

        print('No action occurred')
        pass

    def getOutput(self):

        return self.output
    
    def getDesc(self):
        
        return self.description

    def getCommand(self):

        return self.command

#TODO: Create a class of commands parented to Command object.

class Link(Command):

    def __init__(self,command,input):
        
        Command.__init__(self,command,input)
        self.description = 'Copy and pastes desired link to the whatsapp group'
        self.output = 'https://www.notion.so/cyun/Dec-19-V1-Chalet-955c0fd2e0d249bd8fd433d12ec8cdcd'
        
        
    def run(self):


        return self.input.setInput(self.getOutput())

def helpFunction(list):

    string = ['List of commands:']
    for i in list:

        string.append('%s - %s \n' % (i.getCommand(),i.getDesc()))

    return string

class Help(Command):

    def __init__(self,command,input,list):

        Command.__init__(self,command,input)
        self.description = 'Returns a list of commands available'
        self.list = list
        self.output = 'End of !help'

    def run(self):

        print('Sending help...')

        for i in helpFunction(self.list):

            self.input.setInput(i)

        return self.input.setInput(self.getOutput())

class Price(Command):

    def __init__(self,command,input):
        
        Command.__init__(self,command,input)
        self.description = 'Check the current price for chalet'
        self.output = 'Current price per person is at $111.13 for those staying in, and $74.13 for those who are not. Accurate as of 29/11/2019.'

    def run(self):

        return self.input.setInput(self.getOutput())

class People(Command):

    def __init__(self,command,input):
        
        Command.__init__(self,command,input)
        self.description = 'Finds number of people currenly going for chalet, and lists them out'
        self.output = 'There are currently 9 confirmed people for chalet. Only Josh and Pei Zhen are not staying over. (Jonathan, Joshua, Pei Zhen, Jolie, Hiromi, Yuuka, Kirby, Sheng Cheng, Chun Yu)'
        
        
    def run(self):


        return self.input.setInput(self.getOutput())



#TODO: Event listener on infinite Loop:

def execute(browser,input):

##    browser = Browser('https://web.whatsapp.com')
##    browser.getWebpage()
##    input = Input(browser)
    commandList = []
    commandList.extend([Help('!help',input,commandList),Link('!link',input),Price('!price',input),People('!people',input)])
    
##    try:
        
    while True:
        #This loops finds the msgs and the input fields
        try:
            browser.setMsgs()
            input.findInputfield()
                

            if len(browser.getMsgs()) > 0 and input.getInputfield() != None:
                print('Input field found')
                print('Messages found')
                break

        except NoSuchElementException:
            print('MessageError found')
            continue

    while True:
        #This loop executes any set of instructions by searching then running the command

        #TODO: Check the messages for any commands

        for i in browser.getMsgs():

            try:
                print('Currently checking msg: %s' % (i.text))
                for item in commandList:

                    if str(item) == i.text:
                        item.setCounter(item.getCounter() + 1)
##                      print('Counter at %s' % (item.getCounter()))
                    
                        
                    if str(item.getOutput()) == i.text:
                        item.setExecute(item.getExecute() + 1)
##                      print('Execute at %s' % (item.getExecute()))
                        
            except StaleElementReferenceException:
                    continue

        for item in commandList:

            if item.getCounter() > item.getExecute():

                print('Running')
                item.run()

            item.resetCounters()

            
                    
                    #linkCommand()
            
        #TODO: Check if command has already been ran
        #TODO: Run the command
        #TODO: Keep listening for commands

##    except KeyboardInterrupt:
##        print('\nCancelled')

browser = Browser('https://web.whatsapp.com')
browser.getWebpage()
input = Input(browser)

while True:

    try:
        
    
        execute(browser,input)

    except StaleElementReferenceException:
    
        continue

    except KeyboardInterrupt:

        print('\nCancelled')
        break


    



