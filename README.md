Folder structure.
project/
├── api/
│   └── api.py
├── app/
│   └── app.py
├── requirements.txt
└── Dockerfile
        |-----Dockerfile-mainapp
        |-----Dockerfile-api

Create a file named “app.py” in there,

The main app includes a function named fetch_data() that sends a GET request to the API to fetch data.
The URL http://api:5001/api is used to access the API. The hostname "api" corresponds to the service name defined in the Docker Compose file.
If the API responds with a 200 status code, the function returns the JSON data; otherwise, it returns a failure message.
In this example, we print the fetched data, but you can modify the code to suit your requirements.

Create a file called api.py in there,

The API is a simple Flask application that defines a route for the “/api” URL and returns a JSON response.
In this example, the API returns the message “Hello from the API!” as JSON data.
You can customize the API logic and responses according to your application’s requirements.

Further, Create a file requirements.txt and put the following content in it.

The requirements.txt file lists the required packages and their versions.In this example, we include Flask version 2.3.2 for the main app and the requests library version 2.28.2 for making HTTP requests.

###########################################
###########################################

Now, let’s build and run the Docker images for both applications.

First, verify that Docker Desktop application is running if you are using windows or mac os. If not, launch it: that will run the docker daemon (just wait few minutes).
Open a terminal or command prompt and navigate to the directory containing the Dockerfile, application files, and requirements.txt.
Build the Docker image for the main app using the following command:

docker build -t myapp -f mainapp/Dockerfile.
3. Build the Docker image for the API using the following command:


docker build -t api -f api/Dockerfile.
4. Create a network so that both the containers run in same network

docker create network mynetwork
5. Run the Docker containers for both applications using the following commands:

docker run -d --name myapi_container -p 8000:8000 --network mynetwork myapi
docker run -d --name myapp_container -p 5000:5000 --network mynetwork myapp
The -p flag maps the container's ports to the host machine's ports, enabling access to the applications. Adjust the port numbers if needed.

Access the main app at http://localhost:5000/ and verify that it fetches data from the API successfully.
