REM Set project name
set PROJECT_NAME=tweets-analyzer
set APP_NAME=tweets-analyzer-app


echo.
echo Cleaning up existing resources...
oc delete route %APP_NAME% 2>nul
oc delete svc %APP_NAME% 2>nul
oc delete deployment %APP_NAME% 2>nul
echo Cleanup completed.

echo.
echo Building and deploying application...
docker build -t hostile-tweets-analyzer-app .
docker push benjypfeffer/hostile-tweets-analyzer-app:latest

oc apply -f infrastructure/k8s/tweets-analyzer-secret.yaml
oc apply -f infrastructure/k8s/tweets-analyzer-deployment.yaml
oc apply -f infrastructure/k8s/tweets-analyzer-service.yaml
oc apply -f infrastructure/k8s/tweets-analyzer-route.yaml
