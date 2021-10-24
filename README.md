#### News board - PS: (A wrong name ~~`job board`~~ is mistakenly used instead of `News Board`) - Will migrate it it into another repository soon for readablity

#### Set up
1. clone this repository 
1. Head into the projects folder
1. Activate a virtual environment for your project and environment variables specified in `local.env` file
 - You will need to configure your local database and specify the values in .env file
 - Ensure you also have RabbitMQ server running locally (You can install it on your machine or use [docker](https://hub.docker.com/_/rabbitmq))
1. Install all dependencies/extensions in the requirments.txt file
1. Run app

```
$git clone https://github.com/hamisicodes/job-board.git
$cd job-board
$python3 -m venv <name_of_your_virtual_environment> eg: $python3 -m venv venv
$pip install -r requirments.txt
$python manage.py runserver

```

###  Production
Import this public collection link https://www.getpostman.com/collections/035a692b97fbd7eb7bf5 on postman to view the APIs
set Variables:
- PROD: 'https://job-board-1.herokuapp.com`
- LOCAL: 'http://127.0.0.1:8000' (Incase your running this locally)
- name: `<Your preffered username>`
- email: `<Your preffered email address>`
- password: `<Your preffered password>`

...and voila start your signup process into the API , then sign in(using the sign in endpoint).
__`N|B`__:- Once your signed in, the token will be saved into a `cookie` and therefore you can successfully make requests to the endpoints as an `authenticated user` .If `cookie` is not available(Not signed in, requests to other endpoints will fail)

### API Docs
- Find the url for the published API doc https://documenter.getpostman.com/view/11614732/UV5ahGSZ

