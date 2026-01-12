CREATE TABLE clients (
id INT AUTO_INCREMENT PRIMARY KEY,
client_name VARCHAR(100) NOT NULL,
company_name VARCHAR(150) NOT NULL,
city VARCHAR(100),
contact_person VARCHAR(100),
phone VARCHAR(20) NOT NULL,
email VARCHAR(150) UNIQUE NOT NULL
);


CREATE TABLE cases (
id INT AUTO_INCREMENT PRIMARY KEY,
client_id INT NOT NULL,
invoice_number VARCHAR(50) NOT NULL,
invoice_amount DECIMAL(10,2) NOT NULL,
invoice_date DATE NOT NULL,
due_date DATE NOT NULL,
status ENUM('New','In Follow-up','Partially Paid','Closed') DEFAULT 'New',
last_follow_up_notes TEXT,
FOREIGN KEY (client_id) REFERENCES clients(id) ON DELETE CASCADE
);