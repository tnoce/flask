from flask import Flask, render_template, session, request
import pandas as pd
import numpy as np
import sqlite3

app = Flask(__name__)

#conn = sqlite3.connect('database.sqlite')
#c = conn.cursor()

def count_word(text):
    txts = text
    result = []
    tmp = ""
    dic = {}
    
    for x in txts:
        if x != " " and x != "\n":
            tmp += x
        else:
            chikan = tmp.replace('\n', '').replace('(', '').\
            replace(')', '').replace('[', '').replace(']', '').\
            replace('.', '').replace(',', '').replace(':', '').\
            replace('-', '').replace('?','').replace('!','').replace('¥','')
            
            result.append(chikan.lower())
            tmp = ""
            
    for word in result:
        if not word in dic:
            dic[word] = 1
        else:
            dic[word] += 1
    
    s = pd.Series(dic)
    df = pd.DataFrame(s, columns=['単語数'])
    dfs = df.sort_values(by='単語数', ascending=False)

    return dfs


@app.route("/", methods=["GET","POST"])
def main_page():
    total = ''

    if request.method == 'POST':
        text = request.form['text']
        total = count_word(text)
        return render_template("index.html", text=text, total=total.to_html())
    
    return render_template("index.html", total=total)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8877)

