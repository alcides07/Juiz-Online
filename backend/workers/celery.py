from celery import Celery


app = Celery("workers", include=['workers.correcaoProblema'])
app.config_from_object('workers.celeryconfig')

if __name__ == '__main__':
    app.start()
