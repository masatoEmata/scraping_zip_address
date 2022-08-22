from dataclasses import dataclass
from keywords_extractor import KeywordsExtractor
from file_handler import FileHandler
from invoke_scraper import InvokeScraper


SELECTOR='desktop-title-content'
REGEX = '.*(\d{3}-\d{4}).*'


@dataclass
class Chunk:
    keys: list
    index: int
    chunk_len: int


def scrape_target(key_chunk):
    scraper = InvokeScraper(selector=SELECTOR)
    extractor = KeywordsExtractor(regex=REGEX)
    targets = []
    for key in key_chunk:
        string = scraper.scrape(key)
        zip = extractor.extract_zip(string)
        targets.append(zip) if zip else 'not found'
    return targets

def combine_rows(keys: list, results: list):
    dataset = zip(keys, results)
    rows = [[key, result] for key, result in dataset]
    return rows

def select_key_chunk(chunk: Chunk):
    chunk_start_index = chunk.index
    chunk_end_index = chunk_start_index + chunk.chunk_len - 1
    return chunk.keys[chunk_start_index: chunk_end_index]

def generate_rows_chunk(chunk: Chunk):
    key_chunk = select_key_chunk(chunk)
    result_chunk = scrape_target(key_chunk)
    combined_rows = combine_rows(key_chunk, result_chunk)
    return combined_rows

def main():
    file_handler = FileHandler()
    chunk_len = 5
    keys = file_handler.read_rows(file_path='data/keywords.csv')
    keys_len = len(keys)

    for i in range(0, keys_len, chunk_len):
        chunk = Chunk(keys, i, chunk_len)
        rows_chunk = generate_rows_chunk(chunk)
        file_handler.write_rows(file_path='data/results.csv', header=None, rows=rows_chunk)
        # print('adding csv: ', rows[-1])

main()
