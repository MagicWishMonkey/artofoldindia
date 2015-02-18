from fuze import *
from fuze.repository import Repository


class Products(Repository):

    def lookup(self, *keys):
        single = False
        if len(keys) == 1:
            if isinstance(keys[0], list) is False:
                single = True

        emails = util.unroll(keys)
        emails = [util.format_email(email) for email in emails]
        if len(emails) == 0:
            return None if single is True else []

        query = self.query("SELECT MemberID FROM member_email;").where("EmailAddress=@email", emails)
        keys = query.scalars()
        if single is True:
            return keys[0] if len(keys) > 0 else None
        return keys


# @Products.plugin
# def verify(self, email):
#     print "Verify! %s" % email