from fuze.model import Model


class Category(Model):
    __slots__ = [
        "id",
        "label",
        "parent_id"
    ]

    def deflate(self):
        return {
            "id": self.id,
            "label": self.label,
            "parent_id": self.parent_id
        }

    def append(self, label):
        return self.ctx.categories.create(label, parent_id=self.id)

    def __repr__(self):
        return "Category#%s - %s" % (str(self.id), self.label)