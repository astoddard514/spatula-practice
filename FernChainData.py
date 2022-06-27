from spatula import (
    HtmlPage, HtmlListPage, CSS, XPath, SelectorError
)

class FernList(HtmlListPage):
     # by providing this here, it can be omitted on the command line
     # useful in cases where the scraper is only meant for one page
     source = "https://www.minnesotawildflowers.info/page/ferns-and-fern-allies"

     # each row represents an employee
     selector = CSS(".thumbs ul li")

     def process_item(self, item):
         # this function is called for each <tr> we get from the selector
         # we know there are 4 <tds>
        common = item.getchildren()
         # return EmployeeDetail(
        return dict(
            common=common.text,
            )
             # source=XPath("./a/@href").match_one(details),
        

