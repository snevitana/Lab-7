import requests


#  constants
URL = "https://holidayapi.com/v1/holidays?"
API_KEY = ""  # enter your api-key


def get_information(day: int, month: int, year: int) -> dict:
    """"GETTING INFORMATION ABOUT HOLIDAYS IN ENTER DATE"""
    result_dict = dict()
    #  getting response
    resp = requests.get(url=URL,
                        params={
                            "key": API_KEY,
                            "year": year,
                            "month": month,
                            "day": day,
                            "country": "Ru"
                        })
    #  getting JSON
    got_dict = resp.json()
    if "error" in got_dict.keys():
        #  invalid date
        return got_dict["error"].split(". ")[0] + ". Try again."
    elif bool(got_dict["holidays"]):
        #  creating result
        result_dict["Country"] = "Russia"
        result_dict["Name of holidays"] = list(map(lambda x: x["name"],
                                       got_dict["holidays"]))
        result_dict["Date"] = got_dict["holidays"][0]["date"]
        result_dict["Weekday"] = (
            got_dict)["holidays"][0]["weekday"]["date"]["name"]
        return result_dict
    else:
        # if not found information about entered day
        return "Not information about holidays in this day"


def main():
    while True:
        try:
            date = input("Enter your date in format DD:MM:YYYY.\n")
            day, month, year = list(map(int, date.split(":")))
            inform = get_information(day, month, year)
            if type(inform) is dict:
                print("Information about this date:")
                for key in inform.keys():
                    if type(inform[key]) is not list:
                        print(f"{key.capitalize()}: {inform[key]}")
                    else:
                        #  for list of holidays
                        print(f"{key.capitalize()}: {", ".join(inform[key])}")
            else:
                print(inform)
        except ValueError as e:
            #  invalid enter
            print("Error!")


if __name__ == "__main__":
    main()
