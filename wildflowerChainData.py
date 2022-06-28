from spatula import (
    HtmlPage, HtmlListPage, CSS, XPath, SelectorError
)

class WildflowerList(HtmlListPage):
     # by providing this here, it can be omitted on the command line
     # useful in cases where the scraper is only meant for one page
    source = "https://www.minnesotawildflowers.info/page/plants-by-name"

     # each row represents an employee
    selector = CSS(".wfList tbody tr")

    def process_item(self, item):
         # this function is called for each <tr> we get from the selector
         # we know there are 4 <tds>
        details, common = item.getchildren()
        return PlantDetail(
            dict(
                  # next thing to research is scraping just the <a> text from these links
                common=common.text,
                ),
            source=XPath("./a/@href").match_one(details),
         )

class PlantDetail(HtmlPage):
    def process_page(self):
        plant_family = CSS(".wfInfo tbody ").match_one(self.root) #td for th="Family:"
        habitat = CSS(".wfInfo tbody").match_one(self.root) #td for th="Habitat:"
        bloom_season = CSS(".wfInfo tbody").match_one(self.root) #td for th="Bloom season:"
        return dict(
            plant_family=plant_family.text,
            habitat=habitat.text,
            bloom_season=bloom_season.text,
            # self.input is the data passed in from the prior scrape,
            # in this case a dict we can expand here
            **self.input,
        )