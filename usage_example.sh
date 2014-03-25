#!/usr/bin/env sh

if [ -z $1 ]; then
    # set default host
    host="127.0.0.1:5000"
else
    host=$1
fi

echo
echo == GET \(initial state\) ==========================================
echo

curl $host/article   --header 'Accept: application/json'
curl $host/article/1 --header 'Accept: application/json'
curl $host/article/2 --header 'Accept: application/json'
curl $host/article/3 --header 'Accept: application/json'
curl $host/article/4 --header 'Accept: application/json'
curl $host/article/5 --header 'Accept: application/json'

echo
echo == DELETE article 1 ===============================================
echo

curl $host/article/1 --header 'Accept: application/json' --request DELETE
curl $host/article   --header 'Accept: application/json'

echo
echo == POST an article ================================================
echo

curl $host/article \
    --header 'Accept: application/json' \
    --header 'Content-type: application/json' \
    --request POST \
    --data '"test article for POST interface"' \
    # --verbose

curl $host/article   --header 'Accept: application/json'
