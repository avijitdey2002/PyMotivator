from apscheduler.schedulers.background import BackgroundScheduler
from motivator import send_whatsapp_text,client,quote
import time
scheduler = BackgroundScheduler(timezone="Asia/Kolkata")
scheduler.start()

job = scheduler.add_job(send_whatsapp_text,'cron',[client,quote],hour="13",minute="51")
while True:
  time.sleep(1)
