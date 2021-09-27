import smtplib, ssl

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "piLitterRobot@gmail.com"
receiver_email = "kaiju466@gmail.com"
password = "Ezekiel!180"#input("Type your password and press enter:")
subject="Subject:"

cycle_count=1
cycle_num_max=4
numInterval_Hours=6

context = ssl.create_default_context()
def notify(sbj,msg):
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        sbj=subject+sbj
        server.sendmail(sender_email, receiver_email, sbj+" \n"+msg)

#notify("besttest","testing 123")
notify("Starting piLitterRobot","piLitterRobot has started it's run cycle. Will cycle "+str(cycle_num_max)+" times every "+str(numInterval_Hours)+" hours")
   
    
    
    
    