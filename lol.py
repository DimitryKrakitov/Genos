import fenixedu


config = fenixedu.FenixEduConfiguration.fromConfigFile('fenixedu.ini')

client = fenixedu.FenixEduClient(config)

url = client.get_authentication_url()

print(url)
#degrees = client.get_degrees()

#print(degrees)