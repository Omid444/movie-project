
HEADER = 'My Movie App'

def serialize_animal(movies_list):
    """This function support dict from data fetcher to make suitable text"""
    movie_text = ''
    body_text = ''
    header_text = '<div class="list-movies-title">'\
             f'<h1>{HEADER}</h1></div><div>'
    body_tag_start = '<ol class="movie-grid">'
    body_tag_end = '</ol></div></div>'
    for title, year_poster in movies_list.items():
        year = year_poster['year']
        poster_url = year_poster['poster']
        movie_data = f'<li><div class="movie">'\
                f'<img class="movie-poster"'\
                f'src={poster_url}/>'\
                f'<div class="movie-title">{title}</div>'\
                f'<div class="movie-year">{year}</div></div></li>'

        movie_text += movie_data
    body_text = body_tag_start + movie_text + body_tag_end
    return header_text,body_text


def read_html(file_path, header, body):
    """Read html file and return needed content"""
    with open(file_path, "r", encoding="utf-8") as html_file:
        index = html_file.read()
        content_file = index.replace("__TEMPLATE_TITLE__", header)
        content_file = content_file.replace("__TEMPLATE_MOVIE_GRID__", body)
        return content_file


def write_html(file_path, index):
    """Write text into html"""
    with open(file_path, "w", encoding="utf-8") as html_file:
        html_file.write(index)


def gen_web(movies):
    """Generate html file based on index_template.html in current directory"""
    if movies:
        header, body = serialize_animal(movies)
        index = read_html('./_static/index_template.html', header, body)
        write_html('./_static/my_movies_app.html', index)
        print('Website was successfully generated to the file index_template.html.')
    else:
        print('No movies found in database')
        header = f"<h2 style='font-family: sans-serif;'>No movies found in database</h2>"
        index = read_html('./_static/index_template.html', header)
        write_html('./_static/my_movies_app.html', index )


