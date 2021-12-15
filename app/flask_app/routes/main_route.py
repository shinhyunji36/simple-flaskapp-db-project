from flask import Blueprint, render_template, request, redirect, url_for, Response, session
from flask_app.models import  Comment, Gympost, delete_post, get_table
from flask_app import models, db

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')


# read (운동 기록 확인)
@bp.route('/posts',methods = ['GET'])
def post_list():
    post_list = get_table()
    return render_template('list.html', post_list = post_list)


# create (운동 기록 등록)
@bp.route('/posts/create', methods = ['POST','GET'])
def create():
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


# read
@bp.route('/posts/<int:id>')
def read(id):
    post = Gympost.query.get(id)
    return render_template('read.html', post=post)


# delete
@bp.route('/posts/<int:id>/delete') 
def delete(id):
    post = Gympost.query.get(id)
    
    delete_post(id)

    return redirect(url_for('main.post_list'))

# edit
@bp.route('/posts/<int:id>/edit')
def edit(id):
    post = Gympost.query.get(id)
    return render_template('edit.html',post=post)


#update
@bp.route('/posts/<int:id>/update', methods=["POST"])
def update(id):
    post = Gympost.query.get(id)
    post.machine = request.form.get('machine')
    post.weight = request.form.get('weight')
    post.num_1set = request.form.get('num_1set')
    post.total_set = request.form.get('total_set')
    
    db.session.commit()
    
    return redirect('/posts/{}'.format(id))


########################################

@bp.route('/posts/<int:post_id>/comments',methods=['POST'])
def comments(post_id):
    if request.method =='POST':
        new_comment = Comment(
            content = request.form['content'],
            creator = request.form['creator'],
        )

        post = Gympost.query.get(post_id)
        post.comments.append(new_comment)
        db.session.add(new_comment)
        db.session.commit()
    
    return redirect('/posts/{}'.format(post_id))
    


@bp.route('/comment/<int:id>/delete')
def comment_delete(id):

    comment = Comment.query.get(id)

    db.session.delete(comment)
    db.session.commit()
    
    return redirect('/')


#############

# DATA ANALYSIS


@bp.route('/predict')
def predict():
    count1 = 6 #Gympost.query.all.filter_by(machine='불가리안 백')
    # count2 = Gympost.query.all

    return render_template('classification.html', count1=count1)