all: locations.json

raw.json:
	wget -O $@ 'https://opendata.socrata.com/resource/xy4y-c4mk.json?$$limit=50000'

locations.json: raw.json filter.py
	python filter.py < raw.json > $@
