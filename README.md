<p align="center">
  <img src="https://raw.githubusercontent.com/Cat9199/SpeedLinkSys/main/static/images/logob.png" alt="SpeedLink Logo" width="512">
</p>

## SpeedLink Flask Application


SpeedLink is a Flask-based web application that manages shipments, shippers, deliveries, and related functionalities.

## Description

This application provides functionalities for managing shipments, shippers, deliveries, and more. It uses Flask as the web framework and SQLAlchemy for database interaction. Users with different roles, such as admins, shippers, and deliveries, can log in and perform various actions related to shipments and accounts.

## Features

- **Authentication:** Users can log in using their credentials, and their roles determine their access rights.

- **Admin Dashboard:** Admins can view and manage shipments, shippers, and deliveries.

- **Shipper Dashboard:** Shippers can manage their own shipments, track status, and more.

- **Delivery Dashboard:** Deliveries have a dedicated dashboard for their tasks.

- **Adding Shipments:** Shippers can add new shipments, providing recipient details, pricing, and more.

- **Barcode Handling:** The application includes barcode extraction and decoding functionalities.

- **Price Management:** Shipping prices for various cities can be configured and managed.

## Setup Instructions

1. Clone the repository to your local machine:
```
<<<<<<< HEAD
git clone https://github.com/your-username/speedlink-flask-app.git
=======
git clone https://github.com/Cat9199/SpeedLinkSys.git
>>>>>>> origin/main
```

2. Navigate to the project directory:
```
<<<<<<< HEAD
cd speedlink-flask-app
=======
cd SpeedLinkSys
>>>>>>> origin/main
```

3. Install the required dependencies using pip:
```
pip install -r requirements.txt
```


4. Configure the application:
- Update the `app.config['SQLALCHEMY_DATABASE_URI']` with your database URI in the `app.py` file.
- Modify other configuration settings if needed.

5. Run the application:
```
python app.py
```


6. Access the application in your web browser at `http://localhost:2000`.


## Routes
### Index
![SpeedLink Logo](https://raw.githubusercontent.com/Cat9199/SpeedLinkSys/main/img/home.png)

- **URL:** `/`
- **Description:** Home page of the application.

### Setting
![SpeedLink Logo](https://raw.githubusercontent.com/Cat9199/SpeedLinkSys/main/img/setting.png)

- **URL:** `/setting`
- **Description:** Displays user settings.

### Login
![SpeedLink Logo](https://raw.githubusercontent.com/Cat9199/SpeedLinkSys/main/img/login.png)

- **URL:** `/login`
- **Description:** Handles user login.

### Dashboard
![SpeedLink Logo](https://raw.githubusercontent.com/Cat9199/SpeedLinkSys/main/img/admin.png)

- **URL:** `/dashboard`
- **Description:** Displays the dashboard.
### Users
![SpeedLink Logo](https://raw.githubusercontent.com/Cat9199/SpeedLinkSys/main/static/images/logob.png)

- **URL:** `/users`
- **Description:** Displays a list of users.

### Print Form
![SpeedLink Logo](https://raw.githubusercontent.com/Cat9199/SpeedLinkSys/main/static/images/logob.png)

- **URL:** `/print`
- **Description:** Displays a print form.

### Print (POST)
![SpeedLink Logo](https://raw.githubusercontent.com/Cat9199/SpeedLinkSys/main/static/images/logob.png)

- **URL:** `/pud`
- **Description:** Handles a POST request to print shipments.

### Mark as Printed
![SpeedLink Logo](https://raw.githubusercontent.com/Cat9199/SpeedLinkSys/main/static/images/logob.png)

- **URL:** `/asprint/<username>`
- **Description:** Marks shipments as printed.

### Track Shipment
![SpeedLink Logo](https://raw.githubusercontent.com/Cat9199/SpeedLinkSys/main/static/images/logob.png)

- **URL:** `/track/<barcode>`
- **Description:** Tracks a shipment by barcode.


### Logout
![SpeedLink Logo](https://raw.githubusercontent.com/Cat9199/SpeedLinkSys/main/static/images/logob.png)

- **URL:** `/logout`
- **Description:** Logs the user out.

### Deliveries
![SpeedLink Logo](https://raw.githubusercontent.com/Cat9199/SpeedLinkSys/main/static/images/logob.png)

- **URL:** `/deliv`
- **Description:** Displays delivery information.

### Delete Shipment
![SpeedLink Logo](https://raw.githubusercontent.com/Cat9199/SpeedLinkSys/main/static/images/logob.png)

- **URL:** `/del/<id>`
- **Description:** Deletes a shipment.

### Print Shipment (POST)
![SpeedLink Logo](https://raw.githubusercontent.com/Cat9199/SpeedLinkSys/main/static/images/logob.png)

- **URL:** `/pa`
- **Description:** Handles a POST request to print shipments.



### Stop Shipping
![SpeedLink Logo](https://raw.githubusercontent.com/Cat9199/SpeedLinkSys/main/static/images/logob.png)

- **URL:** `/stopshipping/<id>`
- **Description:** Stops shipping for a shipment.

### Stop
![SpeedLink Logo](https://raw.githubusercontent.com/Cat9199/SpeedLinkSys/main/static/images/logob.png)

- **URL:** `/stop`
- **Description:** Stops shipments for the delivery.

### Mark as Read Notification
![SpeedLink Logo](https://raw.githubusercontent.com/Cat9199/SpeedLinkSys/main/static/images/logob.png)

- **URL:** `/makeasreed/<id>`
- **Description:** Marks a notification as read.

### Add Shipper
![SpeedLink Logo](https://raw.githubusercontent.com/Cat9199/SpeedLinkSys/main/static/images/logob.png)

- **URL:** `/adds`
- **Description:** Displays a form to add a shipper account.

### Add Delivery
![SpeedLink Logo](https://raw.githubusercontent.com/Cat9199/SpeedLinkSys/main/static/images/logob.png)

- **URL:** `/addd`
- **Description:** Displays a form to add a delivery account.

### Add Shipment
![SpeedLink Logo](https://raw.githubusercontent.com/Cat9199/SpeedLinkSys/main/static/images/logob.png)

- **URL:** `/addushipment`
- **Description:** Displays a form to add a new shipment.

### Add File
![SpeedLink Logo](https://raw.githubusercontent.com/Cat9199/SpeedLinkSys/main/static/images/logob.png)

- **URL:** `/addfile`
- **Description:** Displays a form to add a file.

### Send to Delivery
![SpeedLink Logo](https://raw.githubusercontent.com/Cat9199/SpeedLinkSys/main/static/images/logob.png)

- **URL:** `/sendtodelivery`
- **Description:** Sends shipments to delivery.

### Set Shipment
![SpeedLink Logo](https://raw.githubusercontent.com/Cat9199/SpeedLinkSys/main/static/images/logob.png)

- **URL:** `/setship`
- **Description:** Sets the delivery for a shipment.

### View Shipments
![SpeedLink Logo](https://raw.githubusercontent.com/Cat9199/SpeedLinkSys/main/static/images/logob.png)

- **URL:** `/viweshipping`
- **Description:** Displays all shipments.

### View Wallets
![SpeedLink Logo](https://raw.githubusercontent.com/Cat9199/SpeedLinkSys/main/static/images/logob.png)

- **URL:** `/viwewallets`
- **Description:** Displays all wallets.

### Notifications
![SpeedLink Logo](https://raw.githubusercontent.com/Cat9199/SpeedLinkSys/main/static/images/logob.png)

- **URL:** `/notifications`
- **Description:** Displays notifications.

### Extract Barcode
![SpeedLink Logo](https://raw.githubusercontent.com/Cat9199/SpeedLinkSys/main/static/images/logob.png)

- **URL:** `/extract_barcode`
- **Description:** Extracts barcode data from an image.

### Change Shipment Status
![SpeedLink Logo](https://raw.githubusercontent.com/Cat9199/SpeedLinkSys/main/static/images/logob.png)

- **URL:** `/changstates/<barcode>`
- **Description:** Changes the shipment status.

### Profile
![SpeedLink Logo](https://raw.githubusercontent.com/Cat9199/SpeedLinkSys/main/static/images/logob.png)

- **URL:** `/profile`
- **Description:** Displays user profile.

### View Wallets by Code
![SpeedLink Logo](https://raw.githubusercontent.com/Cat9199/SpeedLinkSys/main/static/images/logob.png)

- **URL:** `/viwewallets/<wallet_code>`
- **Description:** Displays wallets by wallet code.

### Update Profile
![SpeedLink Logo](https://raw.githubusercontent.com/Cat9199/SpeedLinkSys/main/static/images/logob.png)

- **URL:** `/update_profile/<admin_id>`
- **Description:** Updates the admin profile.

### Delivery Price
![SpeedLink Logo](https://raw.githubusercontent.com/Cat9199/SpeedLinkSys/main/static/images/logob.png)

- **URL:** `/dprice/<sid>`
- **Description:** Displays delivery prices.

### Save Price
![SpeedLink Logo](https://raw.githubusercontent.com/Cat9199/SpeedLinkSys/main/static/images/logob.png)

- **URL:** `/saveprice/<sid>`
- **Description:** Saves delivery prices.

### Tables
![SpeedLink Logo](https://raw.githubusercontent.com/Cat9199/SpeedLinkSys/main/static/images/logob.png)

- **URL:** `/tables/<id>`
- **Description:** Displays shipment tables grouped by delivery date.
### Download Database
- **URL:** `/download_database`
- **Description:** Allows users to download the database file.

## Contributing

Contributions are welcome! If you find any issues or want to enhance the application, feel free to submit a pull request.

## License

<<<<<<< HEAD
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
=======
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
>>>>>>> origin/main