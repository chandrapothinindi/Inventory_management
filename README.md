# Inventory Management System

This is a simple web application for managing inventory products. It allows users to add new products, view existing products, update product information, and delete products.

## Features

- View Products: View a list of all products in the inventory.
- Add Product: Add a new product to the inventory by providing its name, description, and count.
- Update Product: Update the information of an existing product, including its name, description, and count.
- Delete Product: Delete a product from the inventory.

## Technologies Used

- Frontend: HTML, CSS, JavaScript
- Backend: Python (Flask)
- Database: MySQL
- ORM: SQLAlchemy
- Deployment: Localhost

## Prerequisites

Before you begin, ensure you have met the following requirements:
- You have Python installed on your local machine.
- You have MySQL installed on your local machine.
- You have Flask and required dependencies installed (`pip install flask`).

## Installation and Setup

1. Clone the repository
Navigate to the project directory:
bash
Copy code
cd inventory-management
Install dependencies:
bash
Copy code
pip install -r requirements.txt
Create a MySQL database named inventory and import the provided schema file inventory_schema.sql.
Update the database configurations in app.py with your MySQL credentials.
Run the application:
bash
Copy code
python app.py
Open your web browser
Usage
To add a new product, click on the "Add Product" link and fill in the required details.
To update a product, click on the "Update" button next to the product you want to edit and follow the instructions.
To delete a product, click on the "Delete" button next to the product you want to remove.
Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any bugs, feature requests, or enhancements.
