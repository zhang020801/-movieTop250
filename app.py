from flask import Flask,render_template
import sqlite3
app = Flask(__name__)


@app.route("/index")
def index():
    datalist = []
    conn = sqlite3.connect("movie.db")
    cur = conn.cursor()
    sql = "select  id,info_link, pic_link, cname, ename, score, rated, instroduction, info from movie250"
    data = cur.execute(sql)
    for item in data:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template("index.html",movies = datalist)

@app.route("/shuju")
def shuju():
    return render_template("shuju.html")
@app.route("/score")
def score():
    score = []
    num = []
    conn = sqlite3.connect("movie.db")
    cur = conn.cursor()
    sql = "select score,count(score) from movie250 group by score"
    data = cur.execute(sql)
    for item in data:
        score.append(item[0])
        num.append(item[1])
    cur.close()
    conn.close()
    return render_template("score.html",score=score,num=num)
@app.route("/wordcloud")
def wordcloud():
    return render_template("wordcloud.html")
@app.route("/team")
def team():
    return render_template("team.html")


if __name__ == '__main__':
    app.run(debug=True)
