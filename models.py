"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


db = SQLAlchemy()

bcrypt = Bcrypt()

class Playlist(db.Model):
    """Playlist."""

    __tablename__ = "playlists"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text, nullable = False)
    description = db.Column(db.Text, nullable = False)
    
    #added the code below for testing
    # new_songs_title = db.Column(db.Text, db.ForeignKey("songs.title"), nullable = False)
    # new_songs = db.relationship("Song", back_populates = "new_playlists")
    songs = db.relationship("Song", secondary = "playlistsongs", backref = "playlists")

class Song(db.Model):
    """Song."""

    __tablename__ = "songs"

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.Text, nullable = False)
    artist = db.Column(db.Text, nullable = False)
    
    #added the code below for testing
    # new_playlists = db.relationship("Playlist", back_populates = "new_songs")

class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""

    __tablename__ = "playlistsongs"

    id = db.Column(db.Integer, primary_key = True)
    playlist_id = db.Column(db.Integer, db.ForeignKey("playlists.id"),nullable = False)
    song_id = db.Column(db.Integer, db.ForeignKey("songs.id"), nullable = False)

    # song = db.relationship("Song", backref="playlist_songs")
    # playlist = db.relationship("Playlist", backref="playlist_songs")


# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

