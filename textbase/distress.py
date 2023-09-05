import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
from twilio.rest import Client

class audio:
    
    @classmethod
    def record(cls): # Recording Audio if there is distress call
        # Sampling frequency
        freq = 44100
        # Recording duration in seconds
        duration = 15
        
        print("Recording your voice for next 15 seconds.....")
        # Start recorder with the given values of duration and sample frequency
        recording = sd.rec(int(duration * freq),
                        samplerate=freq, channels=2) 
        # Record audio for the given number of seconds
        sd.wait()
        # This will convert the NumPy array to an audio
        # file with the given sampling frequency
        write("textbase/distress_audio/recording0.wav", freq, recording)
        # Convert the NumPy array to audio file
        wv.write("textbase/distress_audio/recording.wav", recording, freq, sampwidth=2)
        print("Audio recording saved")
        return("textbase/distress_audio/recording.wav")

class Twilio:
    account_sid = None
    auth_token = None
    phonenumber =None
    msgServiceSid = None

    @classmethod
    def sendsms(
        cls,
        details: str,
    ):
        try:
            print("Sending Message to authorites........")
            client = Client(cls.account_sid, cls.auth_token)
            message = client.messages.create(
                from_='whatsapp:'+cls.phonenumber,
                messaging_service_sid=cls.msgServiceSid,
                body=details,
                to='whatsapp:+919369244056'
            )
            print(client)
            print("Message Sent to Authority Sucessfully")
        except Exception as e:
            print("Message not sent due to :",e)
