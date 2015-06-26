from fuze import *
from fuze.repository import Repository
# from aoi.categories.category import Category


class Categories(Repository):
    # @property
    # def model_spawn(self):
    #     return Category

    def lookup(self, *keys):
        single = False
        if len(keys) == 1:
            if isinstance(keys[0], list) is False:
                single = True

        labels = util.unroll(keys)
        if len(labels) == 0:
            return None if single is True else []

        query = self.query("SELECT id FROM categories;").where("label=@label", labels)
        keys = query.scalars()
        if single is True:
            return keys[0] if len(keys) > 0 else None
        return keys


@Categories.plugin
def create(self, label, parent_id=None):
    if parent_id is None:
        self.query("INSERT INTO categories (label) VALUES (@label);", label=label).insert()
        return self.get(self.query("SELECT id FROM categories WHERE label=@label;", label=label).scalar())
    else:
        self.query("INSERT INTO categories (label, parent_id) VALUES (@label, @parent_id);", label=label, parent_id=parent_id).insert()
        return self.get(self.query("SELECT id FROM categories WHERE parent_id=@parent_id AND label=@label;", label=label, parent_id=parent_id).scalar())