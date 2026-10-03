#!/usr/bin/expect
spawn npx --yes surge ./dist olesya-lanskaya.surge.sh
expect "email:"
send "znoirewgmail.com@gmail.com\r"
expect "password:"
send "TempPassword123!\r"
expect eof
