import requests
from bs4 import BeautifulSoup
r = requests.get("http://www.hindustanuniv.ac.in/")
data = r.text
soup = BeautifulSoup(data, "lxml")
c=0
for link in soup.find_all('img'):

    image = link.get("src")
    if(image[0:4]!="http"):
        # print(image[0:3])
        image = "https://hindustanuniv.ac.in/" + image
        print(image)
    else:
        print(image)
    # img_data = requests.get(image).content
    # fileName = image[-9:-4]
    # output = open(fileName, 'wb')
    # output.write(img_data)
    # output.close()

    c+=1
    # print('file_name'+str(c)+'.jpg')

    img_data = requests.get(image).content
    with open('./images/'+'file_name'+str(c)+'.jpg', 'wb') as handler:
        handler.write(img_data)
        handler.close()
    # fileName = image[-9:-4]
    # fileName=fileName+'.jpg'

    # print(fileName)
    # with open(fileName, 'wb') as handler:
    #     handler.write(img_data)
    # req = urllib.request.Request(image)
    # resp = urllib.request.urlopen(req)
    # respData = resp.read()
    # print(respData)