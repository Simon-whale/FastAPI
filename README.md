# FastAPI
Used to look into Python Fast API and explore Python's framework

Project will expand to include - this is a learning project

* Sentry
* **__ init __.py** namespace packages - Added 14th May
* **routing** - in now all controllers (sorry C# term) are stored in seperate files and joined to the app via routing in the __init__ file
* **dependency** - this is now in and working it gives the ability to add common parameters by particular routing class
* **testing** - Added 14th May
* **docker & requirements scripting**
  
  This has now been added, to build the image from the root of this project folder type the following
  
  **docker-compose build** - this will build a copy of the image on the local machine
  
  **docker-compose up** - this will install the image on the docker engine that has been installed on the local machine
  
  **docker logs simonsproject_web** - this will show the logs that will if any contains messages or errors while deploying the image to docker
* **Error Handling** have addeded via a error route the ability for it too raise a 404 error because the id value is greater than 100