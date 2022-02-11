from urllib import response
import requests
import os

#credentials here
username = "aaxim123"
password = "User@#$%1234"
#get access_token #basic authroization or connection validation to url shortening website(here bitly)
auth_res = requests.post("https://api-ssl.bitly.com/oauth/access_token", auth=(username, password))
if auth_res.status_code ==200:
    access_token = auth_res.content.decode()
    print("Access token recieved: ", access_token)
else:
    print("couldn't recieve access token \t exiting")
    exit()

#Once authorization is complete we can begin the shortening process by requesting the url from the user and sending back the shortened url

#request long url
long_url = input("Enter the url: ")

headers = {
    "Authorization": f"Bearer {access_token}"
    }
    
#get the group uid associated with the account(required by bitly)
group_res = requests.get("https://api-ssl.bitly.com/v4/groups", headers=headers)
if group_res.status_code ==200:
    #if response is ok get the uid
    groups_data = group_res.json()['groups'][0]
    guid = groups_data['guid']

else:
    print("**Cannot get GUID**, \t exiting...")
    exit()

#paramater to be passed with our post request
data= {"long_url": long_url, "domain":"bit.ly","group_guid":guid }

#Create our post request
response =  requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, json=data)

#get the shortened url from the response object
short_url = response.json().get('link')

#print the shortened url to console
print(f"your shortened link is: {response.json().get('link')}")

#store the long url with its shortened version in a database, here the csv file

f = open('urls.csv', 'a')
f.write(f"{long_url},{short_url}\n")
f.close