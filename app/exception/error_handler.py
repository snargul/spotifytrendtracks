from app import app, render_template
from app.data.constants import error_page_template
from app.data import messages


@app.errorhandler(400)
def bad_req(e):
    """1 parameter is given in order to match flask invalid_route()"""
    msg = e
    if e is not None and e.description is not None:
        msg = e.description
    return render_template(error_page_template, error=msg)


@app.errorhandler(404)
def not_found(e):
    """1 parameter is given in order to match flask invalid_route()"""
    return render_template(error_page_template, error=messages.page_not_found)


@app.errorhandler(500)
def type_error(e):
    """1 parameter is given in order to match flask invalid_route()"""
    return render_template(error_page_template, error=messages.type_error)
