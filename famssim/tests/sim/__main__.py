import sys
from famssim.tests.sim.runner import run


if __name__ == '__main__':
    if 'crate' not in sys.argv and 'timescale' not in sys.argv:
        print('''
        Unknown or missing environment. 
        Usage: python famssim <env> (env: crate|timescale)
        ''')
        exit(1)

    run(sys.argv[1])
