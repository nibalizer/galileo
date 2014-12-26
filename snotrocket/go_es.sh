


# search on all the tweets that match the followers of user 2
#curl -XGET localhost:9200/tweets/_search -d '{
#  "query" : {
#    "filtered" : {
#      "filter" : {
#        "terms" : {
#          "user" : {
#            "index" : "users",
#            "type" : "user",
#            "id" : "2",
#            "path" : "followers"
#          },
#          "_cache_key" : "user_2_friends"
#        }
#      }
#    }
#  }
#}'

curl -XGET localhost:9200/snotrocket/_search -d '{
{
    "query": {
        "term": {
            "status": "open"
        }
    }
}'

