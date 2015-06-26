from fuze import *
from aoi import *

def setup_categories(self):
    self.query("INSERT INTO categories (label) VALUES (@label);", label='ACCESSORIES').insert()
    self.query("INSERT INTO categories (label) VALUES (@label);", label='ARCHITECTURAL').insert()
    self.query("INSERT INTO categories (label) VALUES (@label);", label='FURNISHINGS').insert()
    self.query("INSERT INTO categories (label) VALUES (@label);", label='TEXTILES').insert()

    accessories = self.categories.get("ACCESSORIES")
    architecture = self.categories.get("ARCHITECTURAL")
    furnishings = self.categories.get("FURNISHINGS")
    texttiles = self.categories.get("TEXTILES")

    accessories.append("Lighting")
    accessories.append("Mirrors")
    accessories.append("Misc.")

    texttiles.append("Rugs")
    texttiles.append("Antiques")

    architecture.append("Doors")
    architecture.append("Ceilings")
    architecture.append("Columns")
    architecture.append("Arches")
    architecture.append("Misc.")

    furnishings.append("Seating")
    furnishings.append("Tables")
    furnishings.append("Armoires")
    furnishings.append("Trunks")
    furnishings.append("Consoles")
    furnishings.append("Misc.")

    furnishings.append("Tables")
    furnishings.append("Armoires")
    furnishings.append("Trunks")
    furnishings.append("Consoles")
    furnishings.append("Misc.")






def init():
    self = util.context()
    # records = util.unjson(util.file("/Scratch/art_of_old_india_fixed.json").read_text())
    # records = [r for r in records if r["record_type"] != "page"]
    # data = util.json(records, indent=2)
    # print data


    records = self.query("SELECT ID as id, post_content as content, post_title as title, post_excerpt as excerpt, post_status as status, post_name as name, post_parent as parent_id, post_type as record_type, guid as url FROM  asdw2_posts;").select()
    for x, r in enumerate(records):
        for key in r:
            val = r[key]
            if isinstance(val, basestring) is True:
                # if(val.find("<") > -1 and val.find(">") > -1):
                #     val = ""
                # else:
                val = util.fix_str(val)
                val = val.replace('"', "'")
                r[key] = val
        records[x] = r
    data = util.json(records, indent=2)
    util.file("/Scratch/art_of_old_india.json").write_text(data)

    #records = self.query("SELECT * FROM asdw2_posts;").select()
    product = self.products.get(2)

    #self.query("INSERT INTO products (label) VALUES (@label);", label="Wooden Column").insert()
    records = self.query("SELECT * FROM products;").select()
    # network_id = self.query("SELECT ID FROM network ORDER BY ID LIMIT 1;").scalar()
    # network = self.networks.get(network_id)
    # network = self.networks.get(network_id)
    # members = self.members.get(1, 2, 3)
    # networks = self.members.get(1).networks

    print "..."



init()
quit()
