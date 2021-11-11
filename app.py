from flask import Flask, render_template, jsonify,request, redirect, Blueprint
from main.intro import intro 
from main.statistics import statistics
from main.login_join import login_join
from main.feed import feed
from main.my_page import mypage
from main.about_us import about_us

app = Flask(__name__)

# Page blueprint
'''
intro : 인트로 페이지
statistics : 통계 페이지
login_join : 로그인 페이지
feed : 피드 페이지
mypage : 마이페이지
about_us : 팀 소개 페이지
'''
app.register_blueprint(intro)
app.register_blueprint(statistics)
app.register_blueprint(login_join)
app.register_blueprint(feed)
app.register_blueprint(mypage)
app.register_blueprint(about_us)


# root url
@app.route('/')
def index():
    return render_template('intro.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
