 CREATE SCHEMA Master
 SET search_path TO Master;
 COMMENT ON SCHEMA Master IS 'All columns relating to finance use Dolloars as denomination'
 COMMENT ON SCHEMA Master IS 'Global Timezone for the database is UTC'
 COMMENT ON SCHEMA Master IS 'clarify the users intent before executing the join.'
 
 CREATE TABLE Customers(
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR,
    cutomer_email VARCHAR,
    customer_adress VARCHAR,
    customer_created_at DATETIME,
    customer_last_login DATETIME,
    status VARCHAR
);
COMMENT ON COLUMN Customers.status IS 'the customer status can be "active," "suspended," or "guest."'

CREATE TABLE Products(
    product_id INT PRIMARY KEY,
    product_category VARCHAR,
    product_brand VARCHAR,
    product_description VARCHAR,
    product_retial_price DECIMAL(9, 2),
    product_wholesle_cost DECIMAL(9, 2)
    status VARCHAR
);
COMMENT ON COLUMN Products.status IS 'the products status can be "in-stock"," "backordered," or "discontinued."'
COMMENT ON COLUMN Product.product_retial_price IS 'Use this column only for current retail catalog pricing.'
COMMENT ON COLUMN products.product_category IS 'If the user asks for a category but does not specify which one, you must prompt them to choose from the available categories.'

CREATE TABLE Orders(
    order_id INT PRIMARY KEY,
    customer_id INT REFERENCES Customers(customer_id)
    order_total_cost DECIMAL(9,2),
    order_placed DATETIME,
    order_processed DATETIME,
    order_shipped DATETIME,
    status VARCHAR
);
COMMENT ON COLUMN Orders.status IS 'the order status can be "pending," "processing," "shipped," or "refunded."'
COMMENT ON COLUMN Orders.order_total_cost IS 'total cost of the order inclusive of shiiping charges and taxes.'
COMMENT ON COLUMN Orders.order_placed IS 'the default for general revenue queries'
COMMENT ON COLUMN Orders.shipped IS 'only be used for fulfillment queries.'

CREATE TABLE Line(
    Line_id INT PRIMARY KEY,
    order_id INT REFERENCES Orders(order_id),
    product_id INT REFERENCES Products(product_id),
    product_volume INT,
    product_price_checkout DECIMAL(9, 2),
    product_discount_checkout DECIMAL(9, 2),
);
COMMENT On COLUMN Line.product_price_checkout IS 'Use this column for calculating historical revenue and past order totals'