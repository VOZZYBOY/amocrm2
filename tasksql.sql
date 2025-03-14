
CREATE TABLE cities (
    id INT,
    name TEXT
);

CREATE TABLE companies (
    id INT,
    name TEXT
);

CREATE TABLE offices (
    id INT,
    name TEXT,
    company_id INT,
    city_id INT
);

SELECT name 
FROM offices 
WHERE company_id = 1;


SELECT name 
FROM offices 
WHERE company_id = 1 AND city_id = 1;


SELECT c.name 
FROM companies c, offices o 
WHERE c.id = o.company_id AND o.city_id = 1; 