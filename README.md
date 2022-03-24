
Test task


Steps:

git clone https://github.com/mnjl1/blog-test-task.git

cd blog-test-task

docker-compose up -d --build

docker-compose exec web makemigrations

docker-compose exec web migrate

docker-compose exec web python manage.py createsuperuser

After that you can go to admin panel to populate users and basic data