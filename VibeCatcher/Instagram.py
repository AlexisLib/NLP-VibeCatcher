import os
import requests
from ast import literal_eval
import json
import spacy
from spacy_langdetect import LanguageDetector
import pandas as pd
import time


def get_text_from_json(json_t, first_key, nlp, langue):
    edges = json_t[first_key]["hashtag"]["edge_hashtag_to_media"]["edges"]
    caption_of_tag = []

    for edge in edges:
        nodes = list()
        nodes.append(edge["node"]["edge_media_to_caption"]["edges"])
        for node in nodes:
            for i in node:
                txt = i["node"]["text"]
                lang = nlp(txt)
                if lang._.language['language'] == langue:
                    caption_of_tag.append({'tweet': txt})

    return caption_of_tag


def get_page_info(json_t, first_key):
    return json_t[first_key]["hashtag"]["edge_hashtag_to_media"]['page_info']


def get_hash_tag_caption(name_of_hashtags: str, number: int, save_path, langue):
    pathcheck = 'dataset_instagram/' + langue
    path = 'dataset_instagram/' + langue + '/' + str(name_of_hashtags)

    # Check if folder already exist (yes : continue / no : create folder)
    if not os.path.exists(pathcheck):
        os.makedirs(pathcheck)
    if not os.path.exists(path):
        os.makedirs(path)

    with open('config.json') as json_file:
        configure = json.load(json_file)

    user_agent = configure['user_agent']
    cokkies = configure['cokkies']
    query_hash = configure['query_hash']

    s = requests.session()
    s.headers.update(user_agent)
    s.cookies.update(cokkies)
    request = s.get(f"https://www.instagram.com/explore/tags/{name_of_hashtags}/?__a=1")

    assert request.status_code == 200, "problem of request"

    if langue == "en":
        nlp = spacy.load("en_core_web_sm")
    elif langue == "fr":
        nlp = spacy.load('fr_core_news_sm')
    else:
        assert False, "arg langue required 'en' or 'fr'"
    nlp.add_pipe(LanguageDetector(), name='language_detector', last=True)

    content = request.content

    try:
        content_json = json.loads(content)
    except json.decoder.JSONDecodeError:
        print("unknown request error")
        return

    page_info = get_page_info(content_json, "graphql")

    posts = get_text_from_json(content_json, "graphql", nlp, langue)
    nb_posts = len(posts)

    while page_info["has_next_page"] and nb_posts <= number:

        first = 1000
        request_url = f"https://www.instagram.com/graphql/query/?" \
                      f"query_hash={query_hash}" \
                      f"&variables=%7B" \
                      f"%22tag_name%22%3A%22{name_of_hashtags}%22%2C" \
                      f"%22first%22%3A{first}%2C" \
                      f"%22after%22%3A%22{page_info['end_cursor']}%22%7D"

        request = s.get(request_url)

        if request.status_code != 200:
            content = request.content
            print(content)

            try:
                content_json = json.loads(content)
            except json.decoder.JSONDecodeError:
                print("unknown request error")
                pd.DataFrame(posts).to_csv(save_path)
                return

            if content_json['message'] == "rate limited":
                print('rate limit ....')
                while request.status_code != 200:
                    print("wait 1 min for retry ....")
                    time.sleep(60)
                    print("retry sent the request ....")
                    request = s.get(request_url)

        content = request.content

        try:
            content_json = json.loads(content)
        except json.decoder.JSONDecodeError:
            print("unknown request error")

        res = get_text_from_json(content_json, 'data', nlp, langue)
        page_info = get_page_info(content_json, 'data')

        posts += res
        nb_posts = len(posts)
        print(f"got {len(posts)} posts ....")

    pd.DataFrame(posts).to_csv(save_path)
    return path

