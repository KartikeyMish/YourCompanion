import os
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import io
from io import BytesIO
import pandas as pd
from google.cloud import storage
import os
from twilio.rest import Client

# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'client_secret_626866517991-brc9utto6mpet418gcdfedatl42pmu9p.apps.googleusercontent.com.json' 

class gcp:
    
    @classmethod
    def record(cls): # Recording Audio if there is distress call
        # Sampling frequency
        freq = 44100
        # Recording duration in seconds
        duration = 10
        # Start recorder with the given values
        # of duration and sample frequency
        print("Recording your voice for next 10 seconds.....")
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

    @classmethod
    def upload(cls):
        # Replace with your project and bucket names
        project_id = 'sturdy-tine-397320'
        bucket_name = 'personablend'

        # Create a client to interact with GCS
        storage_client = storage.Client.from_service_account_json('googlestruct.json')
        # client = storage.Client(project=project_id)

        # Get the bucket
        bucket = storage_client.get_bucket(bucket_name)

        # Specify the object's name in the bucket
        object_name = 'recording.wav'

        # Path to the local file you want to upload
        local_file_path = 'textbase/distress_audio/recording.wav'

        # Upload the file to the bucket
        blob = bucket.blob(object_name)
        blob.upload_from_filename(local_file_path)

        print(f"File {local_file_path} uploaded to https://storage.googleapis.com/{bucket_name}/{object_name}")
        return f"https://storage.googleapis.com/{bucket_name}/{object_name}"


class Twilio:
    account_sid = None
    auth_token = None
    phonenumber =None
    trasncript_sid= None
    msgServiceSid = None

    @classmethod
    def transcribe(
        cls, 
        link:str,
    ):
        try:
            client = Client(cls.account_sid, cls.auth_token)

            transcript = client.intelligence \
                            .v2 \
                            .transcripts \
                            .create(
                                    service_sid=str(cls.trasncript_sid),
                                    channel={}
                                )
            print(transcript.sid)
        except:
            print("audio transcibed to text")

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
            print("Message Sent Authority Sucessfully")
        except Exception as e:
            print("Message not sent due to :",e)
