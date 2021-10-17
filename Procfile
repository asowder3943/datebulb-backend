release: DATABASE_URL="postgres://jfszgnebumrwzd:2f62ab9e5a12f40c3f84c0cbb5489a554ed205da77d25dcb99e7a6af191faf80@ec2-3-226-165-74.compute-1.amazonaws.com:5432/d9bmr3u3t3atuu" python manage.py test --keepdb
release: python manage.py migrate

web: gunicorn datebulb.wsgi
