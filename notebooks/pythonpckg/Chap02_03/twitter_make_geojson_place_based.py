# Chap02-03/twitter_make_geojson.py
import json
from argparse import ArgumentParser
import pickle


def get_parser():
    parser = ArgumentParser()
    parser.add_argument('--tweets')
    parser.add_argument('--geojson')
    return parser


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()
    # Read tweet collection and build geo data structure
    with open(args.tweets, 'r') as f:
        geo_data = {
            "type": "FeatureCollection",
            "features": []
        }
        for line in f:
            tweet = json.loads(line)
            try:
                if tweet['place']:
                    geo_json_feature = {
                        "type": "Feature",
                        "geometry": {
                            "type": "Point",
                            "coordinates": tweet['place']['bounding_box']['coordinates'][0][0]
                        },
                        "properties": {
                            "text": tweet['text'].encode('utf-8').replace('\n', ' ').replace('\r', ''),
                            "created_at": tweet['created_at']
                        }
                    }
                    geo_data['features'].append(geo_json_feature)
            except KeyError:
                # Skip if json doc is not a tweet (errors, etc.)
                continue
     
    # Save geo data
    output = open(args.geojson, 'w')
    pickle.dump(geo_data,output)
    output.close()
