import boto3
from camera import captureImg
client=boto3.client('rekognition')
def reko():
    image = captureImg()
    response = client.detect_labels(Image={'Bytes': image.read()})
    print('Detected labels in this image :')
    #for label in response['Labels']:
    #    print (label['Name'] + ' : ' + str(label['Confidence']))
    print(response)
    print('Done...')
    return response

