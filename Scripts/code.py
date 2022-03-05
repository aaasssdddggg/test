
import datetime
import time
import smtplib


while(True):
    time.sleep(5)  # 5 seconds.
    # creates SMTP session
    # s = smtplib.SMTP('smtp.gmail.com', 587)

    # # start TLS for security
    # s.starttls()

    # # Authentication
    # s.login("testgoodenough@gmail.com", "testgoodenough@123")

    # # message to be sent
    # message = "this is a test222"

    # # sending the mail
    # s.sendmail("sender_email_id", "xpxpfarah@gmail.com", message)

    # # terminating the session
    # s.quit()

    # to print the id of the records added in the collection(for debugging, this value can be observed in the heroku logs)
    print("now changed.. this is a test 4")
