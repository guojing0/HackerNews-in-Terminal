import requests


def main():
    top_stories_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
    top_stories_json = requests.get(top_stories_url).json()

    story_base_url = "https://hacker-news.firebaseio.com/v0/item/"

    num = 1

    for story_id in top_stories_json[:60]:
        story_request = requests.get(story_base_url + str(story_id) + ".json")
        story_json = story_request.json()
        formatted_text = "{}. {} (score: {}, {})".format(num, story_json["title"], story_json["score"], story_id)

        try:
            story_url = story_json["url"]
        except KeyError:
            story_url = "https://news.ycombinator.com/item?id=" + str(story_id)

        if len(formatted_text + story_url) <= 180:
            formatted_text += ": " + story_url
        else:
            formatted_text += "\n" + story_url

        print(formatted_text + "\n")

        num += 1


if __name__ == '__main__':
    main()
