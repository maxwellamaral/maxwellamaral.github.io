-- PostgreSQL
DROP TABLE IF EXISTS products;
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    category VARCHAR(255) NOT NULL,
    date_purchase DATE NOT NULL,
    date_final DATE NOT NULL,
    price NUMERIC(10, 2) NOT NULL,
    discount NUMERIC(10, 2) NOT NULL,
    price_liquid NUMERIC(10, 2) NOT NULL,
    price_final NUMERIC(10, 2) NOT NULL,
    quantity INTEGER NOT NULL,
    extended_warranty_price NUMERIC(10, 2) NOT NULL,
    extended_warranty_price_final NUMERIC(10, 2) NOT NULL,
    warranty_days NUMERIC(10, 0) NOT NULL,
    extended_warpyranty_days NUMERIC(10, 0) NOT NULL
);
