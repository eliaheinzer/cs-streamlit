def get_question(category, difficulty):
    params ={"amount":1,"category":category,"difficulty":difficulty}
    api_answer = requests.get("https://opentdb.com/api.php?", params = params)
    answer = api_answer.json()
    print(answer)
    return

get_question("Art","Easy")
