import random
from dure_woorden_lijst import eerste_dure_woorden


def job():
    chosen_word = random.choice(eerste_dure_woorden)
    print(chosen_word)
    eerste_dure_woorden.remove(chosen_word)


job()

from notify_run import Notify

notify = Notify()
notify.send('any message you want')