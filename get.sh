echo $1

# curl -i -H "Content-Type: application/json" -X POST -d '{"url":"https://www.bbc.co.uk/news/uk-politics-50275383"}' http://localhost:5000/url
# curl -i -H "Content-Type: application/json" -X POST -d '{"url":"$1"}' http://localhost:5000/url

curl http://localhost:5000/url/$1
