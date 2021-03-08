import os
from app import app, url_for, redirect, request, render_template, abort
from app.exception.AuthorizationException import AuthorizationException
from app.data import messages, constants
from app.service.AppService import AppService
from app.service.JsonService import JsonService
from app.service.SpotifyApiService import SpotifyApiService
from app.service.SpotifyAuthService import SpotifyAuthService

authorized = False


# ----------------------------------------
# controllers
# ----------------------------------------


@app.route('/unauthorized')
def unauthorizedPage():
    """ if spotify client credential authorization fails """
    if authorized:
        return redirect("/")
    return render_template(constants.error_page_template, error=messages.authorization_error)


try:
    """ if spotify client credential authorization is achieved parts in try will be executed """

    json_service = JsonService(messages.input_not_match, constants.genre_json_file_path)
    spotify_auth_service = SpotifyAuthService(os.getenv('SP_CLIENT_ID'), os.getenv('SP_CLIENT_SECRET'))
    spotify_api_service = SpotifyApiService(spotify_auth_service, constants.popular_track_list_range,
                                            messages.artist_not_found, messages.track_not_found)
    app_service = AppService(json_service, spotify_api_service, messages.input_empty, messages.input_not_match)
    authorized = True


    @app.route('/')
    def home():
        return redirect(url_for('genrePage'))


    @app.route('/tracks')
    def genrePage():
        """ Home page """
        if request.args is not None and len(request.args) > 0:
            genre = request.args.get('genre')
            if genre is '':
                abort(400, messages.input_empty)
            return redirect(url_for('trackList', genre=genre))
        genre_list = app_service.getGenreTypeList()
        return render_template(constants.enter_genre_template, genre_list=genre_list)


    @app.route('/tracks/<genre>', methods=["GET"])
    def trackList(genre):
        """ list the popular tracks """
        try:
            content = app_service.listTopTracks(genre)
            return render_template(constants.track_list_page_template, genre=genre, content=content)
        except Exception as ex:
            print(str(ex))
            abort(400, messages.general_error)


    @app.route('/error')
    def errorPage(error_desc=None):
        if error_desc is None:
            return redirect(url_for('genrePage'))
        return render_template(constants.error_page_template, error=error_desc)

except AuthorizationException as e:
    redirect("/unauthorized")
    """ if spotify client credential authorization fails, then each button displayed should be ineffective """


    @app.route('/')
    def routeHomeToUnAuthPage():
        return redirect("/unauthorized")


    @app.route('/tracks')
    def routeTracksToUnAuthPage():
        return redirect("/unauthorized")
