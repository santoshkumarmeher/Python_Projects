import requests

parameters = {
    "amount": 10,
    "type":"boolean"
}
response = requests.get("https://opentdb.com/api.php",params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]

# question_text = data["question"]
# question_answer = data["correct_answer"]




# question_data = [
#     {
#         "category": "General Knowledge",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "Video streaming website YouTube was purchased in it&#039;s entirety by Facebook for US$1.65 billion in stock.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "category": "General Knowledge",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "&quot;Typewriter&quot; is the longest word that can be typed using only the first row on a QWERTY keyboard.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "General Knowledge",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "The US emergency hotline is 911 because of the September 11th terrorist attacks.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "category": "General Knowledge",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "French is an official language in Canada.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "General Knowledge",
#         "type": "boolean",
#         "difficulty": "hard",
#         "question": "This is the correct spelling of &quot;Supercalifragilisticexpialidocious&quot;.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "General Knowledge",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "The vapor produced by e-cigarettes is actually water.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "category": "General Knowledge",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "It is automatically considered entrapment in the United States if the police sell you illegal substances without revealing themselves.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "category": "General Knowledge",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "The sum of all the numbers on a roulette wheel is 666.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "General Knowledge",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "Furby was released in 1998.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "General Knowledge",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "Nutella is produced by the German company Ferrero.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "category": "General Knowledge",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "There are 86400 seconds in a day.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "General Knowledge",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "An eggplant is a vegetable.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "category": "General Knowledge",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "The bikini is named after the &quot;Bikini Atoll&quot;, an island where the United States conducted tests on atomic bombs.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "General Knowledge",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "Cucumbers are usually more than 90% water.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "General Knowledge",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "A scientific study on peanuts in bars found traces of over 100 unique specimens of urine.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "category": "General Knowledge",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "Bulls are attracted to the color red.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "category": "General Knowledge",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "You are allowed to sell your soul on eBay.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "category": "General Knowledge",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "&quot;Ananas&quot; is mostly used as the word for Pineapple in other languages.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "General Knowledge",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "The average woman is 5 inches / 13 centimeters shorter than the average man.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "General Knowledge",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "The Sun rises from the North.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "category": "General Knowledge",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "The color orange is named after the fruit.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "General Knowledge",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "You can legally drink alcohol while driving in Mississippi.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "General Knowledge",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "The term &quot;Spam&quot; came before the food product &quot;Spam&quot;.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "category": "General Knowledge",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "On average, at least 1 person is killed by a drunk driver in the United States every hour.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "General Knowledge",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "In 2010, Twitter and the United States Library of Congress partnered together to archive every tweet by American citizens.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "General Knowledge",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "Kissing someone for one minute burns about 2 calories.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "General Knowledge",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "The French word to travel is &quot;Travail&quot;",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "category": "General Knowledge",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "The Lego Group was founded in 1932.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "General Knowledge",
#         "type": "boolean",
#         "difficulty": "hard",
#         "question": "In Scandinavian languages, the letter &Aring; means river.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "General Knowledge",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "One of Donald Trump&#039;s 2016 Presidential Campaign promises was to build a border wall between the United States and Mexico.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "General Knowledge",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "Romanian belongs to the Romance language family, shared with French, Spanish, Portuguese and Italian. ",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "General Knowledge",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "Fast food restaurant chains Carl&#039;s Jr. and Hardee&#039;s are owned by the same company.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "General Knowledge",
#         "type": "boolean",
#         "difficulty": "hard",
#         "question": "Stagecoach owned &quot;South West Trains&quot; before losing the rights to FirstGroup and MTR in March of 2017.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "General Knowledge",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "&quot;Santa Claus&quot; is a variety of melon.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "General Knowledge",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "&quot;27 Club&quot; is a term used to refer to a list of famous actors, musicians, and artists who died at the age of 27.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "General Knowledge",
#         "type": "boolean",
#         "difficulty": "hard",
#         "question": "Spoon theory is a theory, utilizing &quot;Spoons&quot; as a metaphor for energy they can use in a day.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "General Knowledge",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "The scientific name for the Southern Lights is Aurora Australis?",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "General Knowledge",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "Haggis is traditionally ate on Burns Night.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "General Knowledge",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "Francis Bacon died from a fatal case of pneumonia while he was attempting to preserve meat by stuffing a chicken with snow.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "General Knowledge",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "Popcorn was invented in 1871 by Frederick W. Rueckheim in the USA where he sold the snack on the streets of Chicago.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "category": "General Knowledge",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "The British organisation CAMRA stands for The Campaign for Real Ale.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "General Knowledge",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "The commercial UK channel ITV stands for &quot;International Television&quot;.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "category": "General Knowledge",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "The pickled gherkin was first added to hamburgers because a US health law required all fast-food to include a source of Vitamin C.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "category": "General Knowledge",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "Vietnam&#039;s national flag is a red star in front of a yellow background.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "category": "General Knowledge",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "A pasodoble is a type of Italian pasta sauce.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "category": "General Knowledge",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "Instant mashed potatoes were invented by Canadian Edward Asselbergs in 1962.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "General Knowledge",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "The mitochondria is the powerhouse of the cell.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "General Knowledge",
#         "type": "boolean",
#         "difficulty": "hard",
#         "question": "NCIS stands for &quot;Navy Corps Investigative Service&quot;",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "category": "General Knowledge",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "Jingle Bells was originally meant for Thanksgiving",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "General Knowledge",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "Ping-Pong originated in England",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     }
# ]
