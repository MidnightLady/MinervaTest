CREATE TABLE IF NOT EXISTS `Djangotest`.`customers` 
( `id` INT AUTO_INCREMENT PRIMARY KEY,
 `cusId` VARCHAR(255) NOT NULL ,
 `name` VARCHAR(255) NOT NULL ,
 `segment` INT NOT NULL ,
 `country` VARCHAR(255) ,
 `city` VARCHAR(255),
 `state` VARCHAR(255),
 `postcode` INT) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `Djangotest`.`categories` 
( `id` INT AUTO_INCREMENT PRIMARY KEY, 
 `name` VARCHAR(255) NOT NULL , 
 `desc` VARCHAR(255) ) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `Djangotest`.`subCategories` 
( `id` INT AUTO_INCREMENT PRIMARY KEY, 
 `name` VARCHAR(255) NOT NULL , 
 `catId` INT NOT NULL ,
 `desc` VARCHAR(255) , 
 FOREIGN KEY fk_sub_cat(catId) REFERENCES categories(id) ON UPDATE CASCADE ON DELETE RESTRICT ) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `Djangotest`.`products` 
( `id` INT AUTO_INCREMENT PRIMARY KEY, 
 `productId` VARCHAR(255) NOT NULL , 
 `name` VARCHAR(255) NOT NULL , 
 `catId` INT NOT NULL , 
 `price` FLOAT NOT NULL , 
 `discount` FLOAT DEFAULT 0, 
 UNIQUE (productId),
 FOREIGN KEY fk_pro_cat(catId) REFERENCES subCategories(id) ON UPDATE CASCADE ON DELETE RESTRICT ) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `Djangotest`.`orders` 
( `id` INT AUTO_INCREMENT PRIMARY KEY,
 `orderId` VARCHAR(255) NOT NULL , 
 `orderDate` DATETIME DEFAULT CURRENT_TIMESTAMP , 
 `shipDate` DATETIME DEFAULT CURRENT_TIMESTAMP , 
 `shipId` INT NOT NULL , 
 `cusId` INT NOT NULL , 
 `productId` INT NOT NULL , 
 `quantity` INT NOT NULL , 
 FOREIGN KEY fk_order_cus(cusId) REFERENCES customers(id) ON UPDATE CASCADE ON DELETE RESTRICT ,
 FOREIGN KEY fk_order_product(productId) REFERENCES products(id) ON UPDATE CASCADE ON DELETE RESTRICT ) ENGINE = InnoDB;



 
INSERT INTO `categories` (`id`, `name`, `desc`) VALUES (1 , 'Furniture', 'Furniture category'), (2, 'Office Supplies', 'Office Supply category');
INSERT INTO `subCategories` (`name`, `catId`, `desc`) VALUES ('Bookcases', '1', NULL), ('Chairs', '1', NULL); 
INSERT INTO `subCategories` (`name`, `catId`, `desc`) VALUES ('Storage', '2', NULL), ('Binders', '2', NULL), ('Labels', '2', NULL); 
INSERT INTO `products` ( `productId`, `name`, `catId`, `price`, `discount`) VALUES ( 'OFF-ST-10000002', 'Alphabetical Labels for Top Tab Filing', '2', '123.22', '25'), ('OFF-ST-10000003', 'Avery 513', '3', '234.55', '0'), ( 'OFF-ST-10000005', 'Canon PC-428 Personal Copier', '4','342.65', '14.12'); 


