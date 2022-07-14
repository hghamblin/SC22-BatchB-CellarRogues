# Run by typing python3 main.py

# import basics
import os
import re
# import stuff for our web server
from flask import Flask, request, redirect, url_for, render_template, session
from utils import get_base_url

# import stuff for our models
from aitextgen import aitextgen

# load models
ai = aitextgen(model="distilgpt2", to_gpu=False)

ai_adventure_time = aitextgen(model_folder="models/adventure-time/", to_gpu = False)
'''
ai_seinfeld = aitextgen(model_folder="models/seinfeld/", to_gpu = False)
ai_spongebob = aitextgen(model_folder="models/spongebob/", to_gpu = False)
ai_arthur = aitextgen(model_folder="models/arthur/", to_gpu = False)
ai_simpsons = aitextgen(model_folder="models/the-simpsons/", to_gpu = False)
ai_office = aitextgen(model_folder="models/the-office/", to_gpu = False)
ai_futurama = aitextgen(model_folder="models/futurama/", to_gpu = False)
ai_avatar = aitextgen(model_folder="models/avatar/", to_gpu = False)
'''

def generate_text(prompt=None, ai=ai):
    if prompt is not None:
        generated = ai.generate(
            n=1,
            prompt=str(prompt),
            max_length=100,
            temperature=0.9,
            return_as_list=True
        )
    
    # select first five generated lines
    generated = generated[0].split('\n')[:5]
    
    # format lines
    clean_lines = []
    for line in generated:
        if ':' in line:
            parts = line.split(':', 1)
            
            character = parts[0]
            line = parts[1]
            
            # bold character names
            clean_lines.append(f"<b>{character}</b>: {line}")
        else:
            clean_lines.append(line)
        
    generated = '<br>'.join(clean_lines)
    
    return generated

# setup the webserver
# port may need to be changed if there are multiple flask servers running on same server
port = 12345
base_url = get_base_url(port)


# if the base url is not empty, then the server is running in development, and we need to specify the static folder so that the static files are served
if base_url == '/':
    app = Flask(__name__)
else:
    app = Flask(__name__, static_url_path=base_url+'static')

app.secret_key = os.urandom(64)

# HOME PAGE
@app.route(f'{base_url}')
def home():
    return render_template('index.html', generated=None)

# TV SHOW SELECTION PAGE
@app.route(f'{base_url}/tv_show_selection/')
def tv_show_selection():
    return render_template('tv_show_selection.html')

# TV SHOW SPECIFIC PAGES
# adventure time
@app.route(f'{base_url}/adventure_time')
def adventure_time():
    if 'data' in session:
        data = session['data']
        return render_template('adventure-time.html', generated=data)
    else:
        return render_template('adventure-time.html', generated="<center>The script will be generated here!</center>")

@app.route(f'{base_url}/adventure_time_results', methods=["POST"])
def adventure_time_results():

    character = request.form['character']
    prompt = request.form['prompt']
    
    if character == "Default":
        character = "Finn"

    generated = generate_text(prompt=f'{character}: {prompt}', ai=ai_adventure_time)

    data = {'generated_ls': generated}
    session['data'] = generated
    return redirect(url_for('adventure_time'))

# arthur
@app.route(f'{base_url}/arthur')
def arthur():
    if 'data' in session:
        data = session['data']
        return render_template('arthur.html', generated=data)
    else:
        return render_template('arthur.html', generated="<center>The script will be generated here!</center>")

@app.route(f'{base_url}/arthur_results', methods=["POST"])
def arthur_results():

    character = request.form['character']
    prompt = request.form['prompt']
    
    if character == "Default":
        character = "Arthur"

    generated = generate_text(prompt=f'{character}: {prompt}', ai=ai_arthur)

    data = {'generated_ls': generated}
    session['data'] = generated
    return redirect(url_for('arthur'))

# avatar
@app.route(f'{base_url}/avatar')
def avatar():
    if 'data' in session:
        data = session['data']
        return render_template('avatar.html', generated=data)
    else:
        return render_template('avatar.html', generated="<center>The script will be generated here!</center>")

@app.route(f'{base_url}/avatar_results', methods=["POST"])
def avatar_results():

    character = request.form['character']
    prompt = request.form['prompt']
    
    if character == "Default":
        character = "Aang"

    generated = generate_text(prompt=f'{character}: {prompt}', ai=ai_avatar)

    data = {'generated_ls': generated}
    session['data'] = generated
    return redirect(url_for('avatar'))

# futurama
@app.route(f'{base_url}/futurama')
def futurama():
    if 'data' in session:
        data = session['data']
        return render_template('futurama.html', generated=data)
    else:
        return render_template('futurama.html', generated="<center>The script will be generated here!</center>")

@app.route(f'{base_url}/futurama_results', methods=["POST"])
def futurama_results():

    character = request.form['character']
    prompt = request.form['prompt']
    
    if character == "Default":
        character = "Fry"

    generated = generate_text(prompt=f'{character}: {prompt}', ai=ai_futurama)

    data = {'generated_ls': generated}
    session['data'] = generated
    return redirect(url_for('futurama'))

# seinfeld
@app.route(f'{base_url}/seinfeld')
def seinfeld():
    if 'data' in session:
        data = session['data']
        return render_template('seinfeld.html', generated=data)
    else:
        return render_template('seinfeld.html', generated="<center>The script will be generated here!</center>")

@app.route(f'{base_url}/seinfeld_results', methods=["POST"])
def seinfeld_results():

    character = request.form['character']
    prompt = request.form['prompt']
    
    if character == "Default":
        character = "Jerry"

    generated = generate_text(prompt=f'{character}: {prompt}', ai=ai_seinfeld)

    data = {'generated_ls': generated}
    session['data'] = generated
    return redirect(url_for('seinfeld'))

# spongebob
@app.route(f'{base_url}/spongebob')
def spongebob():
    if 'data' in session:
        data = session['data']
        return render_template('spongebob.html', generated=data)
    else:
        return render_template('spongebob.html', generated="<center>The script will be generated here!</center>")

@app.route(f'{base_url}/spongebob_results', methods=["POST"])
def spongebob_results():

    character = request.form['character']
    prompt = request.form['prompt']
    
    if character == "Default":
        character = "Spongebob"

    generated = generate_text(prompt=f'{character}: {prompt}', ai=ai_spongebob)

    data = {'generated_ls': generated}
    session['data'] = generated
    return redirect(url_for('spongebob'))

# the office
@app.route(f'{base_url}/the_office')
def the_office():
    if 'data' in session:
        data = session['data']
        return render_template('the-office.html', generated=data)
    else:
        return render_template('the-office.html', generated="<center>The script will be generated here!</center>")

@app.route(f'{base_url}/the_office_results', methods=["POST"])
def the_office_results():

    character = request.form['character']
    prompt = request.form['prompt']
    
    if character == "Default":
        character = "Michael"

    generated = generate_text(prompt=f'{character}: {prompt}', ai=ai_the_office)

    data = {'generated_ls': generated}
    session['data'] = generated
    return redirect(url_for('the_office'))

# the simpsons
@app.route(f'{base_url}/the_simpsons')
def the_simpsons():
    if 'data' in session:
        data = session['data']
        return render_template('the-simpsons.html', generated=data)
    else:
        return render_template('the-simpsons.html', generated="<center>The script will be generated here!</center>")

@app.route(f'{base_url}/the_simpsons_results', methods=["POST"])
def the_simpsons_results():

    character = request.form['character']
    prompt = request.form['prompt']
    
    if character == "Default":
        character = "Bart"

    generated = generate_text(prompt=f'{character}: {prompt}', ai=ai_simpsons)

    data = {'generated_ls': generated}
    session['data'] = generated
    return redirect(url_for('the_simpsons'))

if __name__ == '__main__':
    # IMPORTANT: change url to the site where you are editing this file.
    website_url = 'cocalc7.ai-camp.dev'

    print(f'Try to open\n\n    https://{website_url}' + base_url + '\n\n')
    app.run(host='0.0.0.0', port=port, debug=True)
