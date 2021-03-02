from app import app, url_for, redirect, request, render_template, jsonify, make_response
from app.exception.AuthorizationException import AuthorizationException
from app.data.constants import enter_genre_template, error_page_template
from app.data import messages

authorized = False


# ----------------------------------------
# controllers
# ----------------------------------------


@app.route('/unauthorized')
def unauthorizedPage():
    """ if spotify client credential authorization fails """
    if authorized:
        return redirect("/")
    return render_template(error_page_template, error=messages.authorization_error)


try:
    """ if spotify client credential authorization is achieved parts in try will be executed """
    from app.service.AppService import AppService

    app_service = AppService()
    authorized = True


    @app.route('/')
    def home():
        return redirect(url_for('genrePage'))


    @app.route('/tracks')
    def genrePage():
        """ Home page """
        genre_list = app_service.getGenreTypeList()
        return render_template(enter_genre_template, genre_list=genre_list)


    @app.route('/tracks/<genre>', methods=["GET"])
    def trackList(genre):
        """ list the popular tracks """
        try:
            if request.is_json:
                content = app_service.listTopTracks(genre)
                res = make_response(jsonify(content), 200)
                return res
            else:
                return errorPage(messages.page_not_found)
        except Exception as ex:
            return errorPage(ex)


    @app.route('/error')
    def errorPage(error):
        return render_template(error_page_template, error=error)

except AuthorizationException as e:
    redirect("/unauthorized")
    """ if spotify client credential authorization fails, then each button displayed should be ineffective """


    @app.route('/')
    def routeHomeToUnAuthPage():
        return redirect("/unauthorized")


    @app.route('/tracks')
    def routeTracksToUnAuthPage():
        return redirect("/unauthorized")