#countries in africa
import time
countries = ['Algeria', 'Angola', 'Benin', 'Botswana', 'Burkina Faso', 'Burundi', 'Cabo Verde', 'Cameroon', 'Central African Republic', 'Chad', 'Comoros', 'Ivory Coast', 'Djibouti', 'Democratic Republic Of The Congo', 'Egypt', 'Equatorial Guinea', 'Eritrea', 'Eswatini', 'Ethiopia', 'Gabon', 'Gambia', 'Ghana', 'Guinea', 'Guinea-Bissau', 'Kenya', 'Lesotho', 'Liberia', 'Libya', 'Madagascar', 'Malawi', 'Mali', 'Mauritania', 'Mauritius', 'Morocco', 'Mozambique', 'Namibia', 'Niger', 'Nigeria', 'Republic Of The Congo', 'Rwanda', 'Sao Tome And Principe', 'Senegal', 'Seychelles', 'Sierra Leone', 'Somalia', 'South Africa', 'South Sudan', 'Sudan', 'Tanzania', 'Togo', 'Tunisia', 'Uganda', 'Zambia', 'Zimbabwe' ]
print("--- Countries of Africa ---")
score = 0
lives = 3
print(f"You have {lives} live(s)")
while len(countries) >0:
    if lives == 0:
        break
    print("Number of countries to guess:",len(countries))
    time.sleep(0.5)
    print("Score: ",score)
    time.sleep(0.5)
    country = str(input("Enter the name of a country: "))
    country = country.lower()
    country = country.title()
    if country in countries:
        print("Good Guess")
        score +=1
        countries.remove(country)
        time.sleep(0.75)
    else:
        lives -=1
        print("Invalid Guess")
        time.sleep(0.75)
        print(f"You have {lives} live(s) remaining")
        time.sleep(0.75)
if len(countries) == 0:
    print("You Win!")
    print("You know all the countries in Africa!")
if lives == 0:
    print("You lost the game")
    print("You missed these countries")
    time.sleep(1.5)
    print(*countries, sep="\n")
