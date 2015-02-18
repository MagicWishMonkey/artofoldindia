from fuze.model import Model


class Product(Model):
    __slots__ = [
        "id",
        "label",
        "description"
    ]


    def deflate(self):
        return {
            "id": self.id,
            "label": self.label,
            "description": self.description
        }



