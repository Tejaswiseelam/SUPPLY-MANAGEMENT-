from flask import Flask, render_template, request, jsonify,url_for
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import threading

app = Flask(__name__)
app = Flask(__name__, static_url_path='/static')

def send_thank_you_email(email):
    sender_email = 'tejaswi.seelam00@gmail.com'  # Replace with your email
    sender_password = 'piez xjbl bvuh tsuw'  # Replace with your email password
    
    subject = 'Unleash the Power of Your Generosity -supply management'
    body = f'''
<p><b>Dear User,</b></p>
<p>In a world where every act of kindness ripples with the potential for change, 
your decision to embrace generosity is a beacon of hope. 
Your actions have the power to transform lives, inspire others, and create a positive impact that resonates far beyond what we can imagine.
<br><b>Your Generosity Lights the Way</b></br>
<br>Your willingness to contribute speaks volumes about your compassionate spirit.
It is a testament to your belief in making the world a better place. 
Whether you are supporting a cause close to your heart or extending a helping hand to those in need,
your generosity is a force that ignites positive change.</br>
Great initiative: {email}</p>
<p><b>Thank You for Choosing Supply Management</b>
<br>We extend our deepest gratitude for choosing Supply Management as your platform for making a positive impact. 
Your commitment aligns seamlessly with our mission, and we are honored to be part of your journey to create a better, more compassionate world.
Thank you for your unwavering support, your kindness, and your dedication to making a difference. 
Together, we can build a brighter future for all.</br>
<br>With heartfelt thanks,</br>
<br><b>The Supply Management Team</b></br></p>
'''
    # Set up the MIME object
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = email
    message['Subject'] = subject

    # Attach body as HTML
    message.attach(MIMEText(body, "html"))

    try:
        # Connect to the SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            print(f"Sender email: {sender_email}")
            server.login(sender_email, sender_password)
            print(f"Logged in as: {sender_email}")
            server.sendmail(sender_email, email, message.as_string())
        print(f"Email sent successfully to {email}")
    except Exception as e:
        print(f"Error sending email to {email}: {str(e)}")

def send_thank_you_email_thread(email):
    thread = threading.Thread(target=send_thank_you_email, args=(email,))
    thread.start()

@app.route('/')
def index():
    return render_template('index.html')  # Assuming you have an HTML form

@app.route('/process_login', methods=['POST'])
def submit():
    if request.method == 'POST':
        email = request.form.get('email')
        send_thank_you_email_thread(email)
        return jsonify({'message': 'Thank you! Check your email for a confirmation.'})

if __name__ == '__main__':
    app.run(debug=True)
 
#value= piez xjbl bvuh tsuw

