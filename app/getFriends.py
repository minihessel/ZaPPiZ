#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------
# Name:        main.py
# Purpose:     Main file to create the Facebook graphml file outlined below.
#
# Author:      Andre Wiggins
#
# Created:     03/01/2011
# Copyright:   (c) Andre Wiggins 2011
# License:
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#-------------------------------------------------------------------------------

"""Facebook Friend Graph

This module has the user login into Facebook to get his or her access token (as
defined in the module accesstoken.py) and uses that access token to graph the
friends of the user and the connections between them.

Usage:
    $python main.py
        No command line arguments. This module gets the users access_token
        (as defined in accesstoken.py) by using the Friends Graph
        (a Facebook App) App ID. Then uses fb_friend_graph.py to graph the users
        friends and the friendships between them.
"""

import traceback

from accesstoken import get_access_token
from fb_friend_graph import graph_mutual_friends


def main():
    app_id = 183750651654082
    try:
        print "Opening Facebook. Please login to Facebook."
        #access_token = get_access_token(app_id)
        access_token = "CAACEdEose0cBAF7ZBMbOyTrBK7ejLlZALjSzvGz5zF4c2nGxyLk6lrMq2TwUs3C6i9LP60aoVSVsTZA2wJZCTONsjvUBmqgJZCPhUxZBeoyFYmf3etZA1TrNrU6ZBDriLZCTZAyBlmq74ZAGZBX3uJSSbHpmGvkCUXjeENgZCy5yIsuom1JfGneuJSM6K9eVRSHp7uTJwVeXTUkDz1wZDZD"
    except:
        traceback.print_exc()
    else:
        return graph_mutual_friends(access_token)




if __name__ == '__main__':
    main()
