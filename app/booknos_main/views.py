from app.booknos_main.forms import BookForm
# dbをimport
from app.app import db
# bookクラスをimport
from app.booknos_main.models import Book

from flask import Blueprint, render_template, redirect, url_for


# Blueprintでmainアプリを作成する
booknos_main = Blueprint(
    "booknos_main",
    __name__,
    template_folder="templates",
    static_folder="static",
)


# indexエンドポイントを作成しindex.htmlを返す
@booknos_main.route("/")
def index():
    return render_template("booknos_main/index.html")


"""
@booknos_main.route("/books/new", methods=["GET", "POST"])
def create_book():
    # bookFormをインスタンス化する
    form = BookForm()
    # フォームの値をバリデートする
    if form.validate_on_submit():
        # ユーザを作成する
        book = Book(
            title=form.bookname.data,
            email=form.email.data,
            password=form.password.data,
        )
        # ユーザを追加してコミットする
        db.session.add(book)
        db.session.commit()
        # ユーザの一覧画面へリダイレクトする
        return redirect(url_for("booknos_main.books"))

    return render_template("booknos_main/create.html", form=form)
"""


@booknos_main.route("/books")
def books():
    """ユーザの一覧を取得する"""
    books = Book.query.all()
    return render_template("booknos_main/index.html", books=books)


"""
@booknos_main.route("/books/<book_id>", methods=["GET", "POST"])
def edit_book(book_id):
    form = bookForm()

    # bookモデルを利用してユーザーを取得する
    book = book.query.filter_by(id=book_id).first()

    # formからサブミットされた場合はユーザーを更新してユーザー一覧画面へダイレクトする
    if form.validate_on_submit():
        book.bookname = form.bookname.data
        book.email = form.email.data
        book.password = form.password.data
        db.session.add(book)
        db.session.commit()
        return redirect(url_for("main.books"))

    # GETの場合はHTMLを返す
    return render_template("main/edit.html", book=book, form=form)


@booknos_main.route("/books/<book_id>/delete", methods=["POST"])
def delete_book(book_id):
    book = book.query.filter_by(id=book_id).first()
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for("main.books"))
"""
