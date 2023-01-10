
git init

touch README.md

echo "This repo was created remotely" >> README.md

git add .

git commit -m "first commit"

git remote add origin git@github.com:USER/test.git

curl -u 'USER:TOKEN' https://api.github.com/user/repos -d '{"name":"test"}'

git push -u origin master
