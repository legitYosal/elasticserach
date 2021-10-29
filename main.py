import fire
from agents import cli

def simulate(agent: str, replicas: int = 1):
    """
        client tool for simulating high load
    """
    if agent == 'elastic':
        cli.simulate_elastic(replicas)
    elif agent == 'postgres':
        cli.simulate_postgres(replicas)
    else: 
        print('Not a valid option')


if __name__ == '__main__':
    fire.Fire(simulate)