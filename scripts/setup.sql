-- CREATE PRODUCTS TABLE
DROP TABLE IF EXISTS products;
DROP SEQUENCE IF EXISTS products_id_seq;
CREATE SEQUENCE products_id_seq START 1;

DROP TABLE IF EXISTS products;
CREATE TABLE products (
	"id" int4 NOT NULL DEFAULT nextval('products_id_seq'::regclass),
	"label" varchar(250) NOT NULL COLLATE "default",
	"description" varchar(8000) COLLATE "default"
) WITH (OIDS=FALSE);

ALTER TABLE products ADD PRIMARY KEY ("id") NOT DEFERRABLE INITIALLY IMMEDIATE;


-- CREATE CATEGORIES TABLE
DROP TABLE IF EXISTS categories;
DROP SEQUENCE IF EXISTS categories_id_seq;
CREATE SEQUENCE categories_id_seq START 1;

DROP TABLE IF EXISTS categories;
CREATE TABLE categories (
	"id" int4 NOT NULL DEFAULT nextval('categories_id_seq'::regclass),
	"label" varchar(250) NOT NULL COLLATE "default",
	"parent_id" int4
) WITH (OIDS=FALSE);


ALTER TABLE categories ADD PRIMARY KEY ("id") NOT DEFERRABLE INITIALLY IMMEDIATE;

CREATE UNIQUE INDEX  "categories_id_key" ON "public"."categories" USING btree("id" ASC NULLS LAST);
ALTER TABLE "public"."categories" ADD CONSTRAINT "FK_CATEGORY_PARENT_ID" FOREIGN KEY ("parent_id") REFERENCES "public"."categories" ("id") ON UPDATE CASCADE ON DELETE CASCADE NOT DEFERRABLE INITIALLY IMMEDIATE;