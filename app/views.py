from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db, lm
from .forms import AdminLogin, NewPost
from .models import Admin, Post
from datetime import datetime
from config import POSTS_PAGE


@app.route("/", methods=["GET"])
@app.route("/home", methods=["GET"])
@app.route("/home/<int:page>", methods=["GET"])
def home(page=1):

    # Paginate posts by newest post time.
    posts = Post.query.order_by(Post.timestamp.desc()).paginate(page, POSTS_PAGE, False)
    page_css = url_for('static', filename='css/post.css')
    return render_template("home.html", title="Home", posts=posts,
                           page_css=page_css)


@app.route("/about")
def about():

    return render_template("about.html", title="About")


@app.route("/projects")
def projects():

    return render_template("projects.html", title="Projects")


@app.route("/admin", methods=["GET", "POST"])
def admin():

    # Check if user is already logged in.
    if g.user is not None and g.user.is_authenticated:

        return redirect(url_for("home"))

    form = AdminLogin()

    # Check for login form submitted.
    if form.validate_on_submit():

        # Crosscheck username from form given to user's in db.
        # If user is in db and password is correct, login and redirect to home page.
        # Throw errors otherwise.
        user = Admin.query.filter_by(username=form.username.data).first()
        if user is not None:

            if user.password == form.password.data:

                login_user(user, remember=form.remember_me.data)
                return redirect(request.args.get('next') or url_for('home'))

            else:

                flash("Incorrect password/username combo.")

        else:

            flash("That username does not exist.")

    return render_template("admin.html", title="Sign In",
                           form=form)


@app.route("/post", methods=["GET", "POST"])
@login_required
def post():

    form = NewPost()

    # Check for post form submitted, add post to db, then redirect to home page.
    if form.validate_on_submit():

        new_post = Post(title=form.title.data, body=form.body.data, timestamp=datetime.utcnow(), author=g.user)
        db.session.add(new_post)
        db.session.commit()

        return redirect(url_for("home"))

    page_css = url_for("static", filename="css/new_post.css")
    extra_script = url_for("static", filename="js/newPost.js")
    return render_template("new_post.html", title="New Post", form=form, page_css=page_css,
                           extra_script=extra_script)


@app.route("/delete/<int:post_id>", methods=["GET"])
@login_required
def delete(post_id=0):

    # Takes a post id, finds it in the db, deletes it, then redirects to home page.
    post_delete = Post.query.filter_by(id=post_id).first()
    db.session.delete(post_delete)
    db.session.commit()

    return redirect(url_for("home"))

@app.route("/edit/<int:post_id>", methods=["GET", "POST"])
@login_required
def edit(post_id=0):

    form = NewPost()
    old_post = Post.query.filter_by(id=post_id).first()

    if form.validate_on_submit():

        old_post.title = form.title.data
        old_post.body = form.body.data
        old_post.timestamp = datetime.utcnow()
        old_post.author = g.user
        db.session.commit()

        return redirect(url_for("home"))

    else:

        form.title.data = old_post.title
        form.body.data = old_post.body

    return render_template("new_post.html", title="Edit Post", form=form)


@app.route("/logout")
def logout():

    logout_user()
    return redirect(url_for("home"))


@lm.user_loader
def load_user(user_id):

    return Admin.query.get(int(user_id))


@app.before_request
def before_request():

    g.user = current_user
