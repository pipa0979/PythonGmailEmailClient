'''
import requests
def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandbox7fd532089e6947e5a15253df9c3ba8ce.mailgun.org/messages",
        auth=("api", "key-b071a41098e64c97edb26f6a913d7803"),
        data={"from": "Mailgun Sandbox <postmaster@sandbox7fd532089e6947e5a15253df9c3ba8ce.mailgun.org>",
              "to": "Piyush Sudip Patel <pipa0979@colorado.edu>",
              "subject": "Hello Piyush Sudip Patel",
              "text": "Congratulations Piyush Sudip Patel, you just sent an email with Mailgun!  You are truly awesome!  You can see a record of this email in your logs: https://mailgun.com/cp/log .  You can send up to 300 emails/day from this sandbox server.  Next, you should add your own domain so you can send 10,000 emails/month for free."})

send_simple_message()
'''

'''
import smtplib
fromaddr = 'pipa09799@gmail.com'
toaddrs  = 'pipa09799@gmail.com'
msg = 'Why,Oh why!'
username = 'pipa09799'
password = 'hackcu123'
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
'''



'''
@royskatt : I just got a fix for the issue you where facing. Google has a setting to allow access for less secure apps you just have to turn it 'On'. you can get there from : Google-->my account -->Sign-in & security--> Connected apps & sites--> scroll down and you will find 'Allow less secure apps 


'''
import smtplib
def send_email(user, pwd, recipient, subject, body):
	gmail_user = user
	gmail_pwd = pwd
	FROM = user
	TO = recipient if type(recipient) is list else [recipient]
	SUBJECT = subject
	TEXT = body
	# Prepare actual message
	message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
	""" % (FROM, ", ".join(TO), SUBJECT, TEXT)
	try:
		
		server = smtplib.SMTP("smtp.gmail.com", 587)
		server.ehlo()
		server.starttls()
		server.login(gmail_user, gmail_pwd)
		server.sendmail(FROM, TO, message)
		server.close()
		print 'successfully sent the mail'

	except:
		print "failed to send mail"
send_email('pipa09799@gmail.com','hackcu123','pipa09799@gmail.com','hello','test')

