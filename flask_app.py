from flask import Flask, request
import openai
import pymysql

connection = pymysql.connect(
    host="localhost", # Change this to the hostname or IP address of your database server
    user="root", # Change this to the username for accessing the database
    password="admin123", # Change this to the password for the user
    db="heartrate", # Change this to the name of the database you want to connect to
    cursorclass=pymysql.cursors.DictCursor
)



app = Flask(__name__)

openai.api_key = "00"

gpt_prompt = """

Database contains the following schema "CREATE TABLE `fitrockr_intradaydata` (
  `User Id` int(11) NOT NULL DEFAULT '0',
  `User First Name` text,
  `Household ID` text,
  `User Email` text,
  `Team Names` text,
  `Group Names` text,
  `Calendar Date (Local)` text,
  `Start Time (Local)End Time (Local)` text,
  `End Time (Local)` text,
  `Time Zone (Local)` text,
  `Calendar Date (UTC)` text,
  `Start Time (UTC)` text,
  `End Time (UTC)` text,
  `Start Time (s)` text,
  `Time Zone (s)` text,
  `Duration (s)` text,
  `Active Seconds` text,
  `Activity Type` text,
  `Active Calories` text,
  `Distance (m)` text,
  `Steps` text,
  `Met Value` text,
  `Intensity` text,
  `Stress Level (avg)` text,
  `Stress Level (max)` text,
  `Motion Intensity (avg)` text,
  `Motion Intensity (max)` text,
  `HasHeartRate` text,
  `HeartRateCount` text,
  `AvgHeartRate` text,
  `MinHeartRate` text,
  `MaxHeartRate` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;"
 """


# prompt = f"{gpt_prompt} {user_input}"

def generate_sql_query(prompt, max_tokens=50, temperature=0.2, top_p=1.0, frequency_penalty=0.0, presence_penalty=0.0):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"{gpt_prompt} Create one SQL query for the following command: {prompt}",
        max_tokens=60,
        temperature=0.1,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty
    )
    return response.choices[0].text

@app.route("/", methods=["GET", "POST"])
def generate_sql():
    if request.method == "POST":
        prompt = request.form.get("prompt")
        sql_query = generate_sql_query(prompt)
        with connection.cursor() as cursor:
            cursor.execute(sql_query)
            result = cursor.fetchall()
        return str(result)
    return '''
        <form method="post">
            Prompt: <input type="text" name="prompt">
            <input type="submit" value="Submit">
        </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
