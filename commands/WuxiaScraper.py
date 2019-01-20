import re

from bs4 import BeautifulSoup
from html2text import html2text
from requests import get


def inc_chapter_num(url):
    notNums = re.findall("[^0-9]", url)
    nums = re.findall("[0-9]", url)
    return ''.join(notNums) + str(int(''.join(nums)) + 1)


def get_title(soup):
    chapter_section = soup.find("div", {"class", "caption clearfix"})
    if chapter_section is not None:
        chapter_title = [chapter.find("h4") for chapter in chapter_section]
        return html2text(str(chapter_title[5])).strip('#')


def get_body(soup):
    main_text = soup.find_all("div", {"class": "fr-view"})
    if main_text is not None:
        paragraphs = [text.find_all("p") for text in main_text]
        text = ""
        for p in paragraphs:
            if not str(p).__contains__("<a"):
                # Removes paragraphs with Hyperlinks, generally the end translator notes
                text += str(p)
        return html2text(text).replace("\n,\n", "")


def get_chapter(url):
    soup = BeautifulSoup(get(url).text, "html.parser")
    title = get_title(soup)
    text = get_body(soup)
    if title is not None and text is not None:
        return ('\n\n' + title + '\n\n' + text).replace("\n]\n", "").replace("\n[\n", "")
    else:
        return None


def scrape_wuxia_chapters(url, chap_count):
    story = ""
    while chap_count > 0:
        chapter_text = get_chapter(url)
        if chapter_text is not None:
            story += chapter_text
        else:
            story += "\n CURRENT END CHAPTER REACHED \n\n"
            break
        url = inc_chapter_num(url)
        chap_count -= 1
    return story


if __name__ == "__main__":
    print(scrape_wuxia_chapters("https://www.wuxiaworld.com/novel/renegade-immortal/rge-chapter-1300", 1))
