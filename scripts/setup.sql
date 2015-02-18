DROP SEQUENCE IF EXISTS products_id_seq;
CREATE SEQUENCE products_id_seq START 1;

DROP TABLE IF EXISTS products;
CREATE TABLE products (
	"id" int4 NOT NULL DEFAULT nextval('products_id_seq'::regclass),
	"label" varchar(250) NOT NULL COLLATE "default",
	"description" varchar(8000) COLLATE "default"
) WITH (OIDS=FALSE);


-- ----------------------------
--  Primary key structure for table queries
-- ----------------------------
ALTER TABLE products ADD PRIMARY KEY ("id") NOT DEFERRABLE INITIALLY IMMEDIATE;