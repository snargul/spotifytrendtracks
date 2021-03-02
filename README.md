# Spotify Trend Tracks

This is a simple web application Flask project using Spotify Web API in oder to list 5 popular tracks of a randomly selected artist by entering an available genre type.

![Screenshot](https://i.imgur.com/o0zTxLc.png)

## Dependencies

 - Python 3.7.4
 - Flask 1.1.2
 - spotipy 2.16.1

## Installation

* Clone:
```
$ git clone https://github.com/snargul/spotifytrendtracks.git
$ cd tracks
```
* Register your application on Spotify: [Register Your App on Spotify](https://developer.spotify.com/documentation/general/guides/app-settings/#register-your-app)

* Add your CLIENT ID and CLIENT SECRET info to system environment variables as given below:
```
* CLIENT ID
    Variable name: SP_CLIENT_ID
    Variable value: ********************************
* CLIENT SECRET
    Variable name: SP_CLIENT_SECRET
    Variable value: ********************************
```
* Download the required packages given in requirements.txt

All set! Run the application:
```
cd yourapplication
$ python run.py
* Running on http://127.0.0.1:8080/
```
And then open it at [http://127.0.0.1:8080/](http://127.0.0.1:8080/)


## Features

 - minimal production-ready Flask application: root package, sample static resource, sample template and an index view,
   as per [Larger Applications](http://flask.pocoo.org/docs/0.12/patterns/packages/)

 - configuration system, as per [Configuration Handling](http://flask.pocoo.org/docs/0.12/config/#config)
 
 - [argparse](https://docs.python.org/3/library/argparse.html): for command line arguments. ip and port information can be change with '--ip' and '--port' prefixes.
 
 - [spotipy2.0](https://spotipy.readthedocs.io/en/2.16.1/) : Python library for the Spotify Web API
 
 - Client Credential Flow: is used for Spotify server-to-server authentication with [OAuth2](https://spotipy.readthedocs.io/en/2.16.1/#module-spotipy.oauth2)
 
 - exception handling


