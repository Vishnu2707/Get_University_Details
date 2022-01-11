import requests

url = "http://universities.hipolabs.com/search?country="

print("---------------------------------------------- Get the university details ----------------------------------------------\n")

while(True):
    s = ''
    country = input("Enter the name of the Country!!\n").lower()
    c = country[0].upper() + country[1:]
    s = url + c
    resp = requests.get(s)
    r = resp.json()

    if r == []:
        print("Enter a valid Country name!!\n")
        exit()

    press = input("\nPress 1  - State-wise or Province-wise university details!!\n\nPress Any Digit - Details of all univerities in the Country!!\n")
    #The statewise or province wise data is displayed below.
    if int(press) == 1:
        
        s = input("\nEnter the name of State or Province!!\n").lower()
        state = s[0].upper() + s[1:]

        flag = 1

        for i in range(0,len(r)):
            data = r[i]

            for key,value in data.items():
                if key == 'state-province' and value == state:
                    flag = flag + 1
                    print("\n--------------------------------------------------------------------------------------------------\n")
                    print("Name of the university - ",data['name'],"\n")
                    print("State - ",data['state-province'],"\n")
                    print("Website - ",data['web_pages'],"\n")
                    print("\n--------------------------------------------------------------------------------------------------")

        if flag == 1:
            print('\nEither the data is not available or check the name of the state')
            exit()

    #The countrywise data is displayed below.
    else:
        for i in range(0,len(r)):
            data = r[i]
            print("\n--------------------------------------------------------------------------------------------------\n")

            for key,value in data.items():
                if key == 'name':
                    print("Name of the university - ",value,"\n")
                if key == 'state-province':
                    print("State - ",value,"\n")
                if key == 'web_pages':
                    print("Website - ",value,"\n")


