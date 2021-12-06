from flask import Blueprint, render_template, request, redirect, url_for, Response, session
from flask_app.models import User, Gympost, delete_post, get_table, delete_post
from flask_app import models, db

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/refresh')
def refresh():
    db.drop_all()
    db.create_all()
    return redirect(url_for('main.index'), code = 200)


# 회원 routes : 회원 등록 / 로그인 / 로그아웃 
@bp.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        new_user = User(
            name = request.form['name'],
            email = request.form['email'],
            password = request.form['password']
        )
        
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('main.login'))
    return render_template('register.html')

# not work
@bp.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        data = User.query.filter_by(email = email, password = password).first()

        if data is not None:
            session['email'] = email
            return redirect(url_for('main.index'))
        else:
            return "'id'가 존재하지 않거나, 'password'가 일치하지 않습니다."
    return render_template('login.html')


@bp.route('/logout', methods=['GET'])
def logout():
	session.pop('email', None)
	return redirect('/')



# create (운동 기록 등록)
@bp.route('/post', methods = ['GET','POST'])
def post():
    if request.method =='POST':
        new_post = Gympost(
            name = request.form['name'],
            date = request.form['date'],
            machine = request.form['machine'],
            weight = request.form['weight'],
            num_1set = request.form['num_1set'],
            total_set = request.form['total_set']
        )

        db.session.add(new_post)
        db.session.commit()


        return redirect(url_for('main.post_list'))
    return render_template('add.html')



# read (운동 기록 확인)
@bp.route('/list',methods = ['GET'])
def post_list():
    post_list = get_table()
    return render_template('list.html', post_list = post_list)


# delete
@bp.route('/list/')
@bp.route('/list/<post_id>')
def delete_posts(post_id=None):
    # if post_id is None:
    #     return "400 error", 400

    # delete = delete_post(post_id)
    # if delete is None:
    #     return "404 error", 404
    # else:
    delete_post(post_id)
    return redirect(url_for('main.post_list'), code = 200)

