import threading
from .agents import ElasticAgent, PostgresAgent

def simulate_elastic(replicas: int = 1):
    threads = []
    # start all threads
    for i in range(replicas):
        print('Started agent thread')
        new = threading.Thread(target=ElasticAgent().run, args=())
        new.start()
        threads.append(new)

    # catch them all
    for thread in threads:
        thread.join()
    print('All done')

def simulate_postgres(replicas: int = 1):
    threads = []
    # start all threads
    for i in range(replicas):
        print('Started agent thread')
        new = threading.Thread(target=PostgresAgent().run, args=())
        new.start()
        threads.append(new)

    # catch them all
    for thread in threads:
        thread.join()
    print('All done')