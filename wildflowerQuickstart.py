from spatula import (
    HtmlPage, HtmlListPage, CSS, XPath, SelectorError
)


class WildflowerList(HtmlListPage):
    source = "https://www.minnesotawildflowers.info/page/plants-by-name"

    # each row represents a wildflower
    selector = CSS(".wfList tbody tr")

    def process_item(self, item):
        # this function is called for each <tr> we get from the selector
        # we know there are 4 <tds>
        Latin, common = item.getchildren()
        return dict(
            Latin=Latin.text,  # next thing to research is scraping just the <a> text from these links
            common=common.text,
        )

