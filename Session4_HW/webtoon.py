def extract_info(webtoon_list):
    result = []

    for webtoon in webtoon_list:
        title = webtoon.find("dt").find("a").text
        name = webtoon.find("dd", {"class":"desc"}).find("a").text
        rate = webtoon.find("div", {"class":"rating_type"}).find("strong").text

        webtoon_info = {
            'title' : title,
            'name' : name,
            'rate' : rate,
        }

        result.append(webtoon_info)

    return result