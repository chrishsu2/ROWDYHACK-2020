# -*- coding: utf-8 -*-
# @Author: Christopher Hsu
# @Date:   2020-03-28 18:14:12
# @Last Modified by:   Christopher Hsu
# @Last Modified time: 2020-03-28 19:45:14

import json, falcon


api = falcon.API()


class SearchRequestClass:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200  # may change to 202 depending on wait times
        # If Content-Length happens to be 0, or the header is
        # missing altogether, this will not block.
        data = req.stream.read(req.content_length or 0)  # dictionary
        # {query: '%SEARCHQUERY%', 'grocery chain': '%WALMART or TARGET%', 'store': '%SPECIFIC STORE%'}
        content = {
            'request type' : 'GET',
            #  Placeholder dummy results
            'results':
                [{'name': 'dummyname0', 'image url': "https://i.imgur.com/C8Yjy1T.jpg", 'stock': '0'},
                {'name': 'dummyname1', 'image url': "https://i.imgur.com/C8Yjy1T.jpg", 'stock': '10'},
                {'name': 'dummyname2', 'image url': "https://i.imgur.com/C8Yjy1T.jpg", 'stock': '-1'},   # -1 means unavailable
                {'name': 'dummyname3', 'image url': "https://i.imgur.com/C8Yjy1T.jpg", 'stock': '99'},
                {'name': 'dummyname4', 'image url': "https://i.imgur.com/C8Yjy1T.jpg", 'stock': '2'}]
        }
        resp.body = json.dumps(content)

    def on_post(self, req, resp):
        resp.status = falcon.HTTP_201  # may change to 202 depending on wait times
        content = {
            'post' : 'dummy result'
        }
        resp.body = json.dumps(content)

    def on_patch(self, req, resp):
        resp.status = falcon.HTTP_200
        content = {
            'patch' : 'dummy result'
        }
        resp.body = json.dumps(content)

    def on_delete(self, req, resp):
        resp.status = falcon.HTTP_200
        content = {
            'delete' : 'dummy result'
        }
        resp.body = json.dumps(content)



api.add_route('/api', SearchRequestClass())
