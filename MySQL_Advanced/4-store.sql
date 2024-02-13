-- Trigger to decrease item quantity on new order
DELIMITER $$

CREATE TRIGGER after_order_insert
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number_ordered
    WHERE id = NEW.item_id;
END$$

DELIMITER ;
