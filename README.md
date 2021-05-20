## Getting started
You will need:
* [Python 3](https://www.python.org/downloads/)
* [Docker](https://docs.docker.com/engine/install/)
* [pip](https://phoenixnap.com/kb/how-to-install-pip-on-ubuntu)

Clone the repository and `cd` into the directory.

Open a shell and run `docker-compose up`  to set up all the necessary Python dependencies and project-related other dependencies.

You should be able to navigate to http://127.0.0.1:8000.

### Test cases
To run Test-Cases In a separate shell, run `docker exec -it todo_service bash` to open shell prompt. Make sure `docker-compose up` should be running in another shell. Then run `python3 manage.py test`. 

### Management Command To Perform Symmetric Encryption.
To Perform Symmetric Encryption on todo's. Use the same shell where you have run test cases or you can repeat steps mentioned for test cases. To run management command in another shell. The only difference is you have to run `python3 manage.py encrypt_todo_command` instead of `python3 manage.py test`.

### To run management command or test case with running docker container you can also take reference from [here](http://masnun.com/2016/04/23/django-running-management-commands-inside-a-docker-container.html)

### API Endpoints
* [Api Root](https://prnt.sc/1369h6p)
* [Todo List](https://prnt.sc/1369li5)
* [Category List](https://prnt.sc/1369rq4)