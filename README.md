npm init -y

serverless plugin install -n serverless-plugin-simulate
serverless plugin install -n serverless-python-requirements

npm install request --save

sls simulate lambda -p 4000

sls simulate apigateway -p 5000 --lambda-port 4000