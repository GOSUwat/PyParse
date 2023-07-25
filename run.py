from threading import Thread
from apscheduler.schedulers.blocking import BlockingScheduler
import bot


scheduler = BlockingScheduler()
scheduler.add_job(bot.feedback, "interval", hours = 1) #hours minutes

def schedule_checker():
    scheduler.start()
        
 
if __name__ == "__main__":
    Thread(target=schedule_checker).start()
    
    bot.bot.polling(none_stop=True, interval=0)