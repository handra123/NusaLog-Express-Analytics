CREATE DATABASE IF NOT EXISTS nusalog_express;
USE nusalog_express;

-- ============================================
-- 1. Table: warehouses
-- ============================================
CREATE TABLE warehouses (
    warehouse_id INT PRIMARY KEY AUTO_INCREMENT,
    warehouse_name VARCHAR(100) NOT NULL,
    city VARCHAR(50) NOT NULL,
    region VARCHAR(50) NOT NULL,
    daily_shipment_capacity INT NOT NULL
);

-- ============================================
-- 2. Table: couriers
-- ============================================
CREATE TABLE couriers (
    courier_id INT PRIMARY KEY AUTO_INCREMENT,
    courier_name VARCHAR(100) NOT NULL,
    warehouse_id INT NOT NULL,
    vehicle_type VARCHAR(20) NOT NULL,
    daily_delivery_capacity INT NOT NULL,
    FOREIGN KEY (warehouse_id) REFERENCES warehouses(warehouse_id)
);

-- ============================================
-- 3. Table: routes
-- ============================================
CREATE TABLE routes (
    route_id INT PRIMARY KEY AUTO_INCREMENT,
    origin_warehouse_id INT NOT NULL,
    destination_warehouse_id INT NOT NULL,
    distance_km DECIMAL(6,2) NOT NULL,
    standard_delivery_days INT NOT NULL,
    FOREIGN KEY (origin_warehouse_id) REFERENCES warehouses(warehouse_id),
    FOREIGN KEY (destination_warehouse_id) REFERENCES warehouses(warehouse_id)
);

-- ============================================
-- 4. Table: customers
-- ============================================
CREATE TABLE customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_name VARCHAR(100) NOT NULL,
    city VARCHAR(50) NOT NULL,
    customer_type VARCHAR(20) NOT NULL
);

-- ============================================
-- 5. Table: shipments (fact table)
-- ============================================
CREATE TABLE shipments (
    shipment_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT NOT NULL,
    courier_id INT NOT NULL,
    route_id INT NOT NULL,
    shipment_date DATE NOT NULL,
    package_weight_kg DECIMAL(5,2) NOT NULL,
    shipping_cost DECIMAL(10,2) NOT NULL,
    estimated_delivery_date DATE NOT NULL,
    actual_delivery_date DATE NOT NULL,
    shipment_status VARCHAR(20) NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (courier_id) REFERENCES couriers(courier_id),
    FOREIGN KEY (route_id) REFERENCES routes(route_id)
);

-- ============================================
-- Indexes (optimasi query analitik)
-- ============================================
CREATE INDEX idx_shipments_status ON shipments(shipment_status);
CREATE INDEX idx_shipments_date ON shipments(shipment_date);
CREATE INDEX idx_shipments_courier ON shipments(courier_id);
CREATE INDEX idx_shipments_route ON shipments(route_id);