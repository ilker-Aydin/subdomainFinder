import requests

target_input = input("enter your target website: ")

with open("subdomainlist.txt","r") as subdomain_list:
    for word in subdomain_list:
        word=word.strip()#bosluklardan kurtulabilmesi için
        print(word)
        url="http://" + word + "." + target_input
        try:
            response=requests.get(url)
            print(f"{url} found subdomain")
        except:
            print(f"{word} is not finded")
