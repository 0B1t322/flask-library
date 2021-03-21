from app import app

__css_base_path__ = app.config.get('CSS_BASE_PATH')

def to_css(name):
    return f'{__css_base_path__}/{name}'