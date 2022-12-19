import os
import datetime

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource
from flask_migrate import Migrate


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)
api = Api(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(20), unique=True, nullable=False)
    phone = db.Column(db.String(10), unique=True, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.datetime.now)

    def __repr__(self):
        return "<Post %s>" % self.user_id


class PostSchema(ma.Schema):
    class Meta:
        fields = ("id", "user_id", "phone", "created_at")
        model = Post


post_schema = PostSchema()
posts_schema = PostSchema(many=True)


class PostListResource(Resource):
    def get(self):
        posts = Post.query.all()
        return posts_schema.dump(posts)

    def post(self):
        new_post = Post(
            user_id=request.json["user_id"],
            phone=request.json["phone"],
            # created_at=request.json["created_at"],
        )
        db.session.add(new_post)
        db.session.commit()
        return post_schema.dump(new_post)


class PostResource(Resource):
    def get(self, id):
        post = Post.query.get_or_404(id)
        return post_schema.dump(post)

    def patch(self, id):
        post = Post.query.get_or_404(id)
        if "user_id" in request.json:
            post.user_id = request.json["user_id"]
        if "phone" in request.json:
            post.phone = request.json["phone"]
        db.session.commit()
        return post_schema.dump(post)

    def delete(self, id):
        post = Post.query.get_or_404(id)
        db.session.delete(post)
        db.session.commit()
        return "", 204


class FilterResource(Resource):
    def get(self):
        post = {}
        if "user_id" in request.json:
            post["user_id"] = request.json["user_id"]
        if "phone" in request.json:
            post["phone"] = request.json["phone"]
        if "created_at" in request.json:
            post["created_at"] = request.json["created_at"]
        users = Post.query.filter_by(**post)
        return posts_schema.dump(users)


api.add_resource(PostListResource, "/posts")
api.add_resource(PostResource, "/posts/<int:id>")
api.add_resource(FilterResource, "/filter")

if __name__ == "__main__":
    app.run(debug=True)
