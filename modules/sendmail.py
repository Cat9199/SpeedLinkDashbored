import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_daily_report_email(x, y, z, name,receiver_email):
    smtp_server = 'smtp.zoho.com'
    smtp_port = 587
    sender_email = 'admin@speedlink-delivery.com'
    sender_password = 'TkqmjJaPDiHJ'
    html_body = f"""
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <style>
        body {{
          font-family: 'Arial', sans-serif;
          background-color: #f0f0f0;
          margin: 0;
          padding: 0;
        }}
        .container {{
          max-width: 700px;
          margin: 0 auto;
          padding: 30px;
          background-color: #ffffff;
          border-radius: 15px;
          box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }}
        .logo {{
          display: block;
          max-width: 150px;
          margin: 0 auto;
          padding-bottom: 30px;
        }}
        .header {{
          color: #FF0040;
          font-size: 40px;
          font-weight: bold;
          margin-bottom: 30px;
          text-align: center;
          text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
        }}
        .header-image {{
          max-width: 100%;
          height: auto;
          display: block;
          margin: 0 auto;
          margin-bottom: 25px;
          border-radius: 8px;
          box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.15);
        }}
        .message {{
          font-size: 24px;
          line-height: 1.8;
          color: #333333;
          text-align: justify;
          padding: 0 15px;
          border-left: 4px solid #FF0040;
          margin-bottom: 30px;
        }}
        .wallet {{
          font-size: 28px;
          color: #28a745;
          font-weight: bold;
          margin-top: 30px;
          text-align: center;
        }}
        .link {{
          color: #007bff;
          text-decoration: none;
          font-weight: 600;
        }}
        .social-icons {{
          text-align: center;
          margin-top: 40px;
        }}
        .social-icon {{
          display: inline-block;
          margin: 0 15px;
          font-size: 30px;
        }}
        .social-icon img {{
          width: 50px;
          height: 50px;
          border-radius: 50%;
          transition: transform 0.3s ease-in-out;
        }}
        .social-icon img:hover {{
          transform: scale(1.2);
        }}
        .footer {{
          text-align: center;
          color: #888888;
          margin-top: 40px;
          font-size: 16px;
          opacity: 0.8;
        }}
        .button-link {{
          display: inline-block;
          padding: 10px 20px;
          background-color: #007bff;
          color: #ffffff;
          font-size: 18px;
          font-weight: bold;
          text-decoration: none;
          border-radius: 5px;
          transition: background-color 0.3s ease-in-out;
        }}
        .button-link:hover {{
          background-color: #0056b3;
        }}
      </style>
    </head>
    <body>
      <div class="container">
        <img class="logo" src="https://raw.githubusercontent.com/Cat9199/SpeedLinkSys/main/static/images/logob.png" alt="SpeedLink Logo">
        <div class="header">
          <img class="header-image" src="https://e3.365dm.com/20/12/1600x900/skynews-delivery-parcel-post_5203539.jpg?20201211153222" alt="Header Image">
          Your Daily Report from SpeedLink
        </div>
        <p>Hello,{name}</p>
        <p class="message">Exciting news! Your shipment, <strong>Your Shipment{x}</strong>, has successfully arrived at <strong>{y}</strong>.</p>
        <p class="wallet">In addition, an amount of <strong>{z} L.E</strong> has been added to your wallet.</p>
        <p>Feel free to check your updated wallet balance by clicking <a href="YOUR_WALLET_LINK_HERE" class="button-link">here</a>.</p>

        <div class="social-icons">
          <a href="YOUR_FACEBOOK_LINK" class="social-icon"><img src="https://cdn-icons-png.flaticon.com/512/124/124010.png" alt="Facebook"></a>
          <a href="YOUR_TWITTER_LINK" class="social-icon"><img src="https://cdn-icons-png.flaticon.com/512/1006/1006771.png" alt="Twitter"></a>
          <a href="YOUR_INSTAGRAM_LINK" class="social-icon"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Instagram_icon.png/2048px-Instagram_icon.png" alt="Instagram"></a>
        </div>
        <div class="footer">Thank you for choosing SpeedLink Delivery! If you have any questions, contact us at support@speedlink-delivery.com.</div>
      </div>
    </body>
    </html>"""
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = 'Your Daily Report from SpeedLink'
    message.attach(MIMEText(html_body, 'html'))
    smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
    smtp_connection.starttls()
    smtp_connection.login(sender_email, sender_password)
    smtp_connection.sendmail(sender_email, receiver_email, message.as_string())
    smtp_connection.quit()
    print('Email sent successfully!')
