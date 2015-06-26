from fuze import *
from aoi.products import *
from aoi.categories import *


class Context:
    @property
    def products(self):
        return Products(self)

    @property
    def categories(self):
        return Categories(self)
