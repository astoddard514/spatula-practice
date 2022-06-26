# imports we'll use in this example
from spatula import (
    HtmlPage, HtmlListPage, CSS, XPath, SelectorError
)


class EmployeeList(HtmlListPage):
    source = "https://yoyodyne-propulsion.herokuapp.com/staff"

    # each row represents an employee
    selector = CSS("#employees tbody tr")

    def process_item(self, item):
        # this function is called for each <tr> we get from the selector
        # we know there are 4 <tds>
        first, last, position, details = item.getchildren()
        return dict(
            first=first.text,
            last=last.text,
            position=position.text,
        )

class EmployeeDetail(HtmlPage):
    def process_page(self):
        marital_status = CSS("#status").match_one(self.root)
        children = CSS("#children").match_one(self.root)
        hired = CSS("#hired").match_one(self.root)
        return dict(
            marital_status=marital_status.text,
            children=children.text,
            hired=hired.text,
        )