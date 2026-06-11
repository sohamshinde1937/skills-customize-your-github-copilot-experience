# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a RESTful API using the FastAPI framework. You'll create a product catalog API that handles HTTP requests, manages data in memory, and returns JSON responses. This assignment teaches you modern API design principles and web framework fundamentals.

## 📝 Tasks

### 🛠️ Set Up a Basic FastAPI Server

#### Description
Create a FastAPI application with initial endpoints that form the foundation of your product catalog API. Configure the server to run locally and respond to HTTP requests.

#### Requirements
Completed program should:

- Import FastAPI and create a FastAPI application instance
- Define a root endpoint (`/`) that returns a welcome message
- Define a GET endpoint (`/products`) that returns a list of sample products as JSON
- Run the server using `uvicorn` on `localhost:8000`
- Be able to test endpoints using a browser or tools like curl/Postman

### 🛠️ Implement CRUD Operations

#### Description
Extend your API to support Create, Read, Update, and Delete operations on products. Each product should have properties like id, name, price, and description.

#### Requirements
Completed program should:

- Implement POST `/products` to add a new product to the catalog
- Implement GET `/products/{product_id}` to retrieve a specific product by ID
- Implement PUT `/products/{product_id}` to update an existing product
- Implement DELETE `/products/{product_id}` to remove a product
- Return appropriate HTTP status codes (200, 201, 404, etc.)
- Validate product data (e.g., price must be positive)

### 🛠️ Add Filtering and Persistence (Stretch Goal)

#### Description
Enhance your API with query parameters for filtering products and save the product catalog to a JSON file so data persists between server restarts.

#### Requirements
Completed program should:

- Support query parameters to filter products by name or price range (`/products?min_price=10&max_price=100`)
- Save all products to a `products.json` file whenever changes are made
- Load products from `products.json` when the server starts
- Handle file I/O gracefully (create the file if it doesn't exist)
