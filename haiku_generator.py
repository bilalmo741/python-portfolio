# haiku_generator.py
# Python project: generate predictive Haikus using the Datamuse API

import requests, json

print("Hello, welcome to the predictive text Haiku generator!")

another = "yes"
while another == "yes":
    word = input("What would you like to see a Haiku about? ").lower()

    # Get words related to the topic
    base_url = "https://api.datamuse.com/words?md=s&rel_trg="
    full_url = base_url + word
    response = requests.get(full_url)
    data = response.json()

    if response:
        # First line
        for item in data:
            if item["numSyllables"] == 3:
                first_word = item["word"]
                break
        for item in data:
            if item["numSyllables"] == 2:
                second_word = item["word"]
                break

        # Second line
        full_url2 = f"https://api.datamuse.com/words?md=s&sp=*&lc={second_word}"
        response2 = requests.get(full_url2)
        data2 = response2.json()
        for item2 in data2:
            if item2["numSyllables"] == 3:
                third_word = item2["word"]
                break

        full_url3 = f"https://api.datamuse.com/words?md=s&sp=*&lc={third_word}"
        response3 = requests.get(full_url3)
        data3 = response3.json()
        for item3 in data3:
            if item3["numSyllables"] == 2:
                second_line2 = item3["word"]
                break

        # Rhyme for second line
        rhyme_url1 = f"https://api.datamuse.com/words?md=s&sp=*&lc={second_line2}&rel_rhy={second_word}"
        response4 = requests.get(rhyme_url1)
        data4 = response4.json()
        for item4 in data4:
            if item4["numSyllables"] == 2:
                second_line3 = item4["word"]
                break

        # Third line
        full_url4 = f"https://api.datamuse.com/words?md=s&sp=*&lc={second_line3}"
        response5 = requests.get(full_url4)
        data5 = response5.json()
        for item5 in data5:
            if item5["numSyllables"] == 3:
                third_line1 = item5["word"]
                break

        # Rhyme for third line
        rhyme_url2 = f"https://api.datamuse.com/words?md=s&sp=*&lc={third_line1}&rel_rhy={second_line3}"
        response6 = requests.get(rhyme_url2)
        data6 = response6.json()
        for item6 in data6:
            if item6["numSyllables"] == 2:
                third_line2 = item6["word"]
                break

        # Display Haiku
        print(first_word, second_word)
        print(third_word, second_line2, second_line3)
        print(third_line1, third_line2)

        another = input("Would you like to see another Haiku (yes/no)? ").lower()
    else:
        print("Error connecting to Datamuse API.")
        break
