CREATE DATABASE energy;

USE energy;

CREATE TABLE regions (
    region_id INT PRIMARY KEY AUTO_INCREMENT,
    region_name VARCHAR(100),
    city VARCHAR(100),
    population INT
);

CREATE TABLE energy_production (
    production_id INT PRIMARY KEY AUTO_INCREMENT,
    region_id INT,
    source_type VARCHAR(50),
    energy_generated_kwh DECIMAL(10,2),
    production_time DATETIME,
    FOREIGN KEY (region_id) REFERENCES regions(region_id)
);