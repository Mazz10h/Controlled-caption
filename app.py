from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Use SQLite for simplicity
db = SQLAlchemy(app)

class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    url = db.Column(db.String(255), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    uploaded_date = db.Column(db.Date, nullable=False)
    caption_tracks = db.relationship('CaptionTrack', backref='video', lazy=True)

class CaptionTrack(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    language = db.Column(db.String(50), nullable=False)
    format = db.Column(db.String(50), nullable=False)
    video_id = db.Column(db.Integer, db.ForeignKey('video.id'), nullable=False)
    caption_segments = db.relationship('CaptionSegment', backref='caption_track', lazy=True)

class CaptionSegment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.Time, nullable=False)
    end_time = db.Column(db.Time, nullable=False)
    text = db.Column(db.Text, nullable=False)
    caption_track_id = db.Column(db.Integer, db.ForeignKey('caption_track.id'), nullable=False)

@app.route('/')
def index():
    videos = Video.query.all()
    return render_template('index.html', videos=videos)

@app.route('/video/<int:video_id>')
def video_details(video_id):
    video = Video.query.get(video_id)
    return render_template('video_details.html', video=video)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

