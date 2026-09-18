bind = "unix:/var/www/modiran-backend/modiran-backend/gunicorn.sock"

workers = 3

timeout = 120

wsgi_app = "modiran_project.wsgi:application"
