import requests
def converter():
    initial=input("Enter initital currency: ")
    target=input("Enter target currency: ")

    while True:
        try:
            amount=float(input("Enter amount: "))
        except:
            print("The amount need to be numeric: ")

        if amount < 0:
            print("Enter a valid amount: ")
            continue
        else:
            break

    url = f"https://api.apilayer.com/fixer/convert?to={target}&from={initial}&amount={amount}"

    payload = {}
    header = {
        "apikey": "API-KEY"
    }
    response = requests.request("GET", url, headers=header, data=payload)
    status_code = response.status_code

    if status_code != 200:
        result=response.json()
        print("Error response" + str(result))
        quit()

    result=response.json()
    print("Conversion Result: "+str(result['result']))


if __name__=="__main__":
    converter()