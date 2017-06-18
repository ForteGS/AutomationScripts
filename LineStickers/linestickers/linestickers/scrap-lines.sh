#!/bin/bash
scrapy crawl line-sticker-cover-spider -a start_url=$1
python3 scaleimg.py


