1. Install python
https://www.python.org/downloads/
2. Install mongodb community server
https://www.mongodb.com/try/download/community
3. Install mongodb compass
https://www.mongodb.com/try/download/compass
create a database named "local" and a collection named "invoice"
4. Install Pycharm
https://www.jetbrains.com/pycharm/download/#section=windows
5. Download and install git bash
https://git-scm.com/downloads
6. Create a git repository in your github account
7. You can clone the created git repo using below git bash command in your local computer in some folder where you want to write code
git clone https://github.com/preudh/P13_fastapi-mongodb-facturx.git
**Make sure to use your git repository
7. Open the local source code folder in Pycharm from open File->Open
8. Open terminal in pycharm and install below packages by running below command
pip install pymongo fastapi uvicorn
9. Create folder pdf_extract used to get pdf files save in binary mode in mongodb and load in it when using get method by id
10. for example purpose when you use post method , I created a sample_facturx folder with hybrid invoices inside (pdf and xml)
10. Create main.py at root of project
11. Write code in main.py for creating a FastAPI app
12. Go to terminal and run below command to run server in auto-relaod mode
uvicorn index:app --reload
13. Go to browser and hit below url to access the default FastAPI swagger page
http://127.0.0.1:8000/docs
14. Using this swagger doc page we will test our all REST api endpoints, you can also use Postman to test your api endpoints
15. Create database.py file inside and write code for DB connection
16. Create model.py, crud.py, model.pys files
17. Create invoice model inside model.py with the help of pydantic BaseModel and add the fields
18. Create methods and route in your crud.py to get/post/delete/update invoices
19. Make sure to register the invoice_router to the FastAPI app inside main.py file
20. Go to the browser and refresh below url, you will see your new endpoint
http://127.0.0.1:8000/docs
21. Test your endpoints using swagger doc page
22. Test all REST API endpoints through swagger url
23. Git commit and push your code to github using below steps
git add .
git commit -m "first commit"
git remote set-url origin https://<YOUR_GITHUB_USERNAME>:<YOUR_GITHUB_PERSONAL_TOKEN>@github.com/<YOUR_GITHUB_USERNAME>/fastapi-mongodb-crudapp.git
git push
