import requests
from twilio_conn import send_whatsapp_text,client

def get_quote_of_the_day(category):
  """
    Gets a QOD from Rest API by Category
  """
  url = "https://api.quotable.io/random"
  res = requests.get(url=url)
  data = res.json()
  status = res.status_code
  match status:
    case 200:
      quote = data['content']
    case 400:
      quote = data['error']
    case _:
      quote = "Sorry"
  return quote
  
  
quote = get_quote_of_the_day(category="inspire")
send_whatsapp_text(client,quote)