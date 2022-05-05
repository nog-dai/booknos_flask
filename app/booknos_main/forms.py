from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, length, NumberRange


# ユーザ新規作成とユーザ編集フォームクラス
class BookForm(FlaskForm):
    title = StringField(
        "タイトル",
        validators=[
            DataRequired(message="タイトルは必須です")
        ],
    )

    auther = StringField(
        "著者",
    )

    description = StringField(
        "概要",
        validators=[
            length(max=65536, message="65536文字以内で入力してください")
        ],
    )

    isbn_code_10 = StringField(
        "ISBNコード(10文字)",
        validators=[
            length(min=10, max=10, message="10文字で入力してください")
        ],
    )

    isbn_code_13 = StringField(
        "ISBNコード(13文字)",
        validators=[
            length(min=13, max=13, message="13文字で入力してください")
        ],
    )

    total = NumberRange(min=10, message="1冊以上から登録してください")

    # ユーザフォームのsubmitの文言を設定する
    submit = SubmitField("新規登録")
