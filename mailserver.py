
import smtplib as s
ob=s.SMTP("smtp.gmail.com",587)

ob.starttls()

ob.login("nsinghboss02@gmail.com",9795357222)

subject="sending email using python"
body="the easiest way to send emails"

message="subject:{}\n\n{}".format(subject,body)
listOfAddress=["singhalokkumar427@gmail.com","nitishtiwari1710@gmail.com","nitin.singh_cs20@gla.ac.in"]
ob.sendmail("nsinghboss02@gmail.com",listOfAddress,message)
print("sent successfully.....")
ob.quit()
