import multiprocessing
from discord.ext import commands
from Ranknir.ranknir import run_ranknir
from Dadabase.dadabase import run_dadabase

if __name__ == '__main__':

    # Create processes for each bot
    p1 = multiprocessing.Process(target=run_ranknir)
    p2 = multiprocessing.Process(target=run_dadabase)

    # Start the processes
    p1.start()
    p2.start()

    # Wait for the processes to finish
    p1.join()
    p2.join()
