import urllib.parse
import time
from dataclasses import dataclass
from drive_setter import DriveSetter


@dataclass
class InvokeScraper:
    selector: str
    driver = DriveSetter()

    def __generate_url(self, keyword):
        keyword_encoded = urllib.parse.quote(keyword)
        return f'https://google.com/search?q={keyword_encoded}'

    def scrape(self, keyword: str, sleep: int = 2):
        url = self.__generate_url(keyword)
        self.driver.access_page(url)
        time.sleep(sleep)
        try:
            return self.driver.find_address_text(self.selector)

        except:
            return None
