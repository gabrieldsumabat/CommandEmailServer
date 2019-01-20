import re

from commands import WuxiaScraper


def handle_commands(message):
    if message.content.__contains__("getwuxia"):
        match = re.search("getwuxia https://www\.wuxiaworld\.com/[-/a-z0-9]* [0-9]*",
                          message.content.lower())
        if match is not None:
            command, url, num_chapters = match.group().split(" ")
            story_name = url.split('/')[-2]
            return story_name, WuxiaScraper.scrape_wuxia_chapters(url, int(num_chapters))
        else:
            return "ERROR", "Please format input as 'getwuxia [chapter link] [num of chapters desired]"
    else:
        if message.subject.lower().__contains__("help"):
            return "Command List", "getwuxia [Starting Chapter Link] [Number of chapters desired]\n"


if __name__ == "__main__":
    match = re.search("https://www\.wuxiaworld\.com/[a-z]*/[-a-z]*",
                      "getwuxia https://www.wuxiaworld.com/novel/renegade-immortal/rge-chapter-1300 6")
    print(match.group().split('/')[-1])
