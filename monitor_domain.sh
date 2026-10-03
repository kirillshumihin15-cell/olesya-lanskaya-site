#!/bin/bash
echo "Monitoring lanskaya.pro..."
for i in {1..120}; do
    HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" -L https://lanskaya.pro || echo "000")
    if [ "$HTTP_CODE" = "200" ]; then
        echo "SUCCESS: Domain is live!"
        exit 0
    fi
    sleep 60
done
echo "TIMEOUT: Domain not live after 2 hours."
exit 1
