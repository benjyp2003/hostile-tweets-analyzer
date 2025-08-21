@echo off
echo Building Docker image...
docker build -t iran-tweets-analyzer .

if %ERRORLEVEL% neq 0 (
    echo Failed to build Docker image
    pause
    exit /b 1
)

echo.
echo Stopping any existing container...
docker stop iran-tweets-analyzer-container 2>nul
docker rm iran-tweets-analyzer-container 2>nul

echo.
echo Running Docker container...
docker run -d ^
    --name iran-tweets-analyzer-container ^
    -p 8000:8000 ^
    iran-tweets-analyzer

if %ERRORLEVEL% neq 0 (
    echo Failed to run Docker container
    pause
    exit /b 1
)

echo.
echo Container is running!
echo API is available at: http://localhost:8000
echo.
echo To view logs: docker logs iran-tweets-analyzer-container
echo To stop container: docker stop iran-tweets-analyzer-container
echo.
pause