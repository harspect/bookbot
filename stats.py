from itertools import groupby

def get_num_words(content: str) -> int:
    return len(content.split())

def get_book_text(filePath) -> str:
    with open(filePath) as f:
        content = f.read()
        return content
    
def get_num_characters(content: str) -> dict:
    content = content.lower()
    dictGroup = {k: content.count(k) for k in set(content)}
    return dictGroup

def create_res(characters: dict) -> list:
    ans = [{"char": k, "num": v} for k, v in characters.items()]
    return sorted(ans, key=lambda x: x['num'], reverse=True)