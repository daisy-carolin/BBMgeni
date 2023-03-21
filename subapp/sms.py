import africastalking

# Initialize Africa's Talking

africastalking.initialize(
    username='sandbox',
    api_key='751e1366adacd9a457f90d653daa7b9109206209aefc23cb70a2d30907972063'
)

sms = africastalking.SMS


class SendSMS:
    def send(self, name, phone_number, invite_code, meeting_date, meeting_time):
        recipients = [f"+{phone_number}"]
        # Set your message
        message = f"Hey  {name}\n " \
                  f"Your invite code is  {invite_code}. \n" \
                  f"Meeting Date: {meeting_date} \n"\
                  f"Meeting Time: {meeting_time}"
        # Set your shortCode or senderId
        sender = "9577"
        try:
            response = sms.send(message, recipients, sender)
            print(response)
        except Exception as e:
            print(f'Houston, we have a problem: {e}')