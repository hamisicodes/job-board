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