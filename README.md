<h1 align="center">ARTIZAN Ecommerce website.</h1><hr>
<h2 align="center">ARTIZAN is an E-commerce website which is dealing with sells a wide variety of products including Clothing, Shoes, Home and Kitchen, Ectronics, Apparel, and Home Improvement.</h2><hr>


<h3>Technologies used :</h3>
<hr>

<h6>❖ Python</h6>
<h6>❖ Django</h6>
<h6>❖ Express js</h6>
<h6>❖ Mysql</h6>
<h6>❖ Javascript</h6>
<h6>❖ Jquery</h6>
<h6>❖ Ajax</h6>
<h6>❖ HTML& CSS</h6>
<h6>❖ Bootstrap</h6>

<h3>Features involved:</h3>
<hr>

<h6>❖Guest user(cart,wishlist)</h6>
<h6>❖  OTP Login and Registration(Twilio)</h6>
<h6>❖ Advanced Payment Options(RazorPay,Paypal)</h6>
<h6>❖ Cash on Delivery</h6>
<h6>❖ Category wise products</h6>
<h6>❖ Responsive Pages</h6>
<h6>❖ User Profile</h6>
<h6>❖ High-Resolution Photos</h6>
<h6>❖ Invoice</h6>
<h6>❖ Add To Cart</h6>
<h6>❖ Product Variation</h6>
<h6>❖ Search</h6>
<h6>❖ Product Filter</h6>
<h6>❖ Address Management</h6>
<h6>❖Product offer and category offer</h6>
<h6>❖ ordered products</h6>


<h3>Admin Side</h3>
 <h6>☆ Dashboard</h3>
 <h6>☆ Responsive Pages</h3>
 <h6>☆ Category Offer, Product Offer, Coupon</h3>
 <h6>☆ Sales Report(pdf,excel)</h3>
 <h6>☆ Charts,Graphs(Chart.js)</h3>
 <h6>☆ Product Management</h3>
 <h6>☆ Category Management</h3>
 <h6>☆ Coupon Management</h3>
 <h6>☆Varaition Management</h3>
 <h6>☆ User Management(block and unblock)</h3>
 <h6>☆ Order Management</h3>


# About The Project
Zanshop is an eCommerce application built with Python Django Framework. Some of the features of this project includes custom user model, categories and products, Carts, Incrementing, Decrementing and removing car items, Unlimited Product image gallery, Orders, Payments, after-order functionalities such as reduce the quantify of sold products, send the order received email, clearing the cart, Order completion page as well as generating an invoice for the order. Also we have a Review and Rating system with the interactive rating stars that even allows you to rate a half-star rating. My account functionalities for the customer who can easily edit his profile, profile pictures, change his account password, and also manage his orders and much more. Finally hosted this application on AWS Elastic Beanstalk


# Setup Instructions
git clone 
1. Navigrate to the working directory `cd project folder`
2. Open the project from the code editor `code .` or `atom .`
3. Create virtual environment `python -m venv env`
4. Activate the virtual environment `source env/Scripts/activate`
5. Install required packages to run the project `pip install -r requirements.txt`
6. Rename _.env-sample_ to _.env_
7. Fill up the environment variables:
    _Generate your own Secret key using this tool [https://djecrety.ir/](https://djecrety.ir/), copy and paste the secret key in the SECRET_KEY field._

    _Your configuration should look something like this:_
    ```sh
    SECRET_KEY=47d)n05#ei0rg4#)*@fuhc%$5+0n(t%jgxg$)!1pkegsi*l4c%
    DEBUG=True
    EMAIL_HOST=smtp.gmail.com
    EMAIL_PORT=587
    EMAIL_HOST_USER=youremailaddress@gmail.com
    EMAIL_HOST_PASSWORD=yourStrongPassword
    EMAIL_USE_TLS=True
    ```
    _Note: If you are using gmail account, make sure to [use app password](https://support.google.com/accounts/answer/185833)_
9. Create database tables
    ```sh
    python manage.py migrate
    ```
10. Create a super user
    ```sh
    python manage.py createsuperuser
    ```
    _GitBash users may have to run this to create a super user - `winpty python manage.py createsuperuser`_
11. Run server
    ```sh
    python manage.py runserver
    ```
12. Login to admin panel - (`http://127.0.0.1:8000/zan123/`)
13. Add categories, products, add variations, register user, login, place orders and EXPLORE SO MANY FEATURES
