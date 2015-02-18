from fuze import *
from aoi.products import *


class Context:
    @property
    def products(self):
        return Products(self)
        #return self.get_extension("Members", Members)
