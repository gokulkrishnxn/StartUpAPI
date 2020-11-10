Building a Python Automation Start Up Name 
* Making a list of names in
	bird_list = ['Crow,Peacock,Dove,Sparrow,Goose,Ostrich,Pigeon,Turkey,Hawk,Bald eagle,Raven,Parrot,Flamingo,Seagull,Swallow,Blackbird,Penguin,Robin,Swan,Owl,Stork,Woodpecker']
	Make sure you put Your own list
* Make sure the you put the list name like this
   name = 'bird_list'
 * Make sure you have install selenium by using pip install selenium
   Check your web browser the version on chorme if u have 86. some version then u have to install choremedriver so the selenium can run your driver.
* now check the 
browser = webdriver.Chrome('C:/Users/gokul/AppData/Local/Google/Chrome/Application/chromedriver.exe')
(U have to put your // loaction where is the chrome//path// by puting // chromedriver.exe)
* SO the list will generate a random name 
* it will search the in godaddy.com 
*if it the name has a domain.com then it will print 
there will be a menu like this
----------------------------------
SEARCHING...
----------------------------------
Domain
Warbler.com is available!
What do you want to do?
***********************************
-----------------------------------
-----*****-----MENU-------********-
1. Open up godaddy.com to see more
2. keep searching
3. Quit
if the domain is taken 
it will print
and contiune to search untill one is avaiable
