from fuze import *
from aoi import *


def init():
    self = util.context()
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
